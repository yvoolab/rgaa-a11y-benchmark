| Model | Lenient (any defensible SC) | Strict (primary SC) | Cost USD | Latency s |
|---|---|---|---|---|
| deepseek-ai/deepseek-r1-0528 | 6/6 | 6/6 | $0.0588 | 65 |
| google/gemini-3-flash-preview | 6/6 | 5/6 | $0.0263 | 44 |
| google/gemini-3.7-flash | 6/6 | 5/6 | $0.0272 | 68 |
| anthropic/claude-sonnet-5@default | 6/6 | 4/6 | $0.0073 | 10 |
| openai/gpt-oss-120b | 5/6 | 4/6 | $0.0005 | 149 |

| Case | expected | anthropic/claude-sonnet-5@default | deepseek-ai/deepseek-r1-0528 | google/gemini-3-flash-preview | google/gemini-3.7-flash | openai/gpt-oss-120b |
|---|---|---|---|---|---|---|
| img-no-alt | 1.1.1 | 1.1.1 | <think> We are given an HTML fragment: < | 1.1.1 | 1.1.1 | 1.1.1 |
| input-no-label | 1.3.1 | 3.3.2 | <think> We are given an HTML fragment: < | 3.3.2 | 3.3.2 | 3.3.2 |
| low-contrast | 1.4.3 | 1.4.3 | <think> We are given an HTML fragment: < | 1.4.3 | 1.4.3 | 1.4.3 |
| div-button | 2.1.1 | 4.1.2 | <think> We are given an HTML fragment: ` | 2.1.1 | 2.1.1 | 2.1.1 |
| no-lang | 3.1.1 | 3.1.1 | <think> We are given an HTML fragment: < | 3.1.1 | 3.1.1 | 3 |
| ok-link | NONE | NONE | <think> We are auditing a French public  | NONE | NONE | NONE |
