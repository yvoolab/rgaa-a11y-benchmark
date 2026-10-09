#!/usr/bin/env python3
"""Summarize downloaded Kaggle run files → results/summary.md (markdown table + per-model answers).
Usage: python summarize.py   (reads results/**/*.run.json)"""
import glob, json, os, re

CASES = ["img-no-alt", "input-no-label", "low-contrast", "div-button", "no-lang", "ok-link"]
PRIMARY = {"img-no-alt": "1.1.1", "input-no-label": "1.3.1", "low-contrast": "1.4.3",
           "div-button": "2.1.1", "no-lang": "3.1.1", "ok-link": "NONE"}

rows = []
for f in sorted(glob.glob("results/rgaa-a11y-judgement/2/**/*.run.json", recursive=True)):
    d = json.load(open(f, encoding="utf-8"))
    if "assertions" not in d:  # errored run (e.g. 429 from the proxy): nothing to score
        continue
    model = d.get("modelVersion", {}).get("slug") or os.path.basename(os.path.dirname(os.path.dirname(f)))
    answers, cost, latency = {}, 0, 0
    for c in d["conversations"]:
        for r in c.get("requests", []):
            m = r.get("metrics", {})
            cost += int(m.get("inputTokensCostNanodollars", 0)) + int(m.get("outputTokensCostNanodollars", 0))
            latency += int(m.get("totalBackendLatencyMs", 0))
            txt = [p.get("text", "") for ct in r["contents"] if ct["role"] == "CONTENT_ROLE_ASSISTANT" for p in ct["parts"]]
            answers[c["id"].rsplit("-", 1)[0]] = " ".join(txt).strip().strip("*`")
    lenient = sum(1 for a in d["assertions"] if a["status"].endswith("_PASSED"))
    strict = sum(1 for k, v in answers.items() if PRIMARY[k].lower() in v.lower())
    rows.append((model, lenient, strict, cost / 1e9, latency / 1000, answers))

out = ["| Model | Lenient (any defensible SC) | Strict (primary SC) | Cost USD | Latency s |", "|---|---|---|---|---|"]
for m, l, s, c, t, _ in sorted(rows, key=lambda r: (-r[1], -r[2])):
    out.append(f"| {m} | {l}/6 | {s}/6 | ${c:.4f} | {t:.0f} |")
out += ["", "| Case | expected | " + " | ".join(r[0] for r in rows) + " |", "|---|---|" + "---|" * len(rows)]
for k in CASES:
    out.append(f"| {k} | {PRIMARY[k]} | " + " | ".join(re.sub(r'\s+', ' ', r[5].get(k, ''))[:40] for r in rows) + " |")
open("results/summary.md", "w", encoding="utf-8").write("\n".join(out) + "\n")
print("\n".join(out))

if __name__ == "__main__" and rows:
    assert all(0 <= r[2] <= r[1] <= 6 for r in rows), rows  # strict never exceeds lenient
