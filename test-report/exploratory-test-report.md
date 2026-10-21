# Exploratory Test Report

## Session charter

Explore the Restaurant Menu Manager's critical user journey from API availability through creating, locating, and deleting menu items. Focus on failure handling, data integrity, and deployment readiness.

## Coverage

- Health and menu endpoints
- Dish and drink creation
- Required fields, price boundaries, malformed JSON, and invalid category/type pairs
- Search and category filtering
- Deletion, missing IDs, and malformed IDs
- API outage behaviour
- PostgreSQL record consistency
- Desktop and mobile-layout smoke checks

## Findings

1. The legacy public frontend was reachable while `/api/menu` returned `404`, preventing the core workflow.
2. The refreshed local code removes hard-coded database credentials and validates key API inputs.
3. Client-side error handling still converts detailed API errors into generic messages.
4. Write and delete routes do not have authentication or authorisation and are unsuitable for public deployment.
5. Automated backend integration coverage remains a regression risk.

## Release recommendation

**Suitable for a local portfolio demonstration only.** Do not deploy publicly with write routes enabled until authentication, authorisation, safe CORS/CSRF handling, and audit logging are added. Before a local demo, pass the smoke checklist and verify the database contains only disposable test data.

## Recommended follow-up

- Add API integration tests for success and validation paths
- Surface safe server validation messages in the UI
- Add authenticated roles for create and delete operations
- Add automated deployment smoke checks
- Define a supported browser and mobile-device matrix

