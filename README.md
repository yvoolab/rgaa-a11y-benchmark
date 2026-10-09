# rgaa-a11y-judgement

Six HTML fragments, one question each: which WCAG 2.2 success criterion does this violate, or NONE?
A Kaggle Benchmarks task written for the [DEV Kaggle Benchmarking Challenge](https://dev.to/challenges/kaggle-2026-09-23).

- Task on Kaggle: https://www.kaggle.com/benchmarks/tasks/delphine53303/rgaa-a11y-judgement
- `benchmark.py` — the task (six cases, one prompt, deterministic grading, score = cases passed / 6)
- `results/` — raw run files downloaded with `kaggle b t download`, plus `summary.md`
- `summarize.py` — rebuilds `results/summary.md` from the run files

```
pip install kaggle kaggle-benchmarks
kaggle b init -y && set -a && . ./.env && set +a && python benchmark.py   # local run
kaggle b t push rgaa-a11y-judgement -f benchmark.py --wait
kaggle b t run rgaa-a11y-judgement -m claude-sonnet-5-default -m gemini-3-flash-preview --wait
kaggle b t download rgaa-a11y-judgement -o results && python summarize.py
```
