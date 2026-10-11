"""Run all ten missions' requirement/artifact gates, separately from pytest."""
from pathlib import Path
import datetime
import json
import os
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
COMMANDS={
    'A1-1':['scripts/check_requirements.py'],
    'A2-1':['scripts/check_requirements.py','scripts/verify_lr_boundary.py'],
    'A3-1':['scripts/check_requirements.py'],
    'A3-2':['scripts/count_reviewed_events.py','scripts/audit_review_protocol.py'],
    'A4-1':['scripts/check_requirements.py','scripts/cross_check_readme.py','scripts/verify_external_corpus.py'],
    'A4-2':['scripts/check_requirements.py'],
    'A5-1':['scripts/check_mission.py','scripts/cross_check_readme.py'],
    'A5-2':['scripts/check_mission.py','scripts/cross_check_readme.py'],
    'A6-1':['scripts/check_mission.py'],
    'A6-2':['-m pytest -q tests/test_gates.py tests/test_leakcheck.py tests/test_frozen_input.py'],
}

def main():
    out=ROOT/'reports/current-verification'
    out.mkdir(parents=True,exist_ok=True)
    env=dict(os.environ,PYTHONUTF8='1',PYTHONIOENCODING='utf-8',MISSION_STRICT='1',
             TASKMAP_DIR=str(ROOT.parent/'codyssey-taskmap'),
             MPLCONFIGDIR=str(out/'mpl'),NUMBA_CACHE_DIR=str(out/'numba'),LOKY_MAX_CPU_COUNT='2')
    records=[]
    for mission,commands in COMMANDS.items():
        for command in commands:
            args=command.split() if command.startswith('-m ') else [command]
            proc=subprocess.run([sys.executable,'-X','utf8',*args],cwd=ROOT/mission,
                                env=env,capture_output=True,encoding='utf-8',errors='replace')
            path=out/f'{mission}-{Path(args[-1]).stem}-gate.log'
            captured=proc.stdout+proc.stderr
            # Remove console alignment padding from the saved text, keeping every value.
            path.write_text('\n'.join(line.rstrip() for line in captured.splitlines()).rstrip()+'\n',encoding='utf-8')
            record=dict(mission=mission,command=command,exit_code=proc.returncode,
                        log=str(path.relative_to(ROOT)),summary=(proc.stdout+proc.stderr).splitlines()[-6:])
            records.append(record)
            print(json.dumps(record,ensure_ascii=False),flush=True)
    (out/'mission-gates.json').write_text(json.dumps(dict(
        timestamp_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),records=records,
        scope='Current requirement/artifact gates. Historical experiments remain explicitly labelled.',
        log_format='Console alignment trailing spaces and blank EOF lines are trimmed; reported values are unchanged.'),
        ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return int(any(r['exit_code'] for r in records))

if __name__=='__main__':
    raise SystemExit(main())
