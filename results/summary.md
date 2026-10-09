| Model | Lenient (any defensible SC) | Strict (primary SC) | Cost USD | Latency s |
|---|---|---|---|---|
| google/gemini-3-flash-preview | 6/6 | 5/6 | $0.0263 | 44 |
| google/gemini-3.7-flash | 6/6 | 5/6 | $0.0272 | 68 |
| anthropic/claude-sonnet-5@default | 6/6 | 4/6 | $0.0073 | 10 |

| Case | expected | anthropic/claude-sonnet-5@default | google/gemini-3-flash-preview | google/gemini-3.7-flash |
|---|---|---|---|---|
| img-no-alt | 1.1.1 | 1.1.1 | 1.1.1 | 1.1.1 |
| input-no-label | 1.3.1 | 3.3.2 | 3.3.2 | 3.3.2 |
| low-contrast | 1.4.3 | **1.4.3** | 1.4.3 | 1.4.3 |
| div-button | 2.1.1 | 4.1.2 | 2.1.1 | 2.1.1 |
| no-lang | 3.1.1 | 3.1.1 | 3.1.1 | 3.1.1 |
| ok-link | NONE | NONE | NONE | NONE |
