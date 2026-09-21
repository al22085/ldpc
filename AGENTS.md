# Repository Instructions

These instructions apply to all files in this repository.

## Execution and Validation

- Execute research code, tests, benchmarks, and simulations only on the
  laboratory server. Do not execute them on a local computer, including through
  WSL or containers.
- Local work may include editing, text searches, static source review, and Git
  operations.
- If the laboratory server is unavailable, report that runtime validation was
  not performed. Do not substitute local execution or claim that tests passed.
- Do not install packages or change the local execution environment as a
  workaround for unavailable server access.

## Confidentiality and Security

- Treat all committed content and commit messages as publicly accessible.
- Never record confidential information in this repository. This includes
  credentials, access tokens, passwords, private keys, private server addresses,
  private account identifiers, and internal filesystem paths.
- Keep connection details and environment-specific configuration outside the
  repository. Use clearly identified, non-sensitive placeholders in examples.
- Do not include restricted datasets, confidential logs, personal information,
  or unpublished research materials unless their public release is explicitly
  authorized.
- Inspect the complete staged diff and the staged file list before each commit.
  Check generated files and logs as well as source code. Do not rely solely on
  `.gitignore`, which does not remove files already tracked by Git.
- If a credential is exposed, stop further disclosure and notify the repository
  owner. Do not repeat the value in reports. Removing it from the current file
  does not remove it from Git history; coordinate credential revocation and any
  history remediation with the owner.
- Do not publish or push changes without explicit authorization.

## Language and Research Integrity

- Write documentation, comments, docstrings, diagnostic messages, new
  identifiers, and commit messages in English.
- Use formal scientific terminology and standard terms for coding theory,
  probability, and numerical computation.
- Preserve mathematical definitions, numerical values, algorithmic behavior,
  and output structure when translating existing text.
- Do not fabricate results or describe unexecuted validation as successful.
- Make only the changes required by the task and preserve unrelated user work.
