"""Persist offline checks of all recorded, pinned external input caches."""
from pathlib import Path
import datetime
import json
import subprocess
import sys
ROOT = Path(__file__).resolve().parents[1]

def main():
    records = []
    for mission in ['A3-1', 'A3-2', 'A4-1', 'A6-2']:
        manifest = json.loads((ROOT / mission / 'reports/verification-inputs.json').read_text(encoding='utf-8'))
        result = subprocess.run([sys.executable, '-X', 'utf8', str(ROOT / mission / 'scripts/fetch_verification_inputs.py'), '--check'], capture_output=True, encoding='utf-8')
        record = dict(mission=mission, inputs=len(manifest['files']), exit_code=result.returncode,
                      output=result.stdout.strip(), error=result.stderr.strip())
        print(json.dumps(record, ensure_ascii=False), flush=True)
        records.append(record)
    out = ROOT / 'reports/current-verification'
    out.mkdir(parents=True, exist_ok=True)
    (out / 'inputs.json').write_text(json.dumps(dict(timestamp_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(), records=records), ensure_ascii=False, indent=2), encoding='utf-8')
    return int(any(r['exit_code'] for r in records))

if __name__ == '__main__':
    raise SystemExit(main())
