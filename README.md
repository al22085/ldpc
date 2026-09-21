# Execution and Repository Policy

This repository is intended for public access. All committed content must be
suitable for public disclosure.

## Execution Environment

Execute research programs, tests, benchmarks, and simulations exclusively on the
laboratory server. Local computers are used for source editing, static review,
and Git operations. Do not execute research code locally, including through WSL
or containers.

The current script requires Python 3 and uses only the Python standard library.
On the laboratory server, run the following command from the repository root:

```sh
python3 ldpc_bp_one_round.py
```

Maintain server connection details, credentials, and environment-specific
configuration outside the repository.

## Public Disclosure and Confidentiality

- Do not commit credentials, access tokens, passwords, private keys, or other
  confidential information.
- Do not disclose private server addresses, account identifiers, internal paths,
  restricted datasets, or unpublished research materials without authorization
  for public release.
- Review source files, configuration, logs, results, and Git diffs before
  committing them. Ignore rules do not replace this review.
- Use synthetic values or clearly identified placeholders in configuration
  examples.

## Language

Use English for documentation, comments, docstrings, diagnostic messages, and
new identifiers. Use precise, formal terminology appropriate for scientific
research and established terminology from the relevant technical literature.

Repository-specific instructions for automated coding agents are documented in
`AGENTS.md`.
