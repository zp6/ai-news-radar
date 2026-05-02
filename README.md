# 📡 AI News Radar

> **Where does AI news break first?**
> A curated, speed-ranked list of AI news sources — from instant model drops to deep weekly analysis. One page, ranked by latency.

![Last Updated](https://img.shields.io/github/last-commit/xodn348/ai-news-radar?label=updated&color=brightgreen)
![Sources](https://img.shields.io/badge/sources-80+-blue)
![Auto Updated](https://img.shields.io/badge/auto--updated-weekly-orange)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

> 🔄 **Living document** — updated continuously. Star the repo to track changes. Open a PR or issue to add/remove a source. See [CONTRIBUTING](#-contributing).

---

## ⚡ Speed Tiers (TL;DR)

| Tier | Channel | Latency | Signal/Noise | Best For |
|:---:|---|:---:|:---:|---|
| **S** | X (Twitter) — curated lists | **0–10 min** | Medium | Catching model drops, keynotes, breaking news *first* |
| **S** | r/LocalLLaMA | **5–30 min** | High | Open-source LLMs, local inference, instant benchmark reactions |
| **A** | Discord (Latent Space, LAION, HF) | **Tens of minutes** | Med-High | Builder community insights |
| **A** | Hacker News (`news.ycombinator.com/?q=AI`) | **1–6 hours** | Very High | Curated top discussion |
| **B** | Newsletters (TLDR AI, Rundown, Ben's Bites) | **Next morning** | Very High | Daily catch-up — "did I miss anything?" |
| **B** | YouTube (AI Explained, Matthew Berman) | **1–3 days** | High | In-depth explainers, hands-on reviews |
| **C** | The Batch / Import AI / Interconnects | **Weekly** | Highest | Pure signal — research, policy, post-training |

> 💡 **Recommended combo**: 1–2 S-tier live monitors + 1 B-tier daily newsletter + 1 C-tier weekly. Adding more just adds noise.

---

## 🐦 X (Twitter) — Real-time (S Tier)

> Model launches, company announcements, and researcher hot takes break here ~100% of the time. **Use a List** — the algorithmic timeline is too slow for AI news.

### 🏢 Official company / lab accounts
- [@OpenAI](https://x.com/OpenAI) · [@AnthropicAI](https://x.com/AnthropicAI) · [@GoogleDeepMind](https://x.com/GoogleDeepMind)
- [@xai](https://x.com/xai) · [@MistralAI](https://x.com/MistralAI) · [@AIatMeta](https://x.com/AIatMeta) · [@Alibaba_Qwen](https://x.com/Alibaba_Qwen)
- [@HuggingFace](https://x.com/huggingface) · [@perplexity_ai](https://x.com/perplexity_ai) · [@cursor_ai](https://x.com/cursor_ai)

### 👤 Founders / executives
- [@sama](https://x.com/sama) — Sam Altman (OpenAI)
- [@DarioAmodei](https://x.com/DarioAmodei) — Anthropic
- [@elonmusk](https://x.com/elonmusk) — xAI / Grok
- [@demishassabis](https://x.com/demishassabis) — Google DeepMind
- [@miramurati](https://x.com/miramurati) — Thinking Machines

### 🧠 Researchers / engineers (fastest takes)
- [@karpathy](https://x.com/karpathy) — Andrej Karpathy
- [@ylecun](https://x.com/ylecun) — Yann LeCun
- [@drjimfan](https://x.com/drjimfan) — Jim Fan (NVIDIA)
- [@AndrewYNg](https://x.com/AndrewYNg) — Andrew Ng
- [@goodside](https://x.com/goodside) — Riley Goodside (prompt engineering)
- [@swyx](https://x.com/swyx) — Latent Space
- [@_philschmid](https://x.com/_philschmid) — Philipp Schmid (HF → Google)
- [@simonw](https://x.com/simonw) — Simon Willison (LLM CLI, blog)

> 📌 **Action**: Bundle these into an [X List](https://help.x.com/en/using-x/x-lists) — your native client becomes a chronological, algorithm-free feed.

---

## 🟧 Reddit — Community reactions (S/A Tier)

| Subreddit | What you get |
|---|---|
| [r/LocalLLaMA](https://reddit.com/r/LocalLLaMA) | **#1 for open-source LLMs.** Quantizations and benchmark reactions within 30 min of release |
| [r/singularity](https://reddit.com/r/singularity) | Layperson-friendly news + memes. Lower signal, very fast |
| [r/MachineLearning](https://reddit.com/r/MachineLearning) | Canonical paper discussion ([D]/[R] flairs) |
| [r/OpenAI](https://reddit.com/r/OpenAI) · [r/ClaudeAI](https://reddit.com/r/ClaudeAI) | Model-specific user experience |
| [r/StableDiffusion](https://reddit.com/r/StableDiffusion) | Image/video generation — fastest source for new checkpoints |

---

## 📨 Newsletters — Daily digest (B Tier)

| Name | Cadence | Tone | Link |
|---|:---:|---|---|
| **TLDR AI** | Daily | 5-min read, free | [tldr.tech/ai](https://tldr.tech/ai) |
| **The Rundown AI** | Daily | Industry / product focus | [therundown.ai](https://www.therundown.ai/) |
| **Ben's Bites** | Daily | Casual, strong summaries | [bensbites.com](https://bensbites.com/) |
| **AI Breakfast** | Weekly | Rich curation | [aibreakfast.beehiiv.com](https://aibreakfast.beehiiv.com/) |
| **Last Week in AI** | Weekly | Balanced academic + industry | [lastweekin.ai](https://lastweekin.ai/) |
| **The Batch** (Andrew Ng) | Weekly | Measured, deep | [deeplearning.ai/the-batch](https://www.deeplearning.ai/the-batch/) |
| **Import AI** (Jack Clark) | Weekly | Policy, safety, deep dives | [jack-clark.net](https://jack-clark.net/) |
| **Interconnects** (Nathan Lambert) | 2–3x/week | Top tier on post-training / RLHF | [interconnects.ai](https://www.interconnects.ai/) |
| **Latent Space** (swyx) | 1–2x/week | Builder / engineer angle | [latent.space](https://www.latent.space/) |
| **Stratechery** (Ben Thompson) | 4x/week (paid) | Best-in-class business strategy | [stratechery.com](https://stratechery.com/) |
| **Platformer** (Casey Newton) | 3x/week | Big tech + policy | [platformer.news](https://www.platformer.news/) |
| **Semafor Technology** | 2x/week | Free, high quality | [semafor.com/technology](https://www.semafor.com/technology) |

---

## 📰 Outlets / blogs (depth over speed)

- [The Information](https://www.theinformation.com/) — fastest deep scoops on big tech (paid)
- [The Verge AI](https://www.theverge.com/ai-artificial-intelligence) — accessible speed-runs
- [TechCrunch AI](https://techcrunch.com/category/artificial-intelligence/) — funding, startups
- [Ars Technica AI](https://arstechnica.com/ai/) — technically accurate
- [MIT Tech Review AI](https://www.technologyreview.com/topic/artificial-intelligence/) — societal angle
- [Wired AI](https://www.wired.com/tag/artificial-intelligence/) — long-form, interviews

---

## 📄 Papers / research (deepest signal, slowest)

- [arXiv cs.AI](https://arxiv.org/list/cs.AI/recent) — daily preprint dump
- [Hugging Face Papers](https://huggingface.co/papers) — trending papers + discussion (the de-facto standard)
- [alphaXiv](https://www.alphaxiv.org/) — better arXiv UI + comments
- [Papers with Code](https://paperswithcode.com/) — papers + code + benchmarks
- [Semantic Scholar](https://www.semanticscholar.org/) — AI-powered search + citation graph
- [Connected Papers](https://www.connectedpapers.com/) — visual paper graph

---

## 🎥 YouTube — In-depth (B Tier)

| Channel | Strength |
|---|---|
| [AI Explained](https://www.youtube.com/@aiexplained-official) | Balanced, careful analysis |
| [Two Minute Papers](https://www.youtube.com/@TwoMinutePapers) | Fast paper rundowns |
| [Yannic Kilcher](https://www.youtube.com/@YannicKilcher) | Rigorous paper reviews |
| [Matthew Berman](https://www.youtube.com/@matthew_berman) | Same-day testing of new models |
| [Wes Roth](https://www.youtube.com/@WesRoth) | Industry news + commentary |
| [1littlecoder](https://www.youtube.com/@1littlecoder) | Fast hands-on tutorials |
| [Lex Fridman](https://www.youtube.com/@lexfridman) | Long-form interviews |

---

## 🔗 Aggregators / trending (when you want full coverage)

- [Hacker News](https://news.ycombinator.com/) — `news.ycombinator.com/?q=AI` or [HN Algolia AI](https://hn.algolia.com/?query=AI)
- [Hugging Face Trending Models](https://huggingface.co/models?sort=trending) — trending models in real-time
- [Product Hunt — AI](https://www.producthunt.com/topics/artificial-intelligence) — new AI product launches
- [GitHub Trending — Python](https://github.com/trending/python?since=daily) — ~90% AI repos these days
- [There's An AI For That](https://theresanaiforthat.com/) — directory of new tools

---

## 💬 Discord communities

- **Latent Space** — builder-focused, run by swyx ([invite at latent.space](https://www.latent.space/))
- **Hugging Face** — official models / libraries
- **EleutherAI** — open-source research
- **LAION** — datasets, image models
- **r/LocalLLaMA Discord** — official subreddit chat

---

## 🛠️ Automation tips (so you don't miss anything)

```text
1. One curated X List + push notifications → instant model-drop alerts
2. RSS reader (Feedly / Inoreader) loaded with above outlets → 1x/day dump
3. Hacker News + r/LocalLLaMA keyword alerts (e.g., "GPT-5", "Claude 5")
4. Gmail label + filter for newsletters → batch-read on commute
5. Skip arXiv firehose — let HF Papers trending pre-filter for you
```

### Tools
- [Feedly](https://feedly.com/) — RSS aggregation + AI keyword alerts
- [Inoreader](https://www.inoreader.com/) — power-user friendly
- [Buttondown](https://buttondown.com/) / [Beehiiv](https://www.beehiiv.com/) — start your own newsletter

---

## 🎯 Recommendations by scenario

<details>
<summary><b>"Just don't let me miss anything important"</b> (10 min/day)</summary>

1. Subscribe to **TLDR AI** (5 min, every morning)
2. Browse **r/LocalLLaMA** once a week
3. Done.
</details>

<details>
<summary><b>"I'm a builder — I need to try every new model and tool"</b> (30 min/day)</summary>

1. X List of ~30 builders + researchers (above)
2. **r/LocalLLaMA** daily
3. **Hugging Face Trending Models** daily
4. **Latent Space** + **Interconnects** newsletters
5. 2–3 **Matthew Berman** or **AI Explained** videos / week
</details>

<details>
<summary><b>"I need investor / strategy lens"</b> (20–40 min/day)</summary>

1. **Stratechery** (paid, worth it)
2. **The Information** (paid, exclusive scoops)
3. **Platformer** + **Semafor Technology** (free)
4. X — CEO accounts
5. **The Batch** (Andrew Ng) — macro academic + industry
</details>

<details>
<summary><b>"Researcher — signal only"</b></summary>

1. **arXiv cs.AI** + **Hugging Face Papers**
2. **Import AI** (Jack Clark) — safety, policy
3. **Interconnects** (Nathan Lambert) — post-training
4. X — Karpathy, LeCun, Jim Fan, etc.
5. Watch X lists right before NeurIPS / ICLR / ICML
</details>

---

## 🔄 How this list stays current

This is a **living document**. Maintenance signals:

- ⏰ **Weekly**: maintainer reviews open issues / PRs and merges accepted additions
- 🤖 **Auto checks**: a scheduled job verifies links aren't dead and flags stale sources (no posts in 90 days)
- 📅 **Monthly**: tier reassessment — sources that slowed down get demoted, hot newcomers get promoted
- 🗑️ **Removed**: dead newsletters, abandoned channels, and accounts that pivoted away from AI

**Last major review**: see commit history. **Want to track changes?** ⭐ Star + Watch this repo.

---

## 🤝 Contributing

PRs and issues are how this stays alive. Please add or remove sources whenever you spot something.

### How to add a source
1. Open a PR editing `README.md` in the right section
2. Include: name, link, one-line description of *why* it's worth following
3. Propose a tier (S / A / B / C) and a one-line justification
4. Bonus: latency estimate and signal/noise self-assessment

### How to flag a stale source
- Open an issue titled `Stale: <source name>` with evidence (last post date, dead link, etc.)
- Or open a PR removing it directly

### Inclusion criteria
- High signal-to-noise ratio
- Accessible to a global English-speaking audience (paid is OK if marked)
- Active for at least 6 months
- Not pure self-promotion

### Tier guidelines
- **S** — breaks news within minutes, you'd actually miss things without it
- **A** — strong curation, high SNR, sub-day latency
- **B** — daily/weekly cadence, near-zero noise
- **C** — weekly+ deep analysis, almost never wrong

---

## 📜 License

MIT — fork, translate, redistribute freely.

---

<sub>Made with ☕ and an X timeline that wouldn't shut up. <br>
Inspired by [awesome-lists](https://github.com/sindresorhus/awesome) and the chaos of 2026 AI news.</sub>
