from pathlib import Path
import subprocess,json,concurrent.futures,os
R=Path('/Users/rlduq19938319/Downloads/codyssey/codyssey');py=str(R.parent/'.venv312/bin/python')
J=[('A1-1',['-m','pytest','-q']),('A2-1',['-m','pytest','-q']),('A3-1',['-m','pytest','-q']),('A3-2',['-m','pytest','-q']),('A4-1',['-m','pytest','-q']),('A4-2',['-m','pytest','-q']),('A5-1',['-m','pytest','-q']),('A5-2',['-m','pytest','-q']),('A6-1',['-m','pytest','-q']),('A6-2',['-m','pytest','-q'])]
env=dict(os.environ,PATH='/Users/rlduq19938319/Downloads/codyssey/.ocr-env/bin:'+os.environ['PATH'],TESSDATA_PREFIX='/Users/rlduq19938319/Downloads/codyssey/.ocr-env/share/tessdata',MPLCONFIGDIR='/private/tmp/codyssey-mpl',NUMBA_CACHE_DIR='/private/tmp/codyssey-numba',LOKY_MAX_CPU_COUNT='2',MISSION_STRICT='1',TASKMAP_DIR='/Users/rlduq19938319/Downloads/codyssey/codyssey-taskmap')
def run(j):
 m,args=j;p=Path('/private/tmp')/(m+'-independent-audit.log')
 with p.open('w') as f:r=subprocess.run([py,*args],cwd=R/m,env=env,stdout=f,stderr=subprocess.STDOUT)
 tail=p.read_text().splitlines()[-4:]
 return dict(mission=m,command='python '+' '.join(args),exit_code=r.returncode,summary=tail)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:rows=list(ex.map(run,J))
Path('/private/tmp/independent-audit-validation.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2));print(json.dumps(rows,ensure_ascii=False,indent=2))
