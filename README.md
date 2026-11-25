# test-deploynaut

Testing product-os/deploynaut with my own changes.

This repo is also set up to reproduce the [GHAS + merge queue required-check workaround](https://ewega.github.io/site/github/tutorial/2023/12/04/enabling-ghas-merge-queue/).

## Merge queue + CodeQL

GitHub's **Code scanning results / CodeQL** check does not report on merge-queue groups. If you make that check required, the queue waits forever. These workflows use a substitute Actions job instead.

### After you create the GitHub org

1. Put this repo in an **organization** (merge queue is not available on personal accounts).
2. Use a **public** repo, or GitHub Enterprise Cloud for a private repo.
3. Enable **GitHub Actions** and **code scanning**. Prefer this advanced workflow over Default setup so `merge_group` is included. If Default setup is already on, turn it off to avoid duplicate CodeQL runs.
4. Protect `main` with an exact branch name (no `*`). Enable **Require merge queue**.
5. Required status checks:
   - **Check CodeQL Status** — PR-only substitute for the GHAS CodeQL results check
   - **tests** — runs on both pull requests and merge groups
   - Do **not** require **Code scanning results / CodeQL** or **CodeQL**
6. Optional: under Code scanning, fail the check when alerts of **error** (or higher) are found, so the `codeql-failure` branch actually fails **Check CodeQL Status**.

### Test branches

| Branch | Purpose |
| --- | --- |
| `main` | Clean hello-world Python; workflows live here |
| `codeql-failure` | Intentional command-injection sample so CodeQL reports a finding |

Open a PR from `codeql-failure` into `main` to exercise the failing path. Open a PR that only changes a comment to exercise a passing path through the merge queue.
