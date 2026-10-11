"""Initialize only the 21 direct Advanced repositories; never descend into hubs."""
from pathlib import Path
import argparse
import subprocess

ROOT=Path(__file__).resolve().parents[1]
MISSIONS=['A1-1','A2-1','A3-1','A3-2','A4-1','A4-2','A5-1','A5-2','A6-1','A6-2']
PATHS=MISSIONS+[m+'-studylog' for m in MISSIONS]+['codyssey-A-studylog-hub']

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--list',action='store_true',help='Print the bounded initialization paths without changing files.')
    args=parser.parse_args()
    if args.list:
        print('\n'.join(PATHS))
        return
    subprocess.run(['git','-c','submodule.recurse=false','-c','fetch.recurseSubmodules=false',
                    '-C',str(ROOT),'submodule','update','--init','--',*PATHS],check=True)

if __name__=='__main__':
    main()
