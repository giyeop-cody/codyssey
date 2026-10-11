from pathlib import Path
import sys,json,cv2,numpy as np
R=Path('/Users/rlduq19938319/Downloads/codyssey/codyssey/A3-2');sys.path.insert(0,str(R))
from src.bgsubtract import create_mog2
from src.detector import clean_mask,to_bboxes
from src.tracker import Tracker
D=R/'data/mot17-04';g=np.loadtxt(D/'gt/gt.txt',delimiter=',');g=g[(g[:,0]<=600)&(g[:,6]==1)&(g[:,7]==1)];by={f:g[g[:,0]==f] for f in range(1,601)}
# Automatic proposals only; manual classifications/counts are separate review records.
events=[];seen=set()
for f in range(80,530,20):
 a=by[f];a=a[a[:,8]>.75]
 for row in a:
  i=int(row[1]);c=row[2:4]+row[4:6]*.5
  other=[z for z in a if int(z[1])!=i]
  if i in seen or any(np.linalg.norm((z[2:4]+z[4:6]*.5)-c)<170 for z in other):continue
  t=g[(g[:,1]==i)&(g[:,0]>=f)&(g[:,0]<=f+15)]
  if len(t)!=16 or min(t[:,8])<.6:continue
  if np.linalg.norm((t[-1,2:4]+t[-1,4:6]/2)-(t[0,2:4]+t[0,4:6]/2))<8:continue
  events.append(dict(event_id=f'single-{len(seen)+1:02}',condition='single',ids=[i],start=f,end=f+15,context_frames=[f-20,f,f+35],source='original'));seen.add(i)
  if len(seen)==10:break
 if len(seen)==10:break
seen=set();cross=[]
for f in range(100,520,15):
 a=by[f];a=a[a[:,8]>.5]
 for n,row in enumerate(a):
  for z in a[n+1:]:
   pair=tuple(sorted([int(row[1]),int(z[1])]))
   if pair in seen:continue
   ix=max(0,min(row[2]+row[4],z[2]+z[4])-max(row[2],z[2]));iy=max(0,min(row[3]+row[5],z[3]+z[5])-max(row[3],z[3]));ov=ix*iy/min(row[4]*row[5],z[4]*z[5])
   if .12<ov<.42:
    if any(len(g[(g[:,1]==i)&(g[:,0]>=f)&(g[:,0]<=f+15)])!=16 for i in pair):continue
    cross.append(dict(event_id=f'cross-{len(cross)+1:02}',condition='cross',ids=list(pair),start=f,end=f+15,context_frames=[f-20,f,f+35],source='original',proposal_overlap=float(ov)));seen.add(pair)
    break
  if len(cross)==10:break
 if len(cross)==10:break
events+=cross
pauses=[(1,171),(4,396),(5,296),(60,451),(62,176)]
for n,(i,f) in enumerate(pauses,1):events.append(dict(event_id=f'pause-{n:02}',condition='pause',ids=[i],start=f+10,end=f+25,context_frames=[f,f+39,f+79],source='original'))
# Real, unchanged scene geometry; only pixel gain changes. Not physical lamp changes.
gains={100:.6,200:1.3,300:.65,400:1.25,500:.7}
for n,f in enumerate(gains,1):
 a=by[f];a=a[a[:,8]>.9]
 row=next(z for z in a if len(g[(g[:,1]==z[1])&(g[:,0]>=f-5)&(g[:,0]<=f+10)])==16)
 events.append(dict(event_id=f'light-{n:02}',condition='light',ids=[int(row[1])],start=f-5,end=f+10,context_frames=[f-15,f,f+20],source='gain-stress',gain_change_frame=f,gain=gains[f]))
print('proposals',[(e['event_id'],e['ids'],e['start']) for e in events],flush=True)
(R/'reports/manual-review').mkdir(parents=True,exist_ok=True)
# Two whole 20-second input streams; detector and tracker run once continuously each.
traces={}
for mode in ['original','gain-stress']:
 sub=create_mog2(detect_shadows=False);tracker=Tracker();trace={};gain=1.
 w=None
 if mode!='original':w=cv2.VideoWriter(str(D/'gain-stress-20s.mp4'),cv2.VideoWriter_fourcc(*'mp4v'),30,(960,540))
 for f in range(1,601):
  im=cv2.resize(cv2.imread(str(D/f'img1/{f:06}.jpg')),(960,540))
  if mode!='original':
   gain=gains.get(f,gain);im=np.clip(im.astype(float)*gain,0,255).astype('uint8');w.write(im)
  ts=tracker.update(to_bboxes(clean_mask(sub.apply(im))))
  cur={t.id:t for t in ts if t.missed==0};assign={};used=set()
  rows=by[f];pairs=sorted((float(np.linalg.norm(np.array(t.center)-(z[2:4]+z[4:6]/2)/2)),int(z[1]),i) for z in rows if z[8]>.5 for i,t in cur.items())
  for dist,truth,i in pairs:
   if dist<=50 and truth not in assign and i not in used:assign[truth]=i;used.add(i)
  trace[f]={'assignments':assign,'tracks':{i:list(map(float,t.bbox)) for i,t in cur.items()}}
 if w:w.release()
 traces[mode]=trace
# Frame-by-frame crops plus visible numeric assignments for manual counting.
for e in events:
 fs=list(range(e['start'],e['end']+1));ids=e['ids'];rows=g[np.isin(g[:,1],ids)&(g[:,0]>=min(e['context_frames']))&(g[:,0]<=max(e['context_frames']))]
 x=int(max(0,rows[:,2].min()/2-25));y=int(max(0,rows[:,3].min()/2-25));x2=int(min(960,np.max((rows[:,2]+rows[:,4])/2)+25));y2=int(min(540,np.max((rows[:,3]+rows[:,5])/2)+25))
 width,height=260,240;tiles=[];values=[]
 for f in e['context_frames']+fs:
  im=cv2.resize(cv2.imread(str(D/f'img1/{f:06}.jpg')),(960,540))
  if e['source']=='gain-stress':
   gain=1.
   for at,v in gains.items():
    if at<=f:gain=v
   im=np.clip(im.astype(float)*gain,0,255).astype('uint8')
  desc=[]
  for i in ids:
   z=next(z for z in by[f] if int(z[1])==i);bb=(z[2:4]/2).astype(int);wh=(z[4:6]/2).astype(int)
   cv2.rectangle(im,tuple(bb),tuple(bb+wh),(0,0,255),2)
   tid=traces[e['source']][f]['assignments'].get(i);desc.append(f'G{i}:T{tid if tid else "MISS"} v{z[8]:.2f}')
   if tid:
    b=list(map(int,traces[e['source']][f]['tracks'][tid]));cv2.rectangle(im,(b[0],b[1]),(b[2],b[3]),(255,200,0),2)
  tile=np.zeros((height,width,3),np.uint8);crop=im[y:y2,x:x2];scale=min(width/crop.shape[1],(height-48)/crop.shape[0]);crop=cv2.resize(crop,None,fx=scale,fy=scale);tile[48:48+crop.shape[0],:crop.shape[1]]=crop
  for n,t in enumerate([f"{e['event_id']} f{f} "+('CONTEXT' if f not in fs else 'COUNT')]+desc):cv2.putText(tile,t,(4,13+n*14),cv2.FONT_HERSHEY_SIMPLEX,.38,(255,255,255),1)
  tiles.append(tile)
  if f in fs:values.append(dict(frame=f,objects=[dict(truth_id=i,track_id=traces[e['source']][f]['assignments'].get(i),visibility=float(next(z for z in by[f] if int(z[1])==i)[8])) for i in ids]))
 while len(tiles)%4:tiles.append(np.zeros_like(tiles[0]))
 sheet=np.vstack([np.hstack(tiles[i:i+4]) for i in range(0,len(tiles),4)])
 cv2.imwrite(str(R/f'reports/manual-review/{e["event_id"]}.jpg'),sheet,[cv2.IMWRITE_JPEG_QUALITY,90]);e['frame_assignments']=values;e['review_image']=f'reports/manual-review/{e["event_id"]}.jpg'
(R/'reports/manual-review/proposals.json').write_text(json.dumps({'proposals_only':True,'reviewer':None,'source_sequence':'MOT17-04-FRCNN','fps':30,'input_frames':[1,600],'duration_seconds':20,'gain_schedule':gains,'events':events},indent=2))
