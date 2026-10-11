"""Run each mission in its own import context; preserve current-platform evidence."""
from pathlib import Path
import argparse
import datetime
import json
import os
import platform
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
MISSIONS = ['A1-1', 'A2-1', 'A3-1', 'A3-2', 'A4-1', 'A4-2', 'A5-1', 'A5-2', 'A6-1', 'A6-2']

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('missions', nargs='*', choices=MISSIONS)
    args = parser.parse_args()
    out = ROOT / 'reports' / 'current-verification'
    out.mkdir(parents=True, exist_ok=True)
    taskmap = ROOT.parent / 'codyssey-taskmap'
    env = dict(os.environ, MISSION_STRICT='1', TASKMAP_DIR=str(taskmap),
               MPLCONFIGDIR=str(out / 'mpl'), NUMBA_CACHE_DIR=str(out / 'numba'),
               LOKY_MAX_CPU_COUNT='2', PYTHONIOENCODING='utf-8', PYTHONUTF8='1')
    ocr = ROOT.parent / '.ocr-env'
    if (ocr / 'Library/bin/tesseract.exe').exists():
        env['TESSERACT_DIR'] = str(ocr / 'Library/bin')
        env['TESSDATA_PREFIX'] = str(ocr / 'share/tessdata')
    records = []
    for mission in args.missions or MISSIONS:
        result = subprocess.run([sys.executable, '-m', 'pytest', '-q'],
                                cwd=ROOT / mission, env=env, capture_output=True,
                                encoding='utf-8', errors='replace')
        log = result.stdout + result.stderr
        (out / f'{mission}.log').write_text(log, encoding='utf-8')
        record = dict(mission=mission, exit_code=result.returncode,
                      summary=log.splitlines()[-8:],
                      counts={key: int(value) for value, key in
                              re.findall(r'(\d+) (passed|failed|skipped|xfailed|xpassed|errors?)',
                                         log.splitlines()[-1] if log.splitlines() else '')})
        records.append(record)
        print(json.dumps(record, ensure_ascii=False), flush=True)
    prior = out / 'tests.json'
    if args.missions and prior.exists():
        old = json.loads(prior.read_text(encoding='utf-8'))['records']
        replaced = {r['mission'] for r in records}
        records = [r for r in old if r['mission'] not in replaced] + records
        records.sort(key=lambda r: MISSIONS.index(r['mission']))
    report = dict(timestamp_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  python=sys.version, platform=platform.platform(), records=records,
                  scope='Current platform pytest only; archived training and GUI evidence is separate.')
    (out / 'tests.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    return int(any(r['exit_code'] for r in records))

if __name__ == '__main__':
    raise SystemExit(main())
