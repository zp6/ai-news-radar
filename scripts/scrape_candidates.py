#!/usr/bin/env python3
"""Daily AI source candidate scraper.

Pulls trending AI content from HN, Reddit, and Hugging Face, deduplicates
against links already in README.md, and writes a markdown report to stdout.
Zero dependencies (stdlib only).
"""

import json
import re
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

UA = "ai-news-radar-bot/1.0 (+https://github.com/xodn348/ai-news-radar)"
TIMEOUT = 25


def fetch_json(url: str):
    req = urllib.request.Request(
        url, headers={"User-Agent": UA, "Accept": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        return json.load(r)


def hn_top():
    since = int(datetime.now(timezone.utc).timestamp()) - 86400
    url = (
        "https://hn.algolia.com/api/v1/search"
        "?query=AI&tags=story"
        f"&numericFilters=points>=100,created_at_i>{since}"
        "&hitsPerPage=15"
    )
    try:
        data = fetch_json(url)
    except Exception as e:
        return [], str(e)
    items = []
    for h in data.get("hits", []):
        items.append({
            "title": h.get("title"),
            "url": h.get("url") or f"https://news.ycombinator.com/item?id={h['objectID']}",
            "score": h.get("points", 0),
            "comments": h.get("num_comments", 0),
        })
    return items, None


def reddit_top(sub: str):
    url = f"https://www.reddit.com/r/{sub}/top.json?t=day&limit=15"
    try:
        data = fetch_json(url)
    except Exception as e:
        return [], str(e)
    items = []
    for child in data.get("data", {}).get("children", []):
        d = child.get("data", {})
        items.append({
            "title": d.get("title"),
            "url": "https://reddit.com" + d.get("permalink", ""),
            "score": d.get("score", 0),
            "comments": d.get("num_comments", 0),
            "external_url": d.get("url_overridden_by_dest"),
        })
    return items, None


def hf_trending_models():
    url = "https://huggingface.co/api/models?sort=trending&limit=10"
    try:
        data = fetch_json(url)
    except Exception as e:
        return [], str(e)
    return [
        {
            "id": m.get("id"),
            "url": f"https://huggingface.co/{m.get('id')}",
            "downloads": m.get("downloads", 0),
            "likes": m.get("likes", 0),
        }
        for m in data
    ], None


def hf_daily_papers():
    url = "https://huggingface.co/api/daily_papers"
    try:
        data = fetch_json(url)
    except Exception as e:
        return [], str(e)
    items = []
    for p in data[:10]:
        paper = p.get("paper", {})
        items.append({
            "title": paper.get("title"),
            "url": f"https://huggingface.co/papers/{paper.get('id')}",
            "upvotes": paper.get("upvotes", 0),
        })
    return items, None


def existing_links() -> set:
    readme = Path("README.md").read_text(encoding="utf-8")
    return {
        u.rstrip("/").lower()
        for u in re.findall(r"https?://[^\s\)\]\>]+", readme)
    }


def section(title: str, items, fmt) -> str:
    if not items:
        return f"### {title}\n\n_No new items today (everything trending is already in the list, or feed empty)._\n"
    return f"### {title}\n\n" + "\n".join(fmt(i) for i in items) + "\n"


def main() -> None:
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    existing = existing_links()

    def is_new(url: str | None) -> bool:
        if not url:
            return True
        return url.rstrip("/").lower() not in existing

    parts: list[str] = [
        f"# 📡 Daily candidates — {today}",
        "",
        "Trending AI items pulled in the last 24h, filtered against sources already in the README.",
        "",
        "**Triage**:",
        "- ✅ High-signal + missing → open PR adding it (use the issue template)",
        "- 🔁 Already covered by a similar source → close",
        "- 🚫 Low-signal / off-topic → close",
        "",
    ]

    hn, err = hn_top()
    parts.append(section(
        "🟧 Hacker News — top AI stories (24h, ≥100 points)",
        [h for h in hn if is_new(h["url"])][:10],
        lambda h: f"- [{h['title']}]({h['url']}) — **{h['score']}** pts · {h['comments']} comments",
    ))
    if err:
        parts.append(f"> ⚠️ HN fetch error: `{err}`\n")

    for sub in ["LocalLLaMA", "MachineLearning", "singularity", "OpenAI", "ClaudeAI"]:
        rd, err = reddit_top(sub)
        parts.append(section(
            f"👽 r/{sub} — top of day",
            [r for r in rd if is_new(r.get("external_url") or r["url"])][:6],
            lambda r: f"- [{r['title']}]({r['url']}) — **{r['score']}** upvotes · {r['comments']} comments",
        ))
        if err:
            parts.append(f"> ⚠️ r/{sub} fetch error: `{err}`\n")

    hf_m, err = hf_trending_models()
    parts.append(section(
        "🤗 Hugging Face — trending models",
        [m for m in hf_m if is_new(m["url"])][:8],
        lambda m: f"- [{m['id']}]({m['url']}) — {m['downloads']:,} downloads · {m['likes']} likes",
    ))
    if err:
        parts.append(f"> ⚠️ HF models fetch error: `{err}`\n")

    hf_p, err = hf_daily_papers()
    parts.append(section(
        "📄 Hugging Face — daily papers",
        [p for p in hf_p if p["title"]][:8],
        lambda p: f"- [{p['title']}]({p['url']}) — {p['upvotes']} upvotes",
    ))
    if err:
        parts.append(f"> ⚠️ HF papers fetch error: `{err}`\n")

    parts.append("")
    parts.append("---")
    parts.append(
        f"_Generated by [`scripts/scrape_candidates.py`](scripts/scrape_candidates.py) "
        f"at {datetime.now(timezone.utc).isoformat(timespec='seconds')}._ "
        "Previous daily issues are auto-closed when this one is filed."
    )

    sys.stdout.write("\n".join(parts))


if __name__ == "__main__":
    main()
