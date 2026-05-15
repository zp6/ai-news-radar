# Fix #15
def dedup(arts):
    seen = set()
    return [a for a in arts if (t:=a.get('title','').strip().lower()) and not (t in seen or seen.add(t))]
