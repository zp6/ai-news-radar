# 📡 AI News Radar

> **AI 소식, 어디서 가장 먼저 터지는가?**
> 속도 순으로 정렬한 AI 뉴스 소스 큐레이션. 오픈소스 모델 드랍부터 OpenAI 키노트, 논문 프리프린트까지 — *가장 빠른 채널부터 가장 깊은 분석까지* 한 페이지에.

![Last Updated](https://img.shields.io/badge/updated-2026--05--01-brightgreen)
![Sources](https://img.shields.io/badge/sources-80+-blue)
![Lang](https://img.shields.io/badge/lang-한국어-red)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

## ⚡ 속도 티어 (TL;DR)

| Tier | 채널 | 평균 지연 | 시그널-노이즈 비 | 추천 대상 |
|:---:|---|:---:|:---:|---|
| **S** | X (Twitter) — 핵심 인물 리스트 | **0–10분** | 중 | 모델 드랍·키노트·해킹뉴스를 *제일 먼저* 알고 싶은 사람 |
| **S** | r/LocalLLaMA | **5–30분** | 상 | 오픈소스 LLM·로컬 추론·벤치마크 즉시 반응 |
| **A** | Discord (Latent Space, LAION, HF) | **수십 분** | 중상 | 빌더 커뮤니티 인사이트 |
| **A** | Hacker News (`news.ycombinator.com/?q=AI`) | **1–6시간** | 매우 상 | 큐레이션된 상위 토론 |
| **B** | 뉴스레터 (TLDR AI, Rundown, Ben's Bites) | **다음날 아침** | 매우 상 | 하루 한 번 정리, 놓친 거 없는지 체크 |
| **B** | YouTube (AI Explained, Matthew Berman) | **1–3일** | 상 | 심층 해설·실험 리뷰 |
| **C** | The Batch / Import AI / Interconnects | **주 1회** | 최상 | 잡음 없이 의미만 — 연구·정책 흐름 |

> 💡 **추천 조합**: S 티어 1–2개 라이브 모니터링 + B 티어 뉴스레터 1개 구독 + C 티어 주간 1개. 더 넣으면 노이즈만 늘어남.

---

## 🐦 X (Twitter) — 실시간 (S Tier)

> 모델 출시·기업 발표·연구자 핫테이크는 거의 100% 여기서 먼저 터집니다. **리스트로 묶어서 보세요** — 타임라인 알고리즘은 AI 속보에 너무 느립니다.

### 🏢 기업/연구소 공식 계정
- [@OpenAI](https://x.com/OpenAI) · [@AnthropicAI](https://x.com/AnthropicAI) · [@GoogleDeepMind](https://x.com/GoogleDeepMind)
- [@xai](https://x.com/xai) · [@MistralAI](https://x.com/MistralAI) · [@AIatMeta](https://x.com/AIatMeta) · [@Alibaba_Qwen](https://x.com/Alibaba_Qwen)
- [@HuggingFace](https://x.com/huggingface) · [@perplexity_ai](https://x.com/perplexity_ai) · [@cursor_ai](https://x.com/cursor_ai)

### 👤 개인 (CEO/리더)
- [@sama](https://x.com/sama) — Sam Altman (OpenAI)
- [@DarioAmodei](https://x.com/DarioAmodei), [@AnthropicAI](https://x.com/AnthropicAI) 임원진
- [@elonmusk](https://x.com/elonmusk) — xAI / Grok
- [@demishassabis](https://x.com/demishassabis) — Google DeepMind
- [@miramurati](https://x.com/miramurati) — Thinking Machines

### 🧠 연구자/엔지니어 (가장 빠른 해석)
- [@karpathy](https://x.com/karpathy) — Andrej Karpathy
- [@ylecun](https://x.com/ylecun) — Yann LeCun
- [@drjimfan](https://x.com/drjimfan) — Jim Fan (NVIDIA)
- [@AndrewYNg](https://x.com/AndrewYNg) — Andrew Ng
- [@goodside](https://x.com/goodside) — Riley Goodside (프롬프트 엔지니어링)
- [@swyx](https://x.com/swyx) — shawn @ Latent Space
- [@_philschmid](https://x.com/_philschmid) — Philipp Schmid (HF→Google)
- [@simonw](https://x.com/simonw) — Simon Willison (LLM CLI)

> 📌 **즉시 적용**: 위 계정만 묶어서 [X List](https://help.x.com/en/using-x/x-lists) 만들면 네이티브 클라이언트가 알고리즘 없는 시간순 피드가 됩니다.

---

## 🟧 Reddit — 커뮤니티 반응 (S/A Tier)

| 서브레딧 | 무엇을 보나 |
|---|---|
| [r/LocalLLaMA](https://reddit.com/r/LocalLLaMA) | **오픈소스 LLM 1순위.** 새 모델 양자화·벤치 리뷰가 출시 30분 안에 올라옴 |
| [r/singularity](https://reddit.com/r/singularity) | 일반인 친화 속보 + 밈. 시그널 약하지만 빠름 |
| [r/MachineLearning](https://reddit.com/r/MachineLearning) | 논문 토론 정통 채널 ([D]/[R] 플레어) |
| [r/OpenAI](https://reddit.com/r/OpenAI) · [r/ClaudeAI](https://reddit.com/r/ClaudeAI) | 모델별 사용자 경험 |
| [r/StableDiffusion](https://reddit.com/r/StableDiffusion) | 이미지/비디오 생성 — 새 체크포인트 가장 빠름 |

---

## 📨 뉴스레터 — 정리된 하루 (B Tier)

| 이름 | 빈도 | 톤 | 링크 |
|---|:---:|---|---|
| **TLDR AI** | 매일 | 5분 컷, 무료 | [tldr.tech/ai](https://tldr.tech/ai) |
| **The Rundown AI** | 매일 | 산업/제품 중심 | [therundown.ai](https://www.therundown.ai/) |
| **Ben's Bites** | 매일 | 캐주얼·요약 강함 | [bensbites.com](https://bensbites.com/) |
| **AI Breakfast** | 주 1회 | 풍부한 큐레이션 | [aibreakfast.beehiiv.com](https://aibreakfast.beehiiv.com/) |
| **Last Week in AI** | 주 1회 | 학계+산업 골고루 | [lastweekin.ai](https://lastweekin.ai/) |
| **The Batch** (Andrew Ng) | 주 1회 | 점잖고 깊음 | [deeplearning.ai/the-batch](https://www.deeplearning.ai/the-batch/) |
| **Import AI** (Jack Clark) | 주 1회 | 정책·안전·딥다이브 | [jack-clark.net](https://jack-clark.net/) |
| **Interconnects** (Nathan Lambert) | 주 2–3회 | 포스트트레이닝·RLHF 1티어 | [interconnects.ai](https://www.interconnects.ai/) |
| **Latent Space** (swyx) | 주 1–2회 | 빌더/엔지니어 관점 | [latent.space](https://www.latent.space/) |
| **Stratechery** (Ben Thompson) | 주 4회 (유료) | 비즈니스·전략 분석 최강 | [stratechery.com](https://stratechery.com/) |
| **Platformer** (Casey Newton) | 주 3회 | 빅테크·정책 | [platformer.news](https://www.platformer.news/) |
| **Semafor Technology** | 주 2회 | 무료 양질 | [semafor.com/technology](https://www.semafor.com/technology) |

---

## 📰 매체·블로그 (분석 깊이 우선)

- [The Information](https://www.theinformation.com/) — 빅테크 단독·내부 소식 (유료, 가장 빠른 deep scoop)
- [The Verge AI](https://www.theverge.com/ai-artificial-intelligence) — 일반인 친화 속도전
- [TechCrunch AI](https://techcrunch.com/category/artificial-intelligence/) — 자금조달·스타트업
- [Ars Technica AI](https://arstechnica.com/ai/) — 기술적으로 정확
- [MIT Tech Review AI](https://www.technologyreview.com/topic/artificial-intelligence/) — 사회적 함의
- [Wired AI](https://www.wired.com/tag/artificial-intelligence/) — 인터뷰·피처

### 🇰🇷 한국어
- [GeekNews](https://news.hada.io/) — Hacker News 한국판, AI 글 상위 노출
- [AI 타임스](https://www.aitimes.com/) — 산업 동향
- [모두의연구소](https://modulabs.co.kr/) — 커뮤니티·세미나
- [티타임즈TV (YouTube)](https://www.youtube.com/@TTimesTV) — 한국어 산업 해설

---

## 📄 논문·연구 (가장 깊은 신호, 가장 늦은 스피드)

- [arXiv cs.AI](https://arxiv.org/list/cs.AI/recent) — 매일 새 프리프린트
- [Hugging Face Papers](https://huggingface.co/papers) — 트렌딩 논문 + 토론 (요즘 사실상 표준)
- [alphaXiv](https://www.alphaxiv.org/) — arXiv UI 개선 + 코멘트
- [Papers with Code](https://paperswithcode.com/) — 논문+코드+벤치마크
- [Semantic Scholar](https://www.semanticscholar.org/) — AI 기반 검색·인용 그래프
- [Connected Papers](https://www.connectedpapers.com/) — 논문 그래프 시각화

---

## 🎥 YouTube — 심층 해설 (B Tier)

| 채널 | 강점 |
|---|---|
| [AI Explained](https://www.youtube.com/@aiexplained-official) | 균형 잡힌 분석·신중한 해설 |
| [Two Minute Papers](https://www.youtube.com/@TwoMinutePapers) | 논문 빠르게 훑기 |
| [Yannic Kilcher](https://www.youtube.com/@YannicKilcher) | 정통 논문 리뷰 |
| [Matthew Berman](https://www.youtube.com/@matthew_berman) | 새 모델 즉시 테스트·빌드 |
| [Wes Roth](https://www.youtube.com/@WesRoth) | 산업 속보·해설 |
| [1littlecoder](https://www.youtube.com/@1littlecoder) | 빠른 핸즈온 튜토리얼 |
| [Lex Fridman](https://www.youtube.com/@lexfridman) | 장시간 인터뷰 |

---

## 🔗 어그리게이터 / 트렌딩 (놓치기 싫을 때)

- [Hacker News](https://news.ycombinator.com/) — `news.ycombinator.com/?q=AI` 또는 [HN Best AI](https://hn.algolia.com/?query=AI)
- [Hugging Face Trending](https://huggingface.co/models?sort=trending) — 트렌딩 모델 실시간
- [Product Hunt — AI](https://www.producthunt.com/topics/artificial-intelligence) — 새 AI 제품 출시
- [GitHub Trending — Python](https://github.com/trending/python?since=daily) — AI 레포 90% 차지
- [Theresanaiforthat](https://theresanaiforthat.com/) — 새 AI 도구 디렉토리

---

## 💬 Discord 커뮤니티

- **Latent Space** — 빌더 중심, swyx 운영 ([초대 링크는 latent.space에서](https://www.latent.space/))
- **Hugging Face** — 모델·라이브러리 공식
- **EleutherAI** — 오픈소스 연구
- **LAION** — 데이터셋·이미지 모델
- **r/LocalLLaMA Discord** — 서브레딧 공식 채팅

---

## 🛠️ 자동화 팁 (놓치지 않는 법)

```text
1. X 리스트 1개 + 푸시 알림: 모델 드랍 즉시 캐치
2. RSS 리더 (Feedly/Inoreader)에 위 매체 OPML 등록 → 하루 1번 dump
3. Hacker News + r/LocalLLaMA 키워드 알림 (e.g., "GPT-5", "Claude 5")
4. 뉴스레터는 Gmail 라벨 + 필터로 받은편지함 분리 (출근길 10분에 일괄)
5. arXiv는 Hugging Face Papers 트렌딩으로 대체 — 사람이 한번 걸러줌
```

### 추천 도구
- [Feedly](https://feedly.com/) — RSS 어그리게이션 + AI 키워드 알림
- [Inoreader](https://www.inoreader.com/) — Power user 친화
- [Buttondown](https://buttondown.com/) / [Beehiiv](https://www.beehiiv.com/) — 본인 뉴스레터 시작용

---

## 🎯 시나리오별 추천

<details>
<summary><b>"전 그냥 안 놓치고만 싶어요"</b> (하루 10분)</summary>

1. **TLDR AI** 구독 (매일 아침 5분)
2. **r/LocalLLaMA** 일주일에 한 번 둘러보기
3. 끝.
</details>

<details>
<summary><b>"빌더입니다, 새 모델·툴 다 써봐야 해요"</b> (하루 30분)</summary>

1. X 리스트 (위 빌더/연구자 30명)
2. **r/LocalLLaMA** 매일
3. **Hugging Face Trending Models** 매일
4. **Latent Space** + **Interconnects** 뉴스레터
5. **Matthew Berman** 또는 **AI Explained** 영상 주 2–3개
</details>

<details>
<summary><b>"투자/전략 관점이 필요해요"</b> (하루 20–40분)</summary>

1. **Stratechery** (유료, 가치 있음)
2. **The Information** (유료, 단독 스쿠프)
3. **Platformer** + **Semafor Technology** (무료)
4. X — CEO 계정 위주
5. **The Batch** (Andrew Ng) — 학술·산업 거시
</details>

<details>
<summary><b>"연구자입니다, 시그널만 주세요"</b></summary>

1. **arXiv cs.AI** + **Hugging Face Papers**
2. **Import AI** (Jack Clark) — 안전·정책
3. **Interconnects** (Nathan Lambert) — 포스트트레이닝
4. X — Karpathy, LeCun, Jim Fan 등
5. NeurIPS/ICLR/ICML 직전 X 리스트 모니터링
</details>

---

## 🤝 기여

이 리스트는 살아있는 문서입니다. 좋은 소스 빠진 거 발견하면:
- **Issue**: 추천 채널 + 왜 좋은지 한 줄
- **PR**: 위 형식 따라 추가 + 어느 티어인지 근거

**기준**:
- 시그널-노이즈 비가 높을 것
- 한국어 사용자도 접근 가능 (영어는 OK, 유료여도 OK 단 명시)
- 최소 6개월 이상 꾸준히 운영

---

## 📜 License

MIT — 자유롭게 포크·번역·재배포.

---

<sub>Made with ☕ and an X timeline that wouldn't shut up. <br>
Inspired by [awesome-lists](https://github.com/sindresorhus/awesome) and the chaos of 2026 AI news.</sub>
