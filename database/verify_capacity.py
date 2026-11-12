"""Run local regression and publish separate sanitized IMP-P1-04 evidence."""
import datetime
import hashlib
import io
import json
from pathlib import Path
import sys
import time
import unittest

import local
import verify
from etl_benchmark import RunLease, common_repository_root


class CountedResult(unittest.TextTestResult):
    """Fixture/setup errors are outcomes, not failed test-method executions."""
    passed_methods=0

    def addSuccess(self,test):
        self.passed_methods+=1
        super().addSuccess(test)


def run_suite():
    started=time.monotonic()
    suite=unittest.TestLoader().discover(str(local.ROOT/'database/tests'))
    names=[]
    def collect(test):
        if isinstance(test,unittest.TestSuite):
            for item in test:collect(item)
        else:names.append(test.id())
    collect(suite)
    stream=io.StringIO()
    result=unittest.TextTestRunner(stream=stream,verbosity=2,resultclass=CountedResult).run(suite)
    state=local.ROOT/'.local/p1-04';state.mkdir(parents=True,exist_ok=True)
    (state/'full_regression.log').write_text(stream.getvalue(),encoding='utf-8')
    report={'task':'IMP-P1-04','checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
       'command':'python database/verify_capacity.py','python_version':sys.version,
       'environment':'Guarded disposable local Docker Desktop PostgreSQL16.15; no pilot reset',
       'image':local.IMAGE,'tests_run':result.testsRun,
       'passed':result.passed_methods,
       'failed':len(result.failures),'errors':len(result.errors),'skipped':len(result.skipped),
       'seconds':round(time.monotonic()-started,6),'exit_code':0 if result.wasSuccessful() else 1,
       'test_ids':names,'error_ids':[test.id() for test,_ in result.errors],
       'counting':'tests_run counts methods; errors may include class setup/teardown outcomes; passed counts addSuccess callbacks',
       'source_file_sha256':{p.relative_to(local.ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest()
         for p in sorted((local.ROOT/'database').rglob('*')) if p.is_file() and p.suffix in {'.py','.sql'}},
       'separate_execution_evidence':['Controlled benchmark attempts, including failures, are reported separately',
          'Independent DB restore and synthetic object rehearsal have separate actual execution reports'],
       'not_run':['Actual image/asset lineage/provider recovery','Cloud/offsite/encrypted recovery/RPO/retention',
          'Application/API/UI/matching','Passing full1479 replay benchmark:23514 remains a recorded blocker']}
    output=local.ROOT/'database/evidence'
    if result.wasSuccessful():
        (output/'capacity_test_results.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
        (output/'capacity_schema_inventory.json').write_text(json.dumps(verify.inventory(),indent=2)+'\n',encoding='utf-8')
    else:
        (state/'failed_regression_result.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
        print(stream.getvalue())
    print(json.dumps({k:report[k] for k in ['tests_run','passed','failed','errors','skipped','seconds','exit_code']}))
    return report['exit_code']


def main():
    # Coordinate with the destructive disposable benchmark reset and recovery driver.
    # The lease is not an exclusion mechanism for arbitrary external SQL clients.
    with RunLease(common_repository_root()):return run_suite()


if __name__=='__main__':sys.exit(main())
