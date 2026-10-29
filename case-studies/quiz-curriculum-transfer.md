# Exam Transfer: Making Sure Exams Move Correctly

> `[SANITIZED WORK CASE]` · Requirement clarification, QA, and retest support

## Context and confidentiality

This case describes an EdTech transfer workflow that connects a source product, quizzes/exams, and a target curriculum. Product names, IDs, learner data, and internal implementation details are intentionally omitted.

## User problem

A transfer must preserve the relationship between the target product, its quizzes, and the curriculum that gives those quizzes meaning. A missing, ambiguous, or incorrectly attached curriculum can leave an exam visible but unusable or wrongly categorized.

## My role

I collected the request context, turned it into a checkable scenario, highlighted risks for the development team, and verified the relevant behaviour after changes. I did not present myself as the product owner or project manager.

## Acceptance criteria used for QA discussion

| Scenario | Expected product behaviour |
| --- | --- |
| One unambiguous matching curriculum exists | Attach the matching curriculum to the target product and preserve the quiz relationship. |
| No suitable curriculum exists | The requested improvement is to create a curriculum and attach it to the target product in a traceable state. |
| More than one plausible curriculum exists | Do not silently choose one; surface a clear mapping decision or a safe unresolved state. |
| Quiz/exam moves with questions | Preserve the intended category, grade/subject context where applicable, and question count. |
| Notifications exist for the transfer-related flow | Avoid stale or duplicated notification state after an update. |

## QA scenarios I used

- Source product and target product have compatible mappings.
- A target has no curriculum and needs an explicit create-and-attach path.
- A target has ambiguous curriculum candidates.
- A transferred quiz remains connected to the intended curriculum and category.
- Counts and visible metadata remain consistent after the transfer.
- Notifications are refreshed or clearly reported when a date or transfer condition changes.

## Example risk reported to the team

One risk was a stale notification: an already scheduled event could retain an earlier schedule after the underlying date changed. The public-safe report is available in [the anonymized example](anonymized-stale-notification-bug.md).

## How I handed off and retested

I described the user scenario, expected result, reproduction or setup conditions, and the specific mapping or notification risk. After a change, I repeated the affected flow and checked nearby paths rather than assuming the visible happy path was enough.

## Tools and boundaries

`Jira` · `Trello` · manual UI testing · Chrome DevTools · API inspection · regression checks.

Internal tickets, customer data, curriculum IDs, screenshots, and release outcomes are not public. No performance numbers or release-success metrics are claimed here.
