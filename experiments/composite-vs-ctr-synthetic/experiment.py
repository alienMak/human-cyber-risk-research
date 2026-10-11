"""Experiment 002: deterministic constructed scenarios, NOT participant observations.
Python 3 standard library only. No network access or real data.
"""
from math import isfinite

def composite(ctr, ttr_seconds, quiz_score, repeat_events):
    values = (ctr, ttr_seconds, quiz_score, repeat_events)
    if any(v is None for v in values):
        return None
    if not all(isinstance(v, (int, float)) and isfinite(v) for v in values):
        raise ValueError("All supplied values must be finite numbers")
    if not (0 <= ctr <= 1 and ttr_seconds >= 0 and 0 <= quiz_score <= 1 and repeat_events >= 0):
        raise ValueError("Input outside defined bounds")
    return round(100 * (0.35 * ctr + 0.20 * min(ttr_seconds / 300, 1)
                        + 0.25 * (1 - quiz_score) + 0.20 * min(repeat_events / 3, 1)), 2)

def ctr_only(ctr):
    return int(ctr * 100 + 0.5)

def main():
    cases = [
        ("A: high quiz / quick report / no repeats", .5, 30, .9, 0, 22.0),
        ("B: lower quiz / slow report / repeats", .5, 240, .3, 3, 71.0),
        ("C: no qualifying report time", .5, None, .5, 0, None),
        ("D: minimum defined composite", 0, 0, 1, 0, 0.0),
        ("E: maximum defined composite", 1, 300, 0, 3, 100.0),
        ("F: cap saturation", 1, 900, 0, 10, 100.0)
    ]
    for label, ctr, ttr, quiz, repeats, expected in cases:
        result = composite(ctr, ttr, quiz, repeats)
        assert result == expected, (label, result, expected)
        print(f"{label}: CTR-only {ctr_only(ctr)}, composite {result if result is not None else 'unavailable'}")
    for bad in [(-.1, 30, .5, 0), (.5, -1, .5, 0), (.5, 30, 1.2, 0), (.5, 30, .5, -1)]:
        try:
            composite(*bad)
        except ValueError:
            continue
        raise AssertionError(f"Out-of-range input accepted: {bad}")
    print("PASS: all synthetic examples and bounds assertions")

if __name__ == "__main__":
    main()
