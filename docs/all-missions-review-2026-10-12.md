# 2026-10-12 전체 과제 재검증 및 공개 판단

10개 과제 전체의 테스트, 요구사항·산출물 검사, 원문187문항 연결을 재검증했다.
336 passed / 0 skipped / 1 xfailed. 원본 입력1213개 SHA 및 다운로더 경계4개 검사 통과.

| 과제 | 테스트 통과 | 요구사항·산출물 검사 |
|---|---:|---|
| A1-1 | 16 | 1개 명령 exit0 |
| A2-1 | 23 | 2개 명령 exit0 |
| A3-1 | 49 | 1개 명령 exit0 |
| A3-2 | 26 | 2개 명령 exit0 |
| A4-1 | 25 | 3개 명령 exit0 |
| A4-2 | 109 | 1개 명령 exit0 |
| A5-1 | 18 | 2개 명령 exit0 |
| A5-2 | 28 | 2개 명령 exit0 |
| A6-1 | 25 | 1개 명령 exit0 |
| A6-2 | 17 | 1개 명령 exit0 |

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
