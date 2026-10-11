from pathlib import Path
import json,hashlib,shutil
R=Path('/Users/rlduq19938319/Downloads/codyssey/codyssey/A3-2')
p=json.loads((R/'reports/manual-review/proposals.json').read_text())
changes=[]
def fix(eid,truth,start,end,value,reason):
 changes.append(dict(event_id=eid,truth_id=truth,start=start,end=end,track_id=value,reason=reason))
fix('single-10',3,281,282,None,'Cyan box lies on floor, not target.')
fix('cross-01',63,100,112,None,'Cyan head box belongs to G65.')
fix('cross-01',65,100,112,19,'Cyan head box follows G65, not G63.')
fix('cross-02',71,103,115,None,'Cyan hat box belongs to G70, not G71.')
for eid in ['cross-03','cross-05']:fix(eid,89,108,115,None,'Cyan arm/shoe boxes belong to foreground white-shirt person, not blonde G89.')
fix('cross-08',89,131,141,None,'Cyan boxes follow G2 or third person, not blonde G89.')
fix('cross-08',89,145,145,None,'Cyan shoulder box belongs to G2.')
for f in [145,148]:fix('cross-09',60,f,f,None,'Cyan hat box belongs to G70, not standing G60.')
fix('cross-10',71,163,164,None,'Merged leg box cannot be assigned unambiguously to G71; conservative miss.')
fix('pause-02',4,406,421,None,'Cyan box is to right of stationary G4; nearest-center proposal is incorrect.')
fix('pause-05',62,194,194,None,'Cyan box above/right belongs to another person, not G62.')
notes={
'single-01':'Head-only detection; 9 consecutive misses, below failure threshold.',
'single-02':'Stable partial body/shoe detection.',
'single-03':'Stable ID but occasionally merged with companion.',
'single-04':'Transient ID changes last at most 4 frames; no sustained switch.',
'single-05':'Isolated walking target with stable ID.',
'single-06':'Merged foreground box changes from T68 to T79 for 7 frames.',
'single-07':'T104 changes to T105 for 5 frames.',
'single-08':'Partial shoe detection T62 persists 7 frames; companion nearby.',
'single-09':'Stable merged box includes companion; not a clean isolated scene.',
'single-10':'Floor false associations removed; scattered partial detections interrupt miss runs.',
'cross-01':'Overlapping dark-clothed people; corrected head association. G63 excluded when visibility <=0.5.',
'cross-02':'Hat detections were assigned to wrong person; corrected.',
'cross-03':'Foreground white-shirt target changes ID for 5 frames; blonde target missed.',
'cross-04':'Both visible overlapping targets are missed for 16 frames.',
'cross-05':'Crowd overlap; third-person boxes cannot count as target detections.',
'cross-06':'White foreground target changes T33 to T29 for 6 frames; rear dark target missed.',
'cross-07':'Rear shoulders detected; foreground jersey target missed.',
'cross-08':'Blonde head detected only at 142–144; blue-suit ID changes for 6 frames.',
'cross-09':'Standing rear target missed; hat/shoe boxes belong to foreground walker.',
'cross-10':'Rear target missed; ambiguous merged legs treated conservatively.',
'pause-01':'Stationary phone user absorbed into background; wrist detected at final frame.',
'pause-02':'Stationary gray jacket next to scooter; off-target detections removed.',
'pause-03':'Stationary body but hand motion creates intermittent partial detections.',
'pause-04':'Stationary body with hand gestures; tiny hand/upper-body detection remains.',
'pause-05':'Standing target behind lamp; unrelated bright-area detection removed.',
'light-01':'Digital gain changes 1.0 to 0.6; visible target missed for 11 frames.',
'light-02':'Digital gain changes 0.6 to 1.3; visible target missed for 11 frames.',
'light-03':'Digital gain changes 1.3 to 0.65; 8-frame miss followed by 3-frame new ID, below thresholds.',
'light-04':'Digital gain changes 0.65 to 1.25; T180 changes to T298 for 11 frames.',
'light-05':'Digital gain changes 1.25 to 0.7; T408 appears intermittently for at most 3 consecutive frames.'}
summary={}
for e in p['events']:
 # Context frame can duplicate first count frame in proposal; count each source frame once.
 frames={v['frame']:v for v in e['frame_assignments']}; e['frame_assignments']=[frames[f] for f in range(e['start'],e['end']+1)]
 for c in changes:
  if c['event_id']==e['event_id']:
   for v in e['frame_assignments']:
    if c['start']<=v['frame']<=c['end']:
     for ob in v['objects']:
      if ob['truth_id']==c['truth_id']:ob['track_id']=c['track_id']
 counts=dict(id_switches=0,failure_events=0,missed_object_frames=0,eligible_object_frames=0,excluded_object_frames=0)
 for truth in e['ids']:
  current=None;candidate=None;hold=0;miss=0
  for v in e['frame_assignments']:
   ob=next(o for o in v['objects'] if o['truth_id']==truth)
   if ob['visibility']<=.5:
    counts['excluded_object_frames']+=1;miss=0;candidate=None;hold=0;continue
   counts['eligible_object_frames']+=1;t=ob['track_id']
   if t is None:
    counts['missed_object_frames']+=1;miss+=1;candidate=None;hold=0
    if miss==10:counts['failure_events']+=1
    continue
   miss=0
   if current is None:current=t
   if t==current:candidate=None;hold=0
   else:
    if candidate==t:hold+=1
    else:candidate=t;hold=1
    if hold==5:counts['id_switches']+=1;current=t;candidate=None;hold=0
 e['counts']=counts;e['visual_observation']=notes[e['event_id']];e['review_image_sha256']=hashlib.sha256((R/e['review_image']).read_bytes()).hexdigest()
 s=summary.setdefault(e['condition'],dict(events=0,**{k:0 for k in counts}));s['events']+=1
 for k,v in counts.items():s[k]+=v
for s in summary.values():s['missed_object_frame_rate']=s['missed_object_frames']/s['eligible_object_frames']
p.update(proposals_only=False,reviewer='Codex frame-by-frame visual review of 30 contact sheets, assisted by automatic proposals; not a human learner self-measurement',corrections=changes,summary=summary,scope='30 selected 16-frame event windows within two 20-second streams; not 30 independent clips or a whole-clip manual census. Single means one reviewed target in a crowded scene. Lighting is digital gain stress on real footage, not physical lamp variation.',counting='One source frame counted once. New ID >=5 consecutive eligible frames; visible misses >=10 consecutive frames; visibility <=0.5 excluded; initial ID established within each event window.')
(R/'reports/manual-review/reviewed.json').write_text(json.dumps(p,indent=2)+'\n')
lines=['# 실제 영상 프레임별 시각 검토','',p['scope'],'',p['reviewer'],'',p['counting'],'','원본: MOT17-04-FRCNN 1–600프레임, 30 FPS, 20초. 조명 조건: 같은 영상에 명시된 gain_schedule을 적용. 빨강은 GT, 청록은 자동 검출 후보. 잘못된 사람/바닥 매칭은 reviewed.json의 corrections에 수정 이유와 프레임을 기록했다. 자동 전 구간 결과와 이 선택 구간 결과는 서로 다른 측정이다.','', '|조건|사건 수|ID switch|실패 사건|누락/유효 객체 프레임|누락률|','|---|---:|---:|---:|---:|---:|']
for k,s in summary.items():lines.append(f"|{k}|{s['events']}|{s['id_switches']}|{s['failure_events']}|{s['missed_object_frames']}/{s['eligible_object_frames']}|{s['missed_object_frame_rate']:.2%}|")
lines+=['','## 사건별 기록','','|사건|대상 GT ID|프레임|switch|실패|비고|','|---|---|---|---:|---:|---|']
for e in p['events']:lines.append(f"|[{e['event_id']}]({e['event_id']}.jpg)|{e['ids']}|{e['start']}–{e['end']}|{e['counts']['id_switches']}|{e['counts']['failure_events']}|{e['visual_observation']}|")
lines+=['','## 재현','','`python scripts/fetch_real_video.py --sequence 04` 후 `python scripts/prepare_manual_review.py`를 실행해 후보와 이미지들을 생성한다. `python scripts/count_reviewed_events.py`는 버전 관리된 reviewed.json의 수정 이력을 후보에 적용해 계수를 재계산·비교한다. 시각 판단은 별도 검토자가 이미지와 corrections를 검토해야 하며, 재실행이 사람의 판단을 자동 증명하지 않는다.','']
(R/'reports/manual-review/README.md').write_text('\n'.join(lines))
src=Path('/private/tmp/prepare_manual_review.py').read_text().replace("R=Path('/Users/rlduq19938319/Downloads/codyssey/codyssey/A3-2')","R=Path(__file__).resolve().parents[1]")
(R/'scripts/prepare_manual_review.py').write_text(src)
print(json.dumps(summary,indent=2))
