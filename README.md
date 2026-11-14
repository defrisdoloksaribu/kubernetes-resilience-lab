# Kubernetes CI

This workflow verifies that a fresh deployment can reach two Ready replicas and serve a successful request through its internal Service. It uses a minimal Python HTTP fixture with the source, Dockerfile, and manifests in this repository.

The CI fixture is not the original API image used for the Windows lab. The GitHub-hosted runner builds the fixture from source and creates its own disposable kind cluster. It does not import a local image archive, access the Windows cluster, or publish a deployment.

## Install in the repository

Copy the contents of the ZIP to the repository root. Keep the existing lab's files, including `k8s/app.yaml`, `k8s/hpa.yaml`, and `v2/`, where they are. Commit the new files in `.github/workflows/` and `ci/` together. A push to `main`, a pull request targeting `main`, or a manual run triggers the workflow.

In the repository, open **Actions → Kubernetes CI → Deploy and verify on kind**. Check these results:

| Step | Expected evidence |
| --- | --- |
| Build fixture image from source | `resilience-ci-api:ci` built from `ci/app`. |
| Deploy and wait for two ready replicas | Deployment `resilience-api` shows `2/2`. |
| Smoke test API through Service | `HTTP 200 {'status': 'running', 'version': 'ci'}`. |

The CI smoke test does not rerun the Windows lab's self-healing, rolling update, rollback, or HPA experiments. Those are separate results.
