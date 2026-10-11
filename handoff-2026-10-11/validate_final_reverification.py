from pathlib import Path
import json,re,hashlib,subprocess
R=Path('/Users/rlduq19938319/Downloads/codyssey');root=R/'codyssey';hub=root/'codyssey-A-studylog-hub'
a=json.loads((hub/'docs/independent-reverification.json').read_text());total=0
for rec in a['records']:
 m=rec['mission'];mission=root/m;log=root/(m+'-studylog');d=json.loads((log/'docs/evaluation-mapping.json').read_text())
 raw=(R/'codyssey-evalmap'/m/(m.lower()+'-eval.md')).read_bytes()
 assert re.findall(r'^\*\s+(.*)$',raw.decode(),re.M)==[q['question'] for q in d['items']]
 assert hashlib.sha256(raw).hexdigest()==rec['source']['evaluation_sha256']
 assert rec['source']['task_sha256']==hashlib.sha256((R/'codyssey-taskmap'/m/(m.lower()+'-description.md')).read_bytes()).hexdigest()
 text=(log/'docs/14-final-reverification.md').read_text()
 for q in d['items']:
  assert q['question'] in text
  assert q.get('reverification',{}).get('answer',q['answer']) in text
 assert rec['tests']['exit_code']==0
 for repo in [mission,log]:subprocess.run(['git','-C',str(repo),'diff','--check'],check=True)
 total+=len(d['items'])
for seq in ['11','04']:
 data=root/'A3-2/data'/('mot17-'+seq);report=json.loads((root/'A3-2/reports'/('real-video-benchmark.json' if seq=='11' else 'real-video-benchmark-04.json')).read_text())
 assert report['duration_seconds']==20 and len(report['source_frame_sha256'])==600
 assert report['source_gt_sha256']==hashlib.sha256((data/'gt/gt.txt').read_bytes()).hexdigest()
 assert report['video_sha256']==hashlib.sha256((data/'real-20s.mp4').read_bytes()).hexdigest()
 for i,sha in enumerate(report['source_frame_sha256'],1):assert sha==hashlib.sha256((data/f'img1/{i:06}.jpg').read_bytes()).hexdigest()
 assert report['manual_protocol_complete'] is False
for m in ['A3-1','A3-2']:
 gui=json.loads((root/m/'reports/gui-native-verification.json').read_text());assert gui['backend']=='COCOA'
 assert all(r['rects']['Edges'][2]>0 for r in gui['observations']) if m=='A3-1' else gui['output_fps']==30 and gui['snapshot_saved']
pca=json.loads((root/'A5-2/reports/pca-policy-audit.json').read_text());assert pca['robust_k2']['silhouette_2d_sample']>pca['standard_k4']['silhouette_2d_sample']
assert pca['protocol']['csv_sha256']==hashlib.sha256((root/'A5-2/data/finance_data.csv').read_bytes()).hexdigest()
ks=json.loads((root/'A5-2/reports/k_selection.json').read_text());assert ks['choice']['chosen_k']==max(ks['rows'],key=lambda r:r['silhouette'])['k']==2
assert total==187 and a['passed_tests']==334 and a['skipped_tests']==0 and a['expected_failures']==1
for repo in [root,hub]:subprocess.run(['git','-C',str(repo),'diff','--check'],check=True)
print('PASS: 187 exact questions/answers; 10 original source hash pairs; 334 passed tests/0 skips/1 recorded optional xfail; 1200 public real-video frames/GT/video SHA; native GUI; target-excluded unchanged CSV/PCA/K policy; all 22 diff checks.')
print('No commit or push; remaining requirement conflict/manual protocol/optional v3 failure explicitly recorded.')
