# Restaurant Menu Manager Test Plan

> `[LEARNING PROJECT]` · Planning artefact, not a release sign-off

This plan defines the intended local test scope. An executed run must be recorded separately in [`test-runs/`](../test-runs/README.md) before any exit criterion is treated as met.

## Objective

Verify that users can reliably view, create, search, filter, and delete restaurant menu items through the React interface and Java REST API, while PostgreSQL stores valid and consistent records.

## Scope

### In scope

- API health and availability
- Menu retrieval and empty-state behaviour
- Dish and drink creation
- Required-field, price, category, and payload validation
- Search and category filtering
- Deletion and confirmation flow
- UI feedback when the API is unavailable
- Persistence and database constraints
- Responsive layout smoke coverage

### Out of scope

- Authentication and role-based access, which are not implemented
- Performance, load, and endurance testing
- Production deployment and browser support beyond the stated test matrix
- Editing, pagination, and audit logging, which are not implemented

## Test approach

| Area | Approach |
| --- | --- |
| Functional | Positive and negative end-to-end scenarios through UI and API |
| Regression | Re-run critical create, read, filter, and delete flows after changes |
| API | Validate status codes, JSON schema basics, headers, and error responses |
| Database | Compare API results with PostgreSQL records and constraint rules |
| UI/UX | Check states, labels, validation feedback, keyboard flow, and responsiveness |
| Compatibility | Smoke-test current Chrome and one mobile viewport |

## Test environment

- Java 17 REST API on `http://localhost:4567`
- React/Vite dashboard on `http://localhost:5173`
- Local PostgreSQL test database with non-production credentials
- Chrome DevTools Network and Console panels
- Postman collection from this repository

## Entry criteria

- Backend and frontend builds pass
- Test database is available and contains no production data
- Required environment variables are configured
- API health endpoint returns `200 OK`

## Exit criteria

- All critical and high-priority cases executed
- No open blocker or critical defect
- Core smoke suite passes
- Known limitations and unresolved defects documented
- Test data cleaned or retained intentionally for investigation

## Key risks

- Write and delete endpoints have no authentication and must remain local-only
- A database outage blocks most functional flows
- Client errors currently use generic messages, which can slow diagnosis
- Automated backend tests are limited, increasing regression risk

