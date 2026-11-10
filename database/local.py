"""Bounded local PostgreSQL harness. No remote-host/production connection interface."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import secrets
import subprocess
import time

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / ".local" / "p1-01"
CONTAINER = "doomparfum-p1-01"
VOLUME = "doomparfum-p1-01-data"
LABEL = "com.doomparfum.task=IMP-P1-01"
IMAGE = "postgres@sha256:f1c3376c26f2609ab9f29f71f824103fe2fcd8ee0346485cb6122a4f93df6f94"
DATABASES = {"dpt_foundation", "dpt_schema_test", "dpt_migration_probe"}


def docker(*args: str, input: str | None = None, check: bool = True):
    return subprocess.run(["docker", "--context", "desktop-linux", *args], input=input, text=True, encoding="utf-8",
                          capture_output=True, check=check)


def guard():
    assert_local_endpoint()
    info = json.loads(docker("inspect", CONTAINER).stdout)[0]
    if info["Config"].get("Labels", {}).get("com.doomparfum.task") != "IMP-P1-01":
        raise RuntimeError("Refusing an unrelated container")
    if info["Config"]["Image"] != IMAGE:
        raise RuntimeError("Local image pin differs")
    if not any(m.get("Type")=="volume" and m.get("Name")==VOLUME and m.get("Destination")=="/var/lib/postgresql/data" for m in info["Mounts"]):
        raise RuntimeError("Local volume identity differs")
    volume = json.loads(docker("volume", "inspect", VOLUME).stdout)[0]
    if volume.get("Labels", {}).get("com.doomparfum.task") != "IMP-P1-01":
        raise RuntimeError("Local volume task label differs")
    bindings = info["HostConfig"].get("PortBindings", {})
    if bindings != {"5432/tcp": [{"HostIp": "127.0.0.1", "HostPort": "55431"}]}:
        raise RuntimeError("Local loopback binding differs")


def sql(text: str, db: str = "dpt_schema_test", user: str = "postgres", check=True):
    if db not in DATABASES | {"postgres"}:
        raise ValueError("Database is outside the disposable task allowlist")
    guard()
    result = docker("exec", "-i", "--user", "postgres", CONTAINER,
                    "psql", "-X", "-q", "-A", "-t", "-v", "ON_ERROR_STOP=1",
                    "-v", "VERBOSITY=verbose", "-U", user, "-d", db,
                    input=text, check=False)
    if check and result.returncode:
        raise RuntimeError(result.stderr.strip())
    return result


def assert_local_endpoint():
    endpoint = docker("context", "inspect", "desktop-linux", "--format", "{{.Endpoints.docker.Host}}").stdout.strip()
    if not endpoint.startswith(("npipe:////./pipe/", "unix:///")):
        raise RuntimeError("Refusing a non-local Docker engine")


def start():
    assert_local_endpoint()
    exists = docker("inspect", CONTAINER, check=False)
    if exists.returncode == 0:
        guard()
        docker("start", CONTAINER)
    else:
        STATE.mkdir(parents=True, exist_ok=True)
        password_file = STATE / "postgres-password"
        if not password_file.exists():
            password_file.write_text(secrets.token_urlsafe(40), encoding="utf-8")
        volume = docker("volume", "inspect", VOLUME, check=False)
        if volume.returncode == 0:
            if json.loads(volume.stdout)[0].get("Labels", {}).get("com.doomparfum.task") != "IMP-P1-01":
                raise RuntimeError("Refusing an unrelated volume")
        else:
            docker("volume", "create", "--label", LABEL, VOLUME)
        docker("run", "-d", "--name", CONTAINER, "--label", LABEL,
               "--publish", "127.0.0.1:55431:5432", "--memory", "768m", "--cpus", "2",
               "--mount", f"type=volume,source={VOLUME},target=/var/lib/postgresql/data",
               "--mount", f"type=bind,source={password_file},target=/run/secrets/postgres-password,readonly",
               "-e", "POSTGRES_PASSWORD_FILE=/run/secrets/postgres-password",
               "-e", "POSTGRES_DB=dpt_foundation", "-e", "POSTGRES_INITDB_ARGS=--auth-host=scram-sha-256",
               IMAGE)
    for _ in range(45):
        probe = docker("exec", CONTAINER, "pg_isready", "-U", "postgres", check=False)
        if probe.returncode == 0:
            print("Local PostgreSQL ready on 127.0.0.1:55431; secret not printed")
            return
        time.sleep(1)
    raise RuntimeError("Local PostgreSQL did not become ready")


def recreate(db: str):
    if db not in DATABASES - {"dpt_foundation"}:
        raise ValueError("Automatic recreation is restricted to disposable test databases")
    sql(f'DROP DATABASE IF EXISTS "{db}" WITH (FORCE);', "postgres")
    sql(f'CREATE DATABASE "{db}";', "postgres")


def reset_empty_foundation():
    """Unpublished pilot reset only: refuse if any actual domain data or other connection exists."""
    names = json.loads((ROOT / "database/schema_contract.json").read_text(encoding="utf-8"))["logical_tables"]
    for name in names:
        if name != "field_definitions" and sql(f'SELECT count(*) FROM dpt."{name}";', "dpt_foundation").stdout.strip() != "0":
            raise RuntimeError("Foundation contains data; reset refused")
    if sql("SELECT count(*) FROM pg_stat_activity WHERE datname='dpt_foundation';", "postgres").stdout.strip() != "0":
        raise RuntimeError("Foundation has another connection; reset refused")
    sql('DROP DATABASE dpt_foundation;', "postgres")
    sql('CREATE DATABASE dpt_foundation;', "postgres")
    print("Recreated empty disposable foundation; no user/source/product data was present")


def migration_digest(file: Path):
    # Hash exactly the UTF-8/LF SQL text sent to psql, independent of checkout line endings.
    return hashlib.sha256(file.read_text(encoding="utf-8").encode("utf-8")).hexdigest()


def migrate(db: str = "dpt_foundation", extra: Path | None = None):
    sql("CREATE SCHEMA IF NOT EXISTS dpt_ops; CREATE TABLE IF NOT EXISTS dpt_ops.schema_migrations "
        "(name text PRIMARY KEY, sha256 text NOT NULL, applied_at timestamptz NOT NULL DEFAULT now());", db)
    files = sorted((ROOT / "database" / "migrations").glob("*.sql"))
    if extra is not None:
        files.append(extra)
    for file in files:
        digest = migration_digest(file)
        if not file.name.replace("_", "").replace(".", "").isalnum():
            raise ValueError("Unsafe migration filename")
        existing = sql(f"SELECT sha256 FROM dpt_ops.schema_migrations WHERE name='{file.name}';", db).stdout.strip()
        if existing:
            if existing != digest:
                raise RuntimeError("Applied migration checksum mismatch: " + file.name)
            continue
        script = "BEGIN;\nSELECT pg_advisory_xact_lock(1900101);\n" + file.read_text(encoding="utf-8")
        script += f"\nINSERT INTO dpt_ops.schema_migrations(name,sha256) VALUES ('{file.name}','{digest}');\nCOMMIT;\n"
        sql(script, db)
        print("Applied " + file.name + " to " + db)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["start", "migrate", "status", "stop"])
    parser.add_argument("--database", choices=sorted(DATABASES), default="dpt_foundation")
    args = parser.parse_args()
    if args.action == "start":
        start()
    elif args.action == "migrate":
        migrate(args.database)
    elif args.action == "stop":
        guard(); docker("stop", CONTAINER); print("Stopped task container; retained disposable volume")
    else:
        guard(); print(sql("SELECT version();", "postgres").stdout.strip())


if __name__ == "__main__":
    main()
