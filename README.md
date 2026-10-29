# Alikhan Zhaxylyk — QA & Technical Support Portfolio

[![Portfolio integrity](https://github.com/saltsnuff2204/qa-engineering-portfolio/actions/workflows/validate.yml/badge.svg)](https://github.com/saltsnuff2204/qa-engineering-portfolio/actions/workflows/validate.yml)

Junior QA Engineer and Technical Support specialist based in Astana, Kazakhstan. I work at the point where a user request becomes a clear scenario or task for a product team, then verify the result after a change.

**Focus:** web and API QA, technical support, requirement clarification, retesting, and AI/video-incident validation.
**Education:** Software Engineering, Astana IT University — expected 2028.

> This repository deliberately separates real, anonymized work from learning material. It contains no employer data, internal URLs, credentials, source videos, or personal information.

## Start here

| Case study | What it shows |
| --- | --- |
| [BestYs — from a user request to retest](case-studies/bestys-request-to-retest.md) | Support request → reproduction → clear handoff → QA verification → retest |
| [AMAN — AI incident validation](case-studies/aman-ai-incident-validation.md) | True-positive / false-positive analysis, admin-panel checks, incident and notification scenarios |
| [Quiz → Curriculum transfer](case-studies/quiz-curriculum-transfer.md) | Translating a product request into acceptance criteria, mapping-risk analysis, and validation scenarios |
| [Anonymized stale-notification report](case-studies/anonymized-stale-notification-bug.md) | A public-safe example of documenting a scheduling risk for a development team |

## How I approach a task

1. Clarify the user scenario, business rule, and expected outcome.
2. Reproduce the issue or turn the request into acceptance criteria.
3. Check the relevant UI, API, data, notification, and edge-case behaviour.
4. Describe findings so that a developer or product teammate can act on them.
5. Retest the implemented change and report the verified result.

## Real work vs. learning material

| Label | Meaning |
| --- | --- |
| `[SANITIZED WORK CASE]` | An anonymized description of real responsibilities and workflows. It deliberately omits client data and internal evidence. |
| `[LEARNING PROJECT]` | A local educational project or a QA artefact made for hands-on practice. It is not presented as a production system. |

Read the [case-study guide](case-studies/README.md) for the evidence and confidentiality rules used here.

## Learning project: Restaurant Menu Manager

`Restaurant Menu Manager` is a local full-stack learning application used as a **system under test**. It is intentionally separate from the work case studies above.

- Source project: [Java 17 + PostgreSQL + React dashboard](https://github.com/saltsnuff2204/restaurant-menu-manager)
- [Test plan](test-plan/restaurant-menu-test-plan.md)
- [Functional test design](test-cases/functional-test-cases.md)
- [Smoke-test charter and checklist](checklists/web-smoke-checklist.md)
- [Example issue documentation style](bug-reports/sample-bug-reports.md)
- [Known local-only limitations](known-limitations.md)
- [Minimal executable Postman smoke set](api/restaurant-menu.postman_collection.json)
- [SQL data-validation queries](sql/data-validation.sql)
- [Exploratory test charter](test-charters/restaurant-menu-exploratory-charter.md)

The test cases and charters are **design artefacts**, not a claim that every scenario has passed. Actual run evidence belongs in [`test-runs/`](test-runs/README.md) only after it is captured against a disposable local environment.

## Additional engineering coursework

- [Java Restaurant OOP](https://github.com/saltsnuff2204/java-restaurant-oop) — Java, Maven, OOP, collections, `BigDecimal`, and JUnit 5.
- [Restaurant Menu Manager](https://github.com/saltsnuff2204/restaurant-menu-manager) — the local system under test for this portfolio.

These repositories are shown as learning projects; they are not presented as client deliverables or production systems.

## Toolkit

`Jira` · `Trello` · `TestRail` · `Postman` · `Swagger` · `Chrome DevTools` · `SQL` · `Git`

- Manual, functional, smoke, regression, exploratory, and UI testing
- REST API inspection and request/response validation
- Browser and network investigation with Chrome DevTools
- SQL-based data checks on disposable test data
- Clear defect documentation, task handoff, and retesting in Agile teams

## Verification and integrity

The badge above reports **portfolio integrity**, not an end-to-end product test run. The workflow validates:

- Postman collection JSON;
- required public-safe case-study structure;
- local Markdown links in this repository;
- basic patterns that help prevent accidental publication of tokens.

Run the same checks locally:

```powershell
py -3 scripts/validate_portfolio.py
```

On macOS or Linux, use `python3 scripts/validate_portfolio.py`.

To exercise the API collection, start the local Restaurant Menu Manager with a disposable PostgreSQL database, then import the collection in Postman or run it with Newman. Do not run it against a production system.

## Confidentiality

Work case studies intentionally explain the method and outcome without disclosing data that belongs to an employer, client, participant, or colleague. See [evidence policy](evidence/README.md) before adding screenshots, logs, or exported test runs.
