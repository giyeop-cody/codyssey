"""Exercise download integrity boundaries with isolated local source files."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import pytest

ROOT = Path(__file__).resolve().parents[1]

@pytest.mark.parametrize('mission', ['A3-1','A3-2','A4-1','A6-2'])
def test_download_repair_hash_rejection_and_offline_check(tmp_path, mission):
    root = tmp_path / mission
    (root / 'scripts').mkdir(parents=True)
    (root / 'reports').mkdir()
    script = root / 'scripts/fetch_verification_inputs.py'
    script.write_bytes((ROOT / mission / 'scripts/fetch_verification_inputs.py').read_bytes())
    source = tmp_path / 'source.txt'
    source.write_bytes(b'known input\n')
    manifest = root / 'reports/verification-inputs.json'
    item = dict(path='data/input.txt', url=source.as_uri(), sha256=hashlib.sha256(source.read_bytes()).hexdigest())
    manifest.write_text(json.dumps(dict(files=[item])), encoding='utf-8')
    def run(*args):
        return subprocess.run([sys.executable, '-X', 'utf8', str(script), *args], capture_output=True)
    assert run('--check').returncode != 0
    assert run().returncode == 0
    target = root / item['path']
    assert target.read_bytes() == source.read_bytes()
    target.write_bytes(b'corrupt cache')
    assert run('--check').returncode != 0
    assert run().returncode == 0
    assert target.read_bytes() == source.read_bytes()
    source.write_bytes(b'corrupt upstream')
    target.write_bytes(b'existing corrupt cache preserved on failure')
    assert run().returncode != 0
    assert target.read_bytes() == b'existing corrupt cache preserved on failure'
    assert not target.with_name(target.name+'.download').exists()
