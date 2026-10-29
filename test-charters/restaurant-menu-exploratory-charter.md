# Exploratory Test Charter — Restaurant Menu Manager

> `[LEARNING PROJECT]` · Test-design charter, not an execution report

## Mission

Explore the Restaurant Menu Manager's critical local user journey from API availability through creating, locating, and deleting menu items. Focus on failure handling, data integrity, and local-demo readiness.

## Areas to explore

- Health and menu endpoints.
- Dish and drink creation.
- Required fields, price boundaries, malformed JSON, and invalid category/type pairs.
- Search and category filtering.
- Deletion, missing IDs, and malformed IDs.
- API outage behaviour.
- PostgreSQL record consistency on a disposable test database.
- Chrome desktop and a narrow mobile viewport as separate checks.

## Risk questions

| Risk area | Question to answer during an executed session |
| --- | --- |
| Validation | Does the UI preserve a safe, useful server validation message? |
| Data integrity | Can invalid category/type combinations or incomplete records reach the database? |
| Error handling | Does the UI remain understandable if the API is unavailable or returns malformed input errors? |
| Delete flow | Does the requested item disappear only after confirmation, while invalid IDs remain safe? |
| Local security scope | Are the local-only limitations clearly documented before a demo? |

## Exit criteria for a recorded run

- The run has a date, environment, test-data note, and a Pass/Fail/Blocked summary.
- Observations are linked to safe evidence or explicitly marked as not publishable.
- Any release recommendation distinguishes the local learning demo from a production deployment.

## Output

Store an executed record in [`test-runs/`](../test-runs/README.md). Do not convert this charter into a passing test report without a real run.
