"""Reproduce descriptive comparisons using synthetic events only."""
import csv
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean

rows = list(csv.DictReader((Path(__file__).parent / "data.csv").open()))
groups = defaultdict(list)
for row in rows:
    groups[row["learner"]].append(row)

for learner, events in sorted(groups.items()):
    risky = [e for e in events if e["risky"] == "1"]
    by_category = Counter(e["category"] for e in risky)
    print(learner, {
        "decisions": len(events),
        "risky": len(risky),
        "ctr": len(risky) / len(events),
        "risky_categories": len(by_category),
        "repeated_risky_categories": sum(n > 1 for n in by_category.values()),
        "mean_all_seconds": round(mean(float(e["decision_seconds"]) for e in events), 2),
        "mean_risky_seconds": round(mean(float(e["decision_seconds"]) for e in risky), 2),
    })
