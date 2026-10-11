"""Check source hashes, exact rubric/answer links and archived visual-review traces.

This verifies retained evidence, not completion of all requirements or past tests.
Large external caches are checked separately by each input downloader --check.
"""
from pathlib import Path
import hashlib
import csv
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    hub = ROOT / 'codyssey-A-studylog-hub'
    audit = json.loads((hub / 'docs/independent-reverification.json').read_text(encoding='utf-8'))
    total = 0
    for record in audit['records']:
        mission = record['mission']
        log = ROOT / (mission + '-studylog')
        mapping = json.loads((log / 'docs/evaluation-mapping.json').read_text(encoding='utf-8'))
        rubric = ROOT.parent / 'codyssey-evalmap' / mission / (mission.lower() + '-eval.md')
        task = ROOT.parent / 'codyssey-taskmap' / mission / (mission.lower() + '-description.md')
        assert re.findall(r'^\*\s+(.*)$', rubric.read_text(encoding='utf-8'), re.M) == [q['question'] for q in mapping['items']], mission
        assert digest(rubric) == record['source']['evaluation_sha256'], mission
        assert digest(task) == record['source']['task_sha256'], mission
        text = (log / 'docs/14-final-reverification.md').read_text(encoding='utf-8')
        for item in mapping['items']:
            assert item['question'] in text, (mission, item['question'])
            assert item.get('reverification', {}).get('answer', item['answer']) in text, mission
        total += len(mapping['items'])
    assert total == 187, total
    subprocess.run([sys.executable, str(ROOT / 'A3-2/scripts/count_reviewed_events.py')], check=True)
    reviewed = json.loads((ROOT / 'A3-2/reports/manual-review/reviewed.json').read_text(encoding='utf-8'))
    with (ROOT / 'A3-2/reports/manual-event-worksheet.csv').open(encoding='utf-8', newline='') as f:
        worksheet = list(csv.DictReader(f))
    assert len(worksheet) == 30
    assert {row['trial_id'] for row in worksheet} == {event['event_id'] for event in reviewed['events']}
    for row in worksheet:
        event = next(e for e in reviewed['events'] if e['event_id'] == row['trial_id'])
        assert row['status'] == 'codex_reviewed_selected_event'
        assert int(row['id_switch_count']) == event['counts']['id_switches']
        assert int(row['tracking_failure_count']) == event['counts']['failure_events']
    assert digest(ROOT / 'A6-2/fixtures/aapl_daily.csv') == '65617e7a9800a8e76b1f03e5d6df802189be9704e40fdd13e13f3e9d460c2973'
    print('PASS: 187 exact question/answer links, 10 source hash pairs, retained visual-review traces and frozen AAPL input.')
    print('Scope: structural and archived-evidence checks; current tests, external caches and unmet protocol conditions remain separate.')

if __name__ == '__main__':
    main()
