"""Sensitivity analyses using only synthetic event records.

Run: python3 experiments/equal-ctr-different-behavior/sensitivity.py
No human-subject observations or validated risk ranking.
"""
import csv
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean, pvariance

PATH = Path(__file__).parent / "data.csv"
with PATH.open(newline="", encoding="utf-8") as handle:
    rows = list(csv.DictReader(handle))
by_person = defaultdict(list)
for row in rows:
    by_person[row["learner"]].append(row)

def describe(events):
    risky = [r for r in events if r["risky"] == "1"]
    counts = Counter(r["category"] for r in events)
    bad = Counter(r["category"] for r in risky)
    rates = {category: bad[category] / count for category, count in counts.items()}
    return {
        "ctr": len(risky) / len(events),
        "risky_categories": len(bad),
        "repeat_categories": sum(n >= 2 for n in bad.values()),
        "mean_decision_time": mean(float(r["decision_seconds"]) for r in events),
        "category_rate_variance": pvariance(rates.values()) if len(rates) > 1 else None,
        "macro_category_ctr": mean(rates.values()),
        "exposure": dict(sorted(counts.items())),
    }

# Case 1: original exposure distribution
baseline = {key: describe(group) for key, group in by_person.items()}
assert baseline["A"]["ctr"] == baseline["B"]["ctr"] == 0.3
assert baseline["A"]["risky_categories"] == 1
assert baseline["B"]["risky_categories"] == 3

# Case 2: same observed learner A decisions, add four non-risky phishing exposures.
# CTR changes; concentration of the existing risky choices does not.
extra = [dict(learner="A", category="phishing", risky="0", decision_seconds="25")] * 4
exposure_shift = describe(by_person["A"] + extra)
assert exposure_shift["ctr"] == 3 / 14
assert exposure_shift["risky_categories"] == 1

# Case 3: what if one risky response is relabeled due to an ambiguous scoring key?
recoded = [dict(row) for row in by_person["A"]]
recoded[0]["risky"] = "0"
label_shift = describe(recoded)
assert label_shift["ctr"] == 0.2
assert label_shift["repeat_categories"] == 1

# Case 4: if one category is absent, variance may be 0 or undefined.
single = describe([dict(learner="C", category="phishing", risky="1", decision_seconds="20")])
assert single["category_rate_variance"] is None

if __name__ == "__main__":
    for key, data in [
        ("baseline_A", baseline["A"]),
        ("baseline_B", baseline["B"]),
        ("A_more_safe_exposures", exposure_shift),
        ("A_one_label_changed", label_shift),
        ("single_category", single),
    ]:
        print(key, data)
