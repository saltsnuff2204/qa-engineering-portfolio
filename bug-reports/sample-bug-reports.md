# Example Issue Documentation Style — Restaurant Menu Manager

> `[LEARNING PROJECT]` · Documentation example, not a production-defect claim

This page demonstrates how I structure an issue for a small local learning application. It is separate from the anonymized work-case report in [`case-studies/`](../case-studies/anonymized-stale-notification-bug.md). The local application's public-deployment limits are documented in [known limitations](../known-limitations.md), not presented as an active demo failure.

## LAB-001 — UI hides a safe API validation message

- **Type:** Usability / error-feedback improvement
- **Severity:** Minor
- **Priority:** Medium
- **Environment:** Local React dashboard and Java REST API
- **Status:** Open learning-project improvement; no release claim

### Preconditions

The API returns a structured validation response such as `{"error":"Name is required"}` for an invalid request.

### Steps to reproduce

1. Open the local dashboard with the API running.
2. Submit data that passes or bypasses client validation but fails server validation.
3. Observe the message displayed by the UI.

### Actual result

The current UI can show a generic `Failed to add item` message and discard the safe validation text returned by the API.

### Expected result

The UI should display a safe, specific validation message returned by the API so the user can correct the input, with a generic fallback if no safe message exists.

### Evidence needed for an executed run

- Request and response from the browser Network panel.
- Screenshot of the visible UI message.
- Exact local application revision and test data note.

### Recommendation

Parse the JSON error body for non-2xx responses and display its safe `error` field, with a generic fallback. Record a verified fix and retest in [`test-runs/`](../test-runs/README.md) before presenting it as resolved.
