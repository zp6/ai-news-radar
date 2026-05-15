# Fix for Issue #15 - AI News Radar Enhancement
from typing import List, Dict
from datetime import datetime

def filter_by_date(articles: List[Dict], days: int = 7) -> List[Dict]:
    cutoff = datetime.now().timestamp() - (days * 86400)
    return [a for a in articles if a.get("timestamp", 0) > cutoff]

def deduplicate_articles(articles: List[Dict]) -> List[Dict]:
    seen_titles = set()
    unique = []
    for article in articles:
        title = article.get("title", "").lower().strip()
        if title and title not in seen_titles:
            seen_titles.add(title)
            unique.append(article)
    return unique

def calculate_relevance(article: Dict, keywords: List[str]) -> float:
    text = (article.get("title", "") + " " + article.get("description", "")).lower()
    matches = sum(1 for kw in keywords if kw.lower() in text)
    return matches / max(len(keywords), 1)
