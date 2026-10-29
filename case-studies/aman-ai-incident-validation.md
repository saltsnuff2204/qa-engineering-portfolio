# AMAN: Testing AI Video Alerts

> `[SANITIZED WORK CASE]` · QA Tester

## Context and confidentiality

I test a system that uses computer vision to identify incidents in video streams and surface them in an administrative interface. The product uses real operational data, so this case deliberately contains no source video, event identifiers, confidence values, internal URLs, or client information.

## My role

My responsibility is QA validation of user-facing and operational behaviour. I do **not** claim to train or tune the ML model. I evaluate how detection results and incident workflows appear to the product's users and report mismatches to development and ML teammates.

## What I check

| Area | QA focus |
| --- | --- |
| Incident detection | Whether a visible event is classified as an incident or a non-incident; true-positive and false-positive review |
| Admin panel | Incident list, details, status, filtering, and the connection between an incident and its video context |
| Video flows | Availability of the relevant stream or fragment and consistency of the displayed incident information |
| Notifications | Whether the expected notification scenario is triggered, represented correctly, and remains understandable to an operator |
| Retest | Whether a reported issue is resolved without breaking adjacent admin or notification flows |

## How I document a mismatch

1. Preserve the relevant context without copying restricted video or user data into a public channel.
2. State the expected user-visible behaviour and the actual result.
3. Classify whether the scenario is a candidate true positive, false positive, or a product/UI problem that needs separate investigation.
4. Share a concise report with the development or ML team and retest the resulting change when it is available.

## Tools and collaboration

`Jira` · `Trello` · admin-interface testing · video-incident review · notification scenarios · functional and regression checks.

## Evidence boundary

The original records are in employer systems and are not public. This page shows the testing method and role scope without inventing model-quality metrics or publishing confidential evidence.
