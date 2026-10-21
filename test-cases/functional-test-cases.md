# Functional Test Cases

| ID | Priority | Scenario | Steps and data | Expected result |
| --- | --- | --- | --- | --- |
| RM-001 | Critical | API health check | Send `GET /api/health` | `200 OK`; JSON contains `status: ok` |
| RM-002 | High | Load menu | Open dashboard with API and DB running | Loading state clears; table matches `GET /api/menu`; no console error |
| RM-003 | High | Create a valid dish | Name `Mushroom risotto`; price `12.50`; category `MAIN_DISH`; vegetarian enabled | `201 Created`; generated ID returned; item appears after refresh and persists in DB |
| RM-004 | High | Create a valid drink | Name `Iced tea`; price `3.25`; category `DRINK`; has ice enabled | `201 Created`; item appears with drink details and persists in DB |
| RM-005 | High | Reject blank name | Submit spaces as name with valid price | UI blocks submission or API returns `400`; no row inserted |
| RM-006 | High | Reject zero and negative price | Test `0`, `-1`, and `-0.01` | Validation message shown or `400`; no row inserted |
| RM-007 | Medium | Price boundary and precision | Test `0.01`, `12.50`, and a very large finite value | Valid values follow documented rules; displayed value uses two decimals; DB value is consistent |
| RM-008 | High | Reject invalid category/type pair | POST a drink with category `DESSERT` | `400 Bad Request`; error explains that drinks require `DRINK` |
| RM-009 | Medium | Search is case-insensitive | Create `Caesar Salad`; search `caesar`, `CAESAR`, and partial `sal` | Same matching item is displayed in all cases |
| RM-010 | Medium | Filter by category | Seed items in all categories; select each filter | Only matching rows display; total stored count remains unchanged |
| RM-011 | High | Delete existing item | Confirm deletion of a known ID | `204 No Content`; row disappears from UI and DB |
| RM-012 | High | Delete missing item | Send `DELETE /api/menu/999999` | `404 Not Found`; JSON error returned; other data unchanged |
| RM-013 | High | Reject malformed ID | Send delete request with `abc`, `0`, and `-1` | `400 Bad Request`; database remains unchanged |
| RM-014 | High | Invalid JSON body | POST malformed JSON | `400 Bad Request`; safe JSON error; no stack trace or row inserted |
| RM-015 | High | API unavailable | Stop backend and refresh dashboard | Page remains usable; clear failure message appears; no uncaught console exception |
| RM-016 | Medium | Mobile smoke | Test at 390×844 viewport | Controls remain reachable; form and table do not overlap; horizontal scrolling is usable where required |

## Suggested regression subset

Run RM-001, RM-002, RM-003, RM-004, RM-005, RM-008, RM-011, RM-014, and RM-015 after any backend, database, or form change.

