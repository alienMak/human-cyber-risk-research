"""Experiment 002: purely constructed categorical decision sequences.

This public demonstration contains no platform scoring implementation, formula,
weights, production data, API interactions, or participant observations.
"""
from collections import Counter

SEQUENCES = {
    "Synthetic learner A": "RRRSSGSSGS",
    "Synthetic learner B": "RGSGRGSGRG",
}

def summarize(sequence):
    assert len(sequence) == 10
    assert set(sequence).issubset({"R", "S", "G"})
    counts = Counter(sequence)
    return {
        "total": len(sequence),
        "risky": counts["R"],
        "safe": counts["S"],
        "grey": counts["G"],
        "risky_rate": counts["R"] / len(sequence),
        "adjacent_risky_pairs": sum(
            sequence[i:i+2] == "RR" for i in range(len(sequence) - 1)
        ),
    }

def main():
    expected = [
        ("Synthetic learner A", (3, 5, 2, .3, 2)),
        ("Synthetic learner B", (3, 2, 5, .3, 0)),
    ]
    for label, target in expected:
        result = summarize(SEQUENCES[label])
        observed = (
            result["risky"], result["safe"], result["grey"],
            result["risky_rate"], result["adjacent_risky_pairs"]
        )
        assert observed == target, (label, observed)
        print(label, SEQUENCES[label], result)
    print("PASS: constructed decisions; equal risky-choice rate, distinct patterns")

if __name__ == "__main__":
    main()
