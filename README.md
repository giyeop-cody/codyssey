# 🚀 Codyssey All-in-One

> 코디세이(Codyssey) 학습 과정 통합 레포지토리 — **기초(B) · 심화(A) · 응용(M)** 3과정과 미션 정의서를 하나의 트리로 관리한다.  
> 서브모듈 pin·상태 기준일: **2026-09-27** · 연결 대장: [codyssey-taskmap/LINKS.md](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/LINKS.md) 🔒

## 🏗️ 구조

```
codyssey/                             # 올인원 루트 레포 (공개)
├── ai-sw-basic/                      # 1️⃣ 기초(B) 과정 허브 — 공개
│   ├── B1-1/ … B7-2/                 #    15과제 서브모듈 (B2-2 는 팀 레포, B4-1 은 Pages 레포)
│   └── README.md                     #    과정 상태표 (PASS/평가전/진행중/대기)
├── A1-1/ … A6-2/                     # 2️⃣ 심화(A) 제출물 레포 10개 — 비공개
├── A1-1-studylog/ … A6-2-studylog/   #    심화(A) 학습기록 레포 10개 — 비공개
├── codyssey-A-studylog-hub/          #    심화(A) 과정 허브 (학습맵·태스크보드·tools) — 비공개
├── codyssey-taskmap/                 # 📕 미션 정의서 41과제 + LINKS.md 연결 대장 — 비공개
└── (응용 M)                           # 3️⃣ 응용(M) 15과제 — 아직 레포 없음, 정의서만 존재
```

## 📊 3과정 현황

| 과정 | projectNo | 기간 | 과제 | 학습시간 | 허브 레포 | 이 레포 안 위치 | 진행 (자체 검증 기준) |
|---|:--:|---|:--:|:--:|---|---|---|
| **기초(Basic)** AI/SW 기초 | 136003 | 2026-05-07 ~ 2026-10-31 | 15개 | 960h | [ai-sw-basic](https://github.com/giyeop-cody/ai-sw-basic) | `ai-sw-basic/` | PASS 5 · 진행중/평가전/대기 10 |
| **심화(Advanced)** AI/SW 심화 | 136002 | 2026-11-01 ~ 2027-03-31 | 11개 | 800h | [codyssey-A-studylog-hub](https://github.com/giyeop-cody/codyssey-A-studylog-hub) 🔒 | `A*-*/` 20개 + 허브 | 구현 완료 3 (A1-1·A2-1·A3-1) · 스캐폴드 7 · 레포 없음 1 |
| **응용(Master)** AI/SW 응용 | 136001 | 2027-04-01 ~ 2027-09-30 | 15개 | 5280h | 없음 | — | 전 과제 미착수 (정의서만 있음) |
| **총합** | | | **41개** | **7040h** | [codyssey-taskmap](https://github.com/giyeop-cody/codyssey-taskmap) 🔒 | `codyssey-taskmap/` | 기준일 2026-09-27 |

상태 판정 근거와 남은 절차는 [codyssey-taskmap/PROGRESS.md](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/PROGRESS.md) 🔒 에 있다. Codyssey 플랫폼의 공식 평가 결과는 이 레포가 확인할 수 없어 **어떤 과제도 '공식 완료'로 표시하지 않는다**.

---

## 1️⃣ 기초(B) — AI/SW 기초 · 15과제 · 960h

과정 허브 [ai-sw-basic](https://github.com/giyeop-cody/ai-sw-basic) 가 15과제를 서브모듈로 고정한다. `B2-2` 는 팀 레포, `B4-1` 은 GitHub Pages 레포가 제출물이다.

| 코드 | 과제명 | 시간 | 이 레포 안 위치 | 제출물 레포 (미션) | 학습기록 (스터디) | 상태 | 정의서(taskmap) |
|:--:|---|:--:|---|---|---|---|---|
| **B1-1** | 컴퓨터가 알아서 자기 상태를 점검하게 만들기 | 40h | `ai-sw-basic/B1-1/` | [B1-1](https://github.com/giyeop-cody/B1-1) | — | PASS | [원문](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/B1-1/b1-1-description.md) · [연결](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/B1-1/links.md) |
| **B1-2** | 컴퓨터가 갑자기 느려지거나 멈췄을 때 원인 찾아 고치기 | 40h | `ai-sw-basic/B1-2/` | [B1-2](https://github.com/giyeop-cody/B1-2) | — | 구현·자체검증 완료, 외부평가 대기 | [원문](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/B1-2/b1-2-description.md) · [연결](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/B1-2/links.md) |
| **B2-1** | 나만의 용돈 기입장 프로그램 만들기 | 60h | `ai-sw-basic/B2-1/` | [B2-1](https://github.com/giyeop-cody/B2-1) | — | PASS | [원문](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/B2-1/b2-1-description.md) · [연결](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/B2-1/links.md) |
| **B2-2** | 친구 3~5명과 함께 프로그램 만드는 법 연습하기 | 20h | `ai-sw-basic/B2-2/` | [git-flow-utility-lab](https://github.com/codyssey-b2-2-team-mission/git-flow-utility-lab)<br><sub>선행/개인</sub> [B2-2](https://github.com/giyeop-cody/B2-2) | — | PASS (팀 레포가 제출물) | [원문](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/B2-2/b2-2-description.md) · [연결](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/B2-2/links.md) |
| **B3-1** | 정보를 엄청 빠르게 찾아주는 작은 저장소 만들기 | 80h | `ai-sw-basic/B3-1/` | [B3-1](https://github.com/giyeop-cody/B3-1) | — | PASS | [원문](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/B3-1/b3-1-description.md) · [연결](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/B3-1/links.md) |
| **B3-2** | 파일이 언제 어떻게 바뀌었는지 기록하는 작은 프로그램 만들기 | 80h | `ai-sw-basic/B3-2/` | [B3-2](https://github.com/giyeop-cody/B3-2) | — | PASS | [원문](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/B3-2/b3-2-description.md) · [연결](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/B3-2/links.md) |
| **B4-1** | 나를 소개하는 웹페이지 처음부터 만들기 | 80h | `ai-sw-basic/B4-1/` | [giyeop-cody.github.io](https://github.com/giyeop-cody/giyeop-cody.github.io) | — | 진행중 (GitHub Pages 배포됨) | [원문](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/B4-1/b4-1-description.md) · [연결](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/B4-1/links.md) |
| **B4-2** | 버튼 누르면 화면이 스르륵 바뀌는 요즘 웹사이트 만들기 | 80h | `ai-sw-basic/B4-2/` | [B4-2](https://github.com/giyeop-cody/B4-2) | — | 평가전 | [원문](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/B4-2/b4-2-description.md) · [연결](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/B4-2/links.md) |
| **B5-1** | 정보를 깔끔하게 정리하는 디지털 서랍장 만들기 | 40h | `ai-sw-basic/B5-1/` | [B5-1](https://github.com/giyeop-cody/B5-1) | — | 평가전 | [원문](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/B5-1/b5-1-description.md) · [연결](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/B5-1/links.md) |
| **B5-2** | 글을 쓰고·보고·고치고·지울 수 있는 게시판형 웹 서비스 만들기 | 60h | `ai-sw-basic/B5-2/` | [B5-2](https://github.com/giyeop-cody/B5-2) | — | 평가전 | [원문](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/B5-2/b5-2-description.md) · [연결](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/B5-2/links.md) |
| **B5-3** | 로그인이 되고 회원끼리 연결되는 웹 서비스 만들기 | 60h | `ai-sw-basic/B5-3/` | [B5-3](https://github.com/giyeop-cody/B5-3) | — | 진행중 | [원문](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/B5-3/b5-3-description.md) · [연결](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/B5-3/links.md) |
| **B6-1** | 내가 만든 웹사이트를 인터넷에 올려 누구나 쓰게 하기 | 40h | `ai-sw-basic/B6-1/` | [B6-1](https://github.com/giyeop-cody/B6-1) | — | 배포 실증 증거 수집 완료, Issue #1 열림 | [원문](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/B6-1/b6-1-description.md) · [연결](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/B6-1/links.md) |
| **B6-2** | 내가 고친 코드 설명을 AI가 대신 써주는 도우미 만들기 | 40h | `ai-sw-basic/B6-2/` | [B6-2](https://github.com/giyeop-cody/B6-2) | — | 평가전 | [원문](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/B6-2/b6-2-description.md) · [연결](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/B6-2/links.md) |
| **B7-1** | 웹 기반 AI 챗봇 서비스 개발 프로젝트 | 120h | `ai-sw-basic/B7-1/` | [ai-chatbot-service](https://github.com/codyssey-term-mission-B7-1/ai-chatbot-service)<br><sub>개인 fork</sub> [ai-chatbot-service](https://github.com/giyeop-cody/ai-chatbot-service)<br><sub>개인 정리</sub> [B7-1](https://github.com/giyeop-cody/B7-1) | — | 팀 구현 진행중 (커밋 245개, 최근 2026-09-15) | [원문](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/B7-1/b7-1-description.md) · [연결](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/B7-1/links.md) |
| **B7-2** | 웹 기반 AI 챗봇 서비스 고도화 프로젝트 | 120h | `ai-sw-basic/B7-2/` | [B7-2](https://github.com/giyeop-cody/B7-2) | — | 대기 | [원문](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/B7-2/b7-2-description.md) · [연결](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/B7-2/links.md) |

> `B7-1` 의 실제 구현은 팀 조직 레포 [codyssey-term-mission-B7-1/ai-chatbot-service](https://github.com/codyssey-term-mission-B7-1/ai-chatbot-service) 다 (커밋 245개). `ai-sw-basic/B7-1` 서브모듈은 개인 정리 레포를 가리킨다.

---

## 2️⃣ 심화(A) — AI/SW 심화 · 11과제 · 800h

과제마다 **제출물 레포(`A#-#/`)** 와 **학습기록 레포(`A#-#-studylog/`)** 가 1:1 로 짝지어진다. 과정 단위 문서(학습맵·태스크보드·요구사항 대조·명세 모호점)는 [codyssey-A-studylog-hub](https://github.com/giyeop-cody/codyssey-A-studylog-hub) 🔒 `docs/` 에만 있다.

| 코드 | 과제명 | 시간 | 이 레포 안 위치 | 제출물 레포 (미션) | 학습기록 (스터디) | 상태 | 정의서(taskmap) |
|:--:|---|:--:|---|---|---|---|---|
| **A1-1** | 쇼핑몰에서 누가 자주 오고 많이 사는지 분석해서 단골 찾기 | 60h | `A1-1/` + `A1-1-studylog/` | [codyssey-A1-1-mission](https://github.com/giyeop-cody/codyssey-A1-1-mission) 🔒<br><sub>선행/개인</sub> [ecommerce-rfm-analysis](https://github.com/giyeop-cody/ecommerce-rfm-analysis) | [codyssey-A1-1-studylog](https://github.com/giyeop-cody/codyssey-A1-1-studylog) 🔒 | 구현 완료 — 게이트 6/6 PASS | [원문](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/A1-1/a1-1-description.md) · [연결](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/A1-1/links.md) |
| **A2-1** | AI가 어떻게 학습하는지 수학으로 직접 풀어보기 | 60h | `A2-1/` + `A2-1-studylog/` | [codyssey-A2-1-mission](https://github.com/giyeop-cody/codyssey-A2-1-mission) 🔒 | [codyssey-A2-1-studylog](https://github.com/giyeop-cody/codyssey-A2-1-studylog) 🔒 | 구현 완료 — 게이트 4/4 PASS | [원문](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/A2-1/a2-1-description.md) · [연결](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/A2-1/links.md) |
| **A3-1** | 휴대폰으로 찍은 종이를 똑바르게 펴서 스캔하게 만들기 | 60h | `A3-1/` + `A3-1-studylog/` | [codyssey-A3-1-mission](https://github.com/giyeop-cody/codyssey-A3-1-mission) 🔒 | [codyssey-A3-1-studylog](https://github.com/giyeop-cody/codyssey-A3-1-studylog) 🔒 | 구현 완료 — 게이트 4/4 PASS | [원문](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/A3-1/a3-1-description.md) · [연결](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/A3-1/links.md) |
| **A3-2** | 영상 속 움직이는 사람·물건을 따라가며 표시해주기 | 80h | `A3-2/` + `A3-2-studylog/` | [codyssey-A3-2-mission](https://github.com/giyeop-cody/codyssey-A3-2-mission) 🔒 | [codyssey-A3-2-studylog](https://github.com/giyeop-cody/codyssey-A3-2-studylog) 🔒 | 스캐폴드 (미구현) | [원문](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/A3-2/a3-2-description.md) · [연결](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/A3-2/links.md) |
| **A4-1** | 원하는 내용이 들어있는 문서를 똑똑하게 찾아주는 검색기 만들기 | 70h | `A4-1/` + `A4-1-studylog/` | [codyssey-A4-1-mission](https://github.com/giyeop-cody/codyssey-A4-1-mission) 🔒 | [codyssey-A4-1-studylog](https://github.com/giyeop-cody/codyssey-A4-1-studylog) 🔒 | 스캐폴드 (미구현) | [원문](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/A4-1/a4-1-description.md) · [연결](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/A4-1/links.md) |
| **A4-2** | 글 속에 숨은 정보와 기분(좋음/나쁨)을 자동으로 뽑아내기 | 70h | `A4-2/` + `A4-2-studylog/` | [codyssey-A4-2-mission](https://github.com/giyeop-cody/codyssey-A4-2-mission) 🔒 | [codyssey-A4-2-studylog](https://github.com/giyeop-cody/codyssey-A4-2-studylog) 🔒 | 스캐폴드 (미구현) | [원문](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/A4-2/a4-2-description.md) · [연결](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/A4-2/links.md) |
| **A5-1** | 대출을 해줘도 될지 AI가 대신 판단해주는 시스템 만들기 | 80h | `A5-1/` + `A5-1-studylog/` | [codyssey-A5-1-mission](https://github.com/giyeop-cody/codyssey-A5-1-mission) 🔒 | [codyssey-A5-1-studylog](https://github.com/giyeop-cody/codyssey-A5-1-studylog) 🔒 | 스캐폴드 (미구현) | [원문](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/A5-1/a5-1-description.md) · [연결](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/A5-1/links.md) |
| **A5-2** | AI가 왜 그런 결정을 했는지 이유를 사람에게 설명해주게 하기 | 80h | `A5-2/` + `A5-2-studylog/` | [codyssey-A5-2-mission](https://github.com/giyeop-cody/codyssey-A5-2-mission) 🔒 | [codyssey-A5-2-studylog](https://github.com/giyeop-cody/codyssey-A5-2-studylog) 🔒 | 스캐폴드 (미구현) | [원문](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/A5-2/a5-2-description.md) · [연결](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/A5-2/links.md) |
| **A6-1** | AI의 속 엔진(두뇌)을 내 손으로 직접 만들어보기 | 80h | `A6-1/` + `A6-1-studylog/` | [codyssey-A6-1-mission](https://github.com/giyeop-cody/codyssey-A6-1-mission) 🔒 | [codyssey-A6-1-studylog](https://github.com/giyeop-cody/codyssey-A6-1-studylog) 🔒 | 스캐폴드 (미구현) | [원문](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/A6-1/a6-1-description.md) · [연결](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/A6-1/links.md) |
| **A6-2** | AI가 어디서 자꾸 틀리는지 찾아내서 더 똑똑하게 만들기 | 80h | `A6-2/` + `A6-2-studylog/` | [codyssey-A6-2-mission](https://github.com/giyeop-cody/codyssey-A6-2-mission) 🔒 | [codyssey-A6-2-studylog](https://github.com/giyeop-cody/codyssey-A6-2-studylog) 🔒 | 스캐폴드 (미구현) | [원문](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/A6-2/a6-2-description.md) · [연결](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/A6-2/links.md) |
| **A7-1** | CV, NLP 자율 주제 프로젝트 | 80h | — | — | — | 미착수 (레포 없음) | [원문](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/A7-1/a7-1-description.md) · [연결](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/A7-1/links.md) |

- **A1-1·A2-1·A3-1**: 게이트 통과까지 끝난 제출물. 2026-09-27 에 클론 후 재실행해 확인했다 — A1-1 `pytest` 11 passed·자가채점 35/35·게이트 6/6, A2-1 `pytest` 19 passed·게이트 4/4, A3-1 `pytest` 9 passed·게이트 4/4.
- **A3-2 ~ A6-2**: 스캐폴드. `python -m pytest -q` 는 skip, `MISSION_STRICT=1` 은 **빨강** — 미구현을 숨기지 않는 계약.
- **A7-1** (CV·NLP 자율 주제): 허브 범위 밖이었고 레포도 없다.
- A1~A6 의 학습 흐름 분석과 M 과정 진입 연결고리는 [codyssey-AI-Applied](https://github.com/giyeop-cody/codyssey-AI-Applied) 🔒 에도 정리돼 있다.

---

## 3️⃣ 응용(M) — AI/SW 응용 · 15과제 · 5280h

15과제 전부 **미션 정의서만 있고 구현 레포가 없다** (과정 기간 2027-04-01 ~ 2027-09-30). 정의서는 [codyssey-taskmap](https://github.com/giyeop-cody/codyssey-taskmap) 🔒 의 `M*/` 폴더에 있다.

| 코드 | 과제명 | 시간 | 과목 | 제출물 레포 | 정의서(taskmap) |
|:--:|---|:--:|---|---|---|
| **M1-1** | 사람이 운전하지 않아도 도시에서 달리는 자동차 AI 만들기 | 440h | 모빌리티·자율주행 | — 레포 없음 | [원문](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/M1-1/m1-1-description.md) · [연결](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/M1-1/links.md) |
| **M1-2** | 어디서 택시 탈 사람이 많을지 AI가 미리 알려주기 | 280h | 모빌리티·자율주행 | — 레포 없음 | [원문](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/M1-2/m1-2-description.md) · [연결](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/M1-2/links.md) |
| **M2-1** | 전기를 언제 얼마나 만들고 쓸지 AI가 알아서 조절하기 | 280h | 에너지·인프라 | — 레포 없음 | [원문](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/M2-1/m2-1-description.md) · [연결](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/M2-1/links.md) |
| **M2-2** | 거대한 컴퓨터실의 에어컨·전기를 AI가 효율적으로 돌리기 | 440h | 에너지·인프라 | — 레포 없음 | [원문](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/M2-2/m2-2-description.md) · [연결](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/M2-2/links.md) |
| **M3-1** | 창고 안에서 로봇이 스스로 길을 찾아 물건 나르게 하기 | 440h | 로보틱스 | — 레포 없음 | [원문](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/M3-1/m3-1-description.md) · [연결](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/M3-1/links.md) |
| **M3-2** | 강아지처럼 네 발로 걷는 로봇이 스스로 움직이게 만들기 | 280h | 로보틱스 | — 레포 없음 | [원문](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/M3-2/m3-2-description.md) · [연결](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/M3-2/links.md) |
| **M4-1** | 공장 기계가 고장 나기 전 AI가 알려주고 불량품도 찾아내기 | 440h | 제조·소재 | — 레포 없음 | [원문](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/M4-1/m4-1-description.md) · [연결](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/M4-1/links.md) |
| **M4-2** | 같은 재료로 금속을 더 많이 뽑아낼 방법 AI가 찾기 | 280h | 제조·소재 | — 레포 없음 | [원문](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/M4-2/m4-2-description.md) · [연결](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/M4-2/links.md) |
| **M5-1** | 중환자실 환자가 위험해지기 전에 AI가 미리 알아차리기 | 280h | 헬스케어 | — 레포 없음 | [원문](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/M5-1/m5-1-description.md) · [연결](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/M5-1/links.md) |
| **M5-2** | 가슴 엑스레이 사진을 보고 AI가 여러 병을 한 번에 찾아주기 | 440h | 헬스케어 | — 레포 없음 | [원문](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/M5-2/m5-2-description.md) · [연결](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/M5-2/links.md) |
| **M6-1** | 신용 이력 없는 사람도 AI가 공정하게 신용점수 매겨주기 | 280h | 금융 | — 레포 없음 | [원문](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/M6-1/m6-1-description.md) · [연결](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/M6-1/links.md) |
| **M6-2** | AI가 알아서 투자 정보를 찾고 돈 굴릴 방법을 조언해주기 | 440h | 금융 | — 레포 없음 | [원문](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/M6-2/m6-2-description.md) · [연결](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/M6-2/links.md) |
| **M7-1** | 글과 사진을 함께 이해해서 원하는 상품 찾고 추천해주기 | 280h | 이커머스·마케팅 | — 레포 없음 | [원문](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/M7-1/m7-1-description.md) · [연결](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/M7-1/links.md) |
| **M7-2** | 어떤 손님이 떠날지 AI로 맞히고 잡을 방법·가성비 찾기 | 440h | 이커머스·마케팅 | — 레포 없음 | [원문](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/M7-2/m7-2-description.md) · [연결](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/M7-2/links.md) |
| **M8-1** | AI 올인원 Final Project 자율 주제 | 240h | Final Project | — 레포 없음 | [원문](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/M8-1/m8-1-description.md) · [연결](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/M8-1/links.md) |

착수하면 A 트랙 관례를 그대로 쓴다: `codyssey-M#-#-mission`(제출물) + `codyssey-M#-#-studylog`(학습기록), 그리고 이 레포에 `M#-#/` 서브모듈로 붙인다.

A → M 진입 연결(기존 정리): A3 → M1·M3 (모빌리티·로보틱스) · A4 → M7 (이커머스 추천·이탈) · A5 → M6 (금융 신용·투자) · A6 → M 전과정 (딥러닝 기반).

---

## 📕 미션 정의서 — codyssey-taskmap

[codyssey-taskmap](https://github.com/giyeop-cody/codyssey-taskmap) 🔒 이 `codyssey-taskmap/` 서브모듈로 들어와 있다. 41과제 전체의 원문이다.

| 파일 | 내용 |
|---|---|
| [`LINKS.md`](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/LINKS.md) | 41과제 ↔ 레포 연결 대장 (역할·pin 커밋·상태) |
| [`PROGRESS.md`](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/PROGRESS.md) | 트랙별 구현·검증 상태와 근거, 남은 절차 |
| [`README.md`](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/README.md) | 과정 구조 + 3과정 과제 목록 |
| [`codyssey-all-urls.md`](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/codyssey-all-urls.md) | Codyssey 원문 API URL 41개 (로그인 세션 필요) |
| `{CODE}/` | 과제별 원문(`-description.md`·`-mission.jpg`·`meta.json`) + `links.md`(연결) |

## 🔗 상호 연결 규칙

1. **양방향** — 여기서 과제 레포를 가리키면, 그 레포 README 상단 「Codyssey 연결」 표도 정의서(`codyssey-taskmap/{CODE}/`)를 가리킨다.
2. **역할 분리** — 제출물(미션) / 학습기록(스터디) / 선행·개인 레포를 섞지 않는다. A 트랙은 미션과 스터디를 별도 레포로 둔다.
3. **원문 불변** — taskmap 의 `-description.md`·`-mission.jpg`·`meta.json` 은 원본 데이터라 진행 상태를 쓰지 않는다. 연결은 `links.md`, 서사는 `PROGRESS.md`.
4. **pin + 근거** — 서브모듈 pin 커밋과 그 상태 판단 근거(실행 결과·PR·이슈)를 함께 남긴다.
5. **안 한 것은 완료로 쓰지 않는다** — 플랫폼 공식 평가·외부 동료평가는 별도 단계로 표시한다.

## 🚀 클론 및 사용 방법

```bash
# 1) 공개 부분만 (기초 허브)
git clone https://github.com/giyeop-cody/codyssey.git
cd codyssey && git submodule update --init ai-sw-basic

# 2) 전체 (심화·정의서 포함 — 비공개 레포가 있으므로 인증 필요)
git clone --recursive https://github.com/giyeop-cody/codyssey.git
# 이미 클론한 경우
git submodule update --init --recursive

# 3) 최신 상태로 갱신
git submodule update --remote --recursive

# 4) 비공개 서브모듈 인증 (토큰은 환경변수로만 — .gitmodules 에 절대 넣지 않는다)
git config --global url."https://${GITHUB_TOKEN}@github.com/".insteadOf "https://github.com/"
```

서브모듈 23개 중 **22개가 비공개** 레포다(A 트랙 20 + 허브 + taskmap). 권한이 없으면 그 폴더는 비어 보이고 GitHub 웹에서는 링크가 404 다 — 공개 레포만 필요하면 `ai-sw-basic/` 만 초기화한다.

## 📝 각 과제 레포지토리

각 과제는 독립적인 Git 레포지토리로 관리되며, 서브모듈을 통해 이 레포에 연결된다. B 트랙 과제 레포에는 `QUEST.md`(과제 내용)·`mission.jpg`(미션 설명 이미지)·`README.md`·`LEARNING.md` 가 있고, A 트랙은 `-mission`(제출물)과 `-studylog`(학습기록)로 나뉜다.

---

> *이 레포지토리는 Codyssey 학습 플랫폼의 과제 체계를 기반으로 자동 구성되었습니다.*  
> *3과정 통합·정의서 연결 갱신: 2026-09-27*

