# Functional Test Design — Restaurant Menu Manager

> `[LEARNING PROJECT]` · Test design, not an execution report

The scenarios below define intended coverage for a disposable local environment. Every row is marked **Not run** until an executed test record is added under [`test-runs/`](../test-runs/README.md).

| ID | Type | Priority | Scenario | Steps and data | Expected result | Execution status | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RM-001 | API smoke | Critical | API health check | Send `GET /api/health` | `200 OK`; JSON contains `status: ok` | Not run | — |
| RM-002 | UI/API smoke | High | Load menu | Open dashboard with API and DB running | Loading state clears; table matches `GET /api/menu`; no console error | Not run | — |
| RM-003 | API/data | High | Create a valid dish | Name `Mushroom risotto`; price `12.50`; category `MAIN_DISH`; vegetarian enabled | `201 Created`; generated ID returned; item appears after refresh and persists in DB | Not run | — |
| RM-004 | API/data | High | Create a valid drink | Name `Iced tea`; price `3.25`; category `DRINK`; has ice enabled | `201 Created`; item appears with drink details and persists in DB | Not run | — |
| RM-005 | Validation | High | Reject blank name | Submit spaces as name with valid price | UI blocks submission or API returns `400`; no row inserted | Not run | — |
| RM-006 | Validation | High | Reject zero and negative price | Test `0`, `-1`, and `-0.01` | Validation message shown or `400`; no row inserted | Not run | — |
| RM-007 | Boundary/data | Medium | Price boundary and precision | Test `0.01`, `12.50`, and a very large finite value | Valid values follow documented rules; displayed value uses two decimals; DB value is consistent | Not run | — |
| RM-008 | API validation | High | Reject invalid category/type pair | POST a drink with category `DESSERT` | `400 Bad Request`; error explains that drinks require `DRINK` | Not run | — |
| RM-009 | UI functional | Medium | Search is case-insensitive | Create `Caesar Salad`; search `caesar`, `CAESAR`, and partial `sal` | Same matching item is displayed in all cases | Not run | — |
| RM-010 | UI functional | Medium | Filter by category | Seed items in all categories; select each filter | Only matching rows display; total stored count remains unchanged | Not run | — |
| RM-011 | API/UI/data | High | Delete existing item | Confirm deletion of a known ID | `204 No Content`; row disappears from UI and DB | Not run | — |
| RM-012 | API validation | High | Delete missing item | Send `DELETE /api/menu/999999` | `404 Not Found`; JSON error returned; other data unchanged | Not run | — |
| RM-013 | API validation | High | Reject malformed ID | Send delete request with `abc`, `0`, and `-1` | `400 Bad Request`; database remains unchanged | Not run | — |
| RM-014 | API validation | High | Invalid JSON body | POST malformed JSON | `400 Bad Request`; safe JSON error; no stack trace or row inserted | Not run | — |
| RM-015 | Resilience | High | API unavailable | Stop backend and refresh dashboard | Page remains usable; clear failure message appears; no uncaught console exception | Not run | — |
| RM-016 | Responsive UI | Medium | Narrow viewport smoke | Test at `390 × 844` viewport | Controls remain reachable; form and table do not overlap; horizontal scrolling is usable where required | Not run | — |

## Suggested regression subset

After a backend, database, or form change, execute RM-001, RM-002, RM-003, RM-004, RM-005, RM-008, RM-011, RM-014, and RM-015. Record the actual scope and result before calling the subset passed.
