-- IMP-P1-01 performance correction. Published001-007 and all global invariants are unchanged.
-- This infrastructure state is transactional, not a client-controlled GUC/temp object or domain table.
CREATE TABLE dpt_ops.validation_pending (
    transaction_id xid8 PRIMARY KEY,
    generation bigint NOT NULL CHECK (generation>0),
    scheduled_generation bigint NOT NULL DEFAULT 0
        CHECK (scheduled_generation>=0 AND scheduled_generation<=generation)
);
REVOKE ALL ON TABLE dpt_ops.validation_pending FROM PUBLIC,dpt_owner,dpt_runtime,dpt_writer,dpt_curator,dpt_anonymous;

CREATE OR REPLACE FUNCTION dpt_guard.serialize_write() RETURNS trigger
LANGUAGE plpgsql SECURITY DEFINER SET search_path=pg_catalog,dpt,pg_temp AS $$
BEGIN
  IF current_setting('transaction_isolation') <> 'read committed' THEN
    RAISE EXCEPTION 'Local contract writes require read committed isolation' USING ERRCODE='25001';
  END IF;
  PERFORM pg_advisory_xact_lock(1900147);
  INSERT INTO dpt_ops.validation_pending(transaction_id,generation)
    VALUES(pg_current_xact_id(),1)
    ON CONFLICT(transaction_id) DO UPDATE SET generation=dpt_ops.validation_pending.generation+1;
  IF TG_OP='DELETE' THEN RETURN OLD; END IF;
  RETURN NEW;
END $$;

CREATE OR REPLACE FUNCTION dpt_guard.validate_all_deferred() RETURNS trigger
LANGUAGE plpgsql SECURITY DEFINER SET search_path=pg_catalog,dpt,pg_temp AS $$
DECLARE dirty_generation bigint;
BEGIN
  SELECT generation INTO dirty_generation FROM dpt_ops.validation_pending
    WHERE transaction_id=pg_current_xact_id() FOR UPDATE;
  IF NOT FOUND THEN RETURN NULL; END IF;
  -- Check the final transaction state with the exact existing validators, including all relationships.
  PERFORM dpt_guard.validate_model();
  PERFORM dpt_guard.validate_images();
  -- Exceptions/savepoint rollback restore state. Never erase writes made after this generation.
  DELETE FROM dpt_ops.validation_pending WHERE transaction_id=pg_current_xact_id()
    AND generation=dirty_generation;
  RETURN NULL;
END $$;

CREATE FUNCTION dpt_guard.schedule_validation() RETURNS trigger
LANGUAGE plpgsql SECURITY DEFINER SET search_path=pg_catalog,dpt,pg_temp AS $$
BEGIN
  -- BEFORE triggers also run on ON CONFLICT DO NOTHING. Schedule after the statement so even those
  -- attempts get a final flush/cleanup, and forcing this queue constraint IMMEDIATE cannot validate
  -- before the actual domain write. No marker exists for a truly untouched zero-row statement.
  UPDATE dpt_ops.validation_pending SET scheduled_generation=generation
    WHERE transaction_id=pg_current_xact_id() AND scheduled_generation<>generation;
  RETURN NULL;
END $$;

CREATE CONSTRAINT TRIGGER validation_pending_flush
AFTER UPDATE ON dpt_ops.validation_pending DEFERRABLE INITIALLY DEFERRED
FOR EACH ROW WHEN (NEW.scheduled_generation>OLD.scheduled_generation)
EXECUTE FUNCTION dpt_guard.validate_all_deferred();

DO $$ DECLARE item record; BEGIN
  FOR item IN SELECT tablename FROM pg_tables WHERE schemaname='dpt' ORDER BY tablename LOOP
    EXECUTE format('CREATE TRIGGER z_schedule_validation AFTER INSERT OR UPDATE OR DELETE ON dpt.%I FOR EACH STATEMENT EXECUTE FUNCTION dpt_guard.schedule_validation()',item.tablename);
  END LOOP;
END $$;

-- Existing function ACLs survive replacement; explicitly deny all new internal entry points too.
REVOKE ALL ON FUNCTION dpt_guard.serialize_write(),dpt_guard.validate_all_deferred(),dpt_guard.schedule_validation()
  FROM PUBLIC,dpt_owner,dpt_runtime,dpt_writer,dpt_curator,dpt_anonymous;
