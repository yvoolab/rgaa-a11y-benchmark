# %%
"""RGAA / WCAG accessibility judgement benchmark — Kaggle Benchmarks task file.

One task, six deterministic cases: each shows a small HTML fragment and asks the
model which WCAG 2.2 success criterion is violated (or NONE). A case passes when
the answer names any defensible criterion for that fragment (several fragments
legitimately fail more than one criterion). Score = cases passed, 0-6.
Ties to Yvoo's accessibility-audit service (F line).

Workflow (needs ~/.kaggle/kaggle.json first):
  kaggle b init -y && set -a && . ./.env && set +a && python benchmark.py
  kaggle b t push rgaa-a11y-judgement -f benchmark.py --wait
  kaggle b t run rgaa-a11y-judgement -m <model> --wait   # repeat -m per model
  kaggle b t publish rgaa-a11y-judgement
"""
import kaggle_benchmarks as kbench

# %%
# (slug, html, accepted criteria — primary first)
CASES = [
    ("img-no-alt", '<img src="hero.jpg">', ("1.1.1",)),
    ("input-no-label", '<input type="text" id="q" placeholder="Rechercher">', ("1.3.1", "3.3.2", "4.1.2")),
    ("low-contrast", '<p style="color:#999;background:#fff">Mentions légales</p>', ("1.4.3",)),
    ("div-button", '<div onclick="go()">Valider</div>', ("2.1.1", "4.1.2")),
    ("no-lang", '<html><head><title>Accueil</title></head><body>Bonjour</body></html>', ("3.1.1",)),
    ("ok-link", '<a href="/contact">Nous contacter</a>', ("NONE",)),
]

PROMPT = (
    "You are auditing a French public website for RGAA 4.1 / WCAG 2.2 compliance.\n"
    "HTML fragment:\n{html}\n\n"
    "Which single WCAG 2.2 success criterion does this fragment most directly violate? "
    "Answer with the criterion number only (e.g. 1.1.1), or NONE if it is compliant."
)


@kbench.task(
    name="rgaa-a11y-judgement",
    description="Six HTML fragments; name the violated WCAG 2.2 criterion (or NONE). Score = cases passed out of 6.",
)
def rgaa_a11y_judgement(llm) -> int:
    passed = 0
    for slug, html, accepted in CASES:
        with kbench.chats.new(slug):
            response = llm.prompt(PROMPT.format(html=html))
        ok = any(a.lower() in response.lower() for a in accepted)
        kbench.assertions.assert_true(ok, expectation=f"{slug}: should name one of {'/'.join(accepted)}")
        passed += ok
    return passed


# %%
rgaa_a11y_judgement.run(kbench.llm)
