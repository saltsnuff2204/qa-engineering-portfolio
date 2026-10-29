# Known scope limitations — Restaurant Menu Manager

> `[LEARNING PROJECT]` · Local-only demo

The Restaurant Menu Manager is deliberately a local learning application. These are documented scope limitations, not production incidents or claims about an employer product.

## Deployment

There is no supported public deployment. A previous legacy frontend endpoint is not used as a demo or as portfolio evidence. The documented workflow is local only.

## Authentication and authorization

The create and delete endpoints have no authentication or authorization. They are suitable only for a disposable local demonstration and must not be exposed publicly.

## Execution evidence

The repository contains test design and a Postman smoke collection. It does not claim that every scenario has executed successfully. See [test-run records](test-runs/README.md) for the standard required before publishing a run summary.

## Future hardening

Before any public deployment, add authentication, authorization, safe CORS/CSRF handling, audit logging, and repeatable integration tests.
