# Sample Bug Reports

These reports demonstrate documentation style using a learning application. They contain no production or employer data.

## BUG-001 Live dashboard cannot load menu data

- **Severity:** Major
- **Priority:** High
- **Environment:** Public legacy frontend deployment; Chrome desktop
- **Status:** Identified during portfolio audit; deployment removed from portfolio claims

### Preconditions

The legacy frontend is publicly reachable.

### Steps to reproduce

1. Open the legacy dashboard.
2. Wait for the initial menu request.
3. Inspect the Network panel request to `/api/menu`.

### Actual result

The interface loads, but the menu request returns `404`. The page shows `Failed to load menu`, so create, list, and delete flows are unavailable.

### Expected result

The frontend should call a reachable backend and receive `200 OK` with a JSON array, or the deployment should clearly state that it is a static preview.

### Evidence to capture

- Network request URL, status, response body, and timing
- Console output
- Screenshot of the visible error state

### Recommendation

Deploy the API and configure the frontend base URL per environment. Add a deployment smoke check for `/api/health` and `/api/menu`.

## BUG-002 Generic client error hides API validation details

- **Severity:** Minor
- **Priority:** Medium
- **Environment:** Local dashboard and API
- **Status:** Open usability improvement

### Preconditions

The API returns a structured validation error such as `{"error":"Name is required"}`.

### Steps to reproduce

1. Open the dashboard.
2. Submit data that passes or bypasses client validation but fails server validation.
3. Observe the error displayed by the UI.

### Actual result

The UI shows only `Failed to add item` and discards the API error message.

### Expected result

The UI should display a safe, specific message returned by the API so the user can correct the input.

### Recommendation

Parse the JSON error body for non-2xx responses and display its safe `error` field, with a generic fallback.

## BUG-003 Unauthenticated delete route is unsafe for public deployment

- **Severity:** Critical for public deployment
- **Priority:** High
- **Environment:** Java REST API
- **Status:** Known limitation; local-only use documented

### Steps to reproduce

1. Obtain any valid menu item ID.
2. Send `DELETE /api/menu/{id}` without authentication.

### Actual result

The item can be deleted without identity or permission checks.

### Expected result

Public deployments should require authenticated, authorised access to destructive routes.

### Recommendation

Keep the application local-only until authentication, role checks, CSRF/CORS policy, and audit logging are implemented.

