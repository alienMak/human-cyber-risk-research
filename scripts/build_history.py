"""Build a public research timeline from reviewed historical records.

This script never manufactures dates, findings or contribution commits.
It writes only when the resulting document differs.
"""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "research" / "history.json"
DEST = ROOT / "docs" / "research-history.md"

def main():
    data = json.loads(SOURCE.read_text(encoding="utf-8"))
    rows = data["milestones"]
    if not isinstance(rows, list) or not rows:
        raise ValueError("Expected at least one milestone")
    lines = [
        "# How this research developed", "",
        "VISHWAR did not begin with this GitHub repository. The research and planning began in February 2025, and the capstone build began in August 2025. I'm documenting those earlier stages here rather than pretending these notes were committed at the time.", "",
        "This is a retrospective record. Dates refer to the work, not the GitHub commit date. Where I only know the year or month, I have left it at that.", ""
    ]
    previous = ""
    for row in rows:
        for key in ("period", "title", "description", "status", "evidence", "public"):
            if key not in row:
                raise ValueError(f"Missing field {key}")
        period = row["period"]
        if not isinstance(period, str) or not (
            len(period) == 4 and period.isdigit() or
            len(period) == 7 and period[:4].isdigit() and period[4] == "-" and period[5:].isdigit() and 1 <= int(period[5:]) <= 12
        ):
            raise ValueError(f"Invalid period: {period}")
        if previous and period < previous:
            raise ValueError("Milestones must be in chronological order")
        previous = period
        if row["status"] not in ("documented", "provisional"):
            raise ValueError("status must be documented or provisional")
        if not isinstance(row["public"], bool):
            raise ValueError("public must be boolean")
        if not row["public"] or row["status"] != "documented":
            continue
        for key in ("title", "description", "evidence"):
            if not isinstance(row[key], str) or not row[key].strip():
                raise ValueError(f"Empty {key}")
        lines.extend([f"## {period} — {row['title']}", "", row["description"], "",
                      f"*Record basis: {row['evidence']}.*", ""])
    lines += [
        "## Limits of this archive", "",
        "These entries are a summary, not a reconstruction of individual workdays. The history may be refined when dated source material is reviewed. Research questions and exploratory observations should not be mistaken for validated product claims.", ""
    ]
    result = "\n".join(lines)
    if "--check" in sys.argv:
        if not DEST.exists() or DEST.read_text(encoding="utf-8") != result:
            print("Research history needs regeneration.")
            return 1
        print("Research history matches reviewed records.")
        return 0
    if not DEST.exists() or DEST.read_text(encoding="utf-8") != result:
        DEST.write_text(result, encoding="utf-8")
        print("Updated research history from reviewed records.")
    else:
        print("No changes to research history.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
