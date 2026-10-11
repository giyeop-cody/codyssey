"""Record the ten-mission review from executable evidence before publication."""
from pathlib import Path
import datetime
import json

ROOT=Path(__file__).resolve().parents[1]

def read(path):return json.loads(path.read_text(encoding='utf-8'))
def write(path,value):path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def main():
    tests=read(ROOT/'reports/current-verification/tests.json')
    gates=read(ROOT/'reports/current-verification/mission-gates.json')
    inputs=read(ROOT/'reports/current-verification/inputs.json')
    assert len(tests['records'])==10
    assert all(r['exit_code']==0 for r in tests['records']+gates['records']+inputs['records'])
    assert sum(r['counts'].get('passed',0) for r in tests['records'])==336
    assert sum(r['counts'].get('xfailed',0) for r in tests['records'])==1
    assert sum(r['inputs'] for r in inputs['records'])==1213
    reviewed=[]
    for record in tests['records']:
        mission=record['mission']
        evidence=[r for r in gates['records'] if r['mission']==mission]
        assert evidence,mission
        limits=[]
        if mission=='A3-1':
            limits.append(dict(type='historical_optional_model_limit',
                issue='v3 para-perspective experiment retains one expected failure; primary four-point scanner and separate v4 frontalization tests pass.',
                resolution='Preserve v3 regression and archived code hashes. The existing v4 route addresses rectification when line-segment evidence is available; do not promise v3 recovery without new geometric evidence.',
                evidence=['tests/test_frontal.py','tests/test_dewarp2.py','scripts/check_requirements.py']))
        if mission=='A3-2':
            limits.append(dict(type='observation_scope',
                issue='30 selected events were visually reviewed by Codex, using crowd targets and digital gain. Personal learner experience is not attested.',
                resolution='Retain reviewer, frame traces, image hashes and acquisition labels. Physical lamps, isolated scenes and explicit resumption are not extra mandatory clauses. Supplement learner personal observation when submitting personal-experience assessment.',
                evidence=['reports/manual-review/reviewed.json','reports/manual-review/protocol-audit.json','reports/manual-review/pause-context-review.json']))
        review=dict(date='2026-10-12',artifact_review_passed=True,blocking_issues=[],
                    documented_limits=limits,test_counts=record['counts'],gate_commands=evidence,
                    scope='Implementation, retained artifact integrity and original-question coverage; not a personal-ability certification or a new full training run.')
        p=ROOT/mission/'reports/independent-reverification.json'
        doc=read(p)
        doc['current_platform_tests']={**record,'date':'2026-10-12','platform':tests['platform'],'scope':tests['scope']}
        doc['publication_review']=review
        write(p,doc)
        p=ROOT/f'{mission}-studylog/docs/evaluation-mapping.json'
        mapping=read(p)
        mapping['current_platform_verification']=doc['current_platform_tests']
        mapping['publication_review']=review
        write(p,mapping)
        text=(f'# 2026-10-12 전체 과제 재검증\n\n{record["summary"][-1]}\n\n'
              '원문 문항/답변 연결, 미션별 요구사항·산출물 검사와 전체 테스트를 재실행했다. '
              '통합 결과는 336 passed / 0 skipped / 역사적 선택 v3 xfail 1건, '
              '원문187문항·10쌍 SHA 및 원본 입력1213개 해시 통과다. '\
              '다운로더 경계 검사4개도 통과했다.\n\n'
              '공개 대상 구현·산출물 검증에서 차단 오류는 발견되지 않았다. '
              '대규모 학습과 Mac GUI 결과는 기존 실행 증거로 구분하고 학습자 자신의 경험·설명 능력을 인증하지 않는다.\n\n'
              '## 실행한 검사\n\n'+''.join(f'- `{r["command"]}`: exit0\n' for r in evidence)+'\n')
        for limit in limits:text+=limit['issue']+'\n\n'+limit['resolution']+'\n\n'
        if mission=='A4-1':text+='20NG3618문서·NSMC4000문서에서 각각10개 독립 TF-IDF/cosine 비교를 새 실행해 통과했다. 공식 20NG 원본 SHA는 sklearn 고정값과 일치한다.\n'
        for folder in [mission,f'{mission}-studylog']:
            (ROOT/folder/'docs/15-current-platform-verification.md').write_text(text.rstrip()+'\n',encoding='utf-8')
        reviewed.append(dict(mission=mission,**review))
    hub=ROOT/'codyssey-A-studylog-hub'
    p=hub/'docs/independent-reverification.json'
    audit=read(p)
    for record in audit['records']:
        current=read(ROOT/record['mission']/'reports/independent-reverification.json')
        record['current_platform_tests']=current['current_platform_tests']
        record['publication_review']=current['publication_review']
    audit['publication_review']=dict(date='2026-10-12',all_ten_artifact_reviews_passed=True,
                                   blocking_issues=[],documented_limits=[l for r in reviewed for l in r['documented_limits']],
                                   decision='Commit and push reviewed changes; retain bounded claims and historical experiment limitations.')
    audit['commit_push']='Publication authorized after all ten reviews; child repositories precede hub and root.'
    write(p,audit)
    final=dict(timestamp_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),missions=reviewed,
               passed=336,skipped=0,xfailed=1,external_input_hashes=1213,question_count=187,
               blocking_issues=[],publication_decision='ready',
               source='Executable tests and requirement gates; manual interpretation is recorded in each publication_review.')
    write(ROOT/'reports/current-verification/publication-review.json',final)
    rows='\n'.join(f'| {r["mission"]} | {r["test_counts"]["passed"]} | {len(r["gate_commands"])}개 명령 exit0 |' for r in reviewed)
    text=('''# 2026-10-12 전체 과제 재검증 및 공개 판단

10개 과제 전체의 테스트, 요구사항·산출물 검사, 원문187문항 연결을 재검증했다.
336 passed / 0 skipped / 1 xfailed. 원본 입력1213개 SHA 및 다운로더 경계4개 검사 통과.

| 과제 | 테스트 통과 | 요구사항·산출물 검사 |
|---|---:|---|
'''+rows+'''

실제 수정: Windows OCR 파일명/글꼴 경로, 영상 테스트 입력 생성, A5-2 원문 CSV 복원,
A6-2 class index long 형식, A2-1 학습률 원문 해석, A3-2 사건 설명과 worksheet,
누락된 재현 검증기, 20NG 동일 SHA 공식 원본 복원, LF/역사 CSV 바이트 보존.
원문 taskmap/evalmap은 변경하지 않았다.

재검토에서 README의 재귀 clone/update 명령도 발견해 수정했다.
`tools/init_direct_submodules.py`는 직계21개만 초기화하며 허브 내부나 taskmap 역참조로
내려가지 않는다. 갱신은 고정 gitlink를 유지하고 자동 --remote 갱신을 하지 않는다.

기존 공개 보류 판단 정정: v3 xfail은 기본 scanner 밖의 추가 원통 실험이며,
이미 존재하는 v4 정면화 경로의 양성/무해/곡면 거부 테스트가 통과한다.
따라서 역사적 v3 한계를 기본 기능의 미해결 오류로 분류하지 않는다.
A3-2는 검토자·군중 대상·digital gain·선택 사건 구간을 그대로 명시한다.
원문에 없는 물리 조명, 고립 장면, 별도 재이동을 추가 필수 조건으로 부과하지 않는다.
학습자 개인의 경험·설명 능력은 모든 과제에서 별도 평가 범위다.

공개 대상 구현·산출물 검증에서 차단 오류를 발견하지 않았다.
미션10개 → 스터디로그10개 → 허브의 명시적 gitlink → 통합 저장소 순서로
커밋·푸시하며 force push나 재귀 초기화를 사용하지 않는다.
학습 및 Mac GUI의 기존 실행과 이번 Windows 실행을 구분해 보존한다.

재현: `python tools/run_verification_tests.py`, `python tools/run_mission_gates.py`,
`python tools/verify_submission.py`, `python tools/verify_input_caches.py`,
`python -m pytest -q tools/test_input_downloaders.py`.
''')
    (ROOT/'docs/all-missions-review-2026-10-12.md').write_text(text,encoding='utf-8')
    (hub/'docs/16-all-missions-review.md').write_text(text,encoding='utf-8')
    print('All ten artifact reviews passed; documented limits preserved; publication ready.')

if __name__=='__main__':
    main()
