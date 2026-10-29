# Web Smoke-Test Charter and Checklist

> `[LEARNING PROJECT]` · Planned checklist, not a recorded pass result

## Run record

| Field | Value |
| --- | --- |
| Date | Not run |
| Tester | Not run |
| Application revision | Not run |
| Environment and test data | Disposable local environment required |
| Overall result | Not run |
| Evidence | Add a link under [`test-runs/`](../test-runs/README.md) after execution |

## Environment

- [ ] Backend starts without exposing credentials or stack traces
- [ ] `GET /api/health` returns `200 OK`
- [ ] Frontend starts and loads without blocking console errors
- [ ] Database connection uses a dedicated test account

## Core flow

- [ ] Menu list loads
- [ ] Empty menu state is readable
- [ ] Valid dish can be created
- [ ] Valid drink can be created
- [ ] Search returns the expected item
- [ ] Category filter narrows results correctly
- [ ] Delete confirmation appears
- [ ] Confirmed deletion removes the intended item
- [ ] Cancelled deletion leaves data unchanged

## Validation and failure handling

- [ ] Blank name is rejected
- [ ] Zero and negative prices are rejected
- [ ] Invalid JSON receives a safe `400` response
- [ ] Missing item deletion receives `404`
- [ ] API outage displays a clear UI error
- [ ] No secret, SQL error, or stack trace appears in the browser response

## UI and compatibility

- [ ] Keyboard focus reaches all interactive controls
- [ ] Labels and validation messages are understandable
- [ ] Current Chrome desktop flow
- [ ] Mobile viewport has no overlapping controls
- [ ] Table remains usable on a narrow screen

## Execution rule

Check an item only during a real run. If the run is blocked, record the blocker and keep the item unchecked rather than treating the checklist as evidence of a pass.

