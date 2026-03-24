![Build Status](https://github.com/iroussos25/prudential-linter/actions/workflows/lint.yml/badge.svg)
# 🛡️ API Governance & Security Linter

A Python CLI tool that audits OpenAPI 3.0 specifications for security and governance issues. Runs as a GitHub Actions CI/CD gate to block non-compliant API specs before they merge. 

## 🏛️ Project Vision
In regulated environments like finance and healthcare, API specs need to pass security checks before they ship. This tool automates that review so it happens on every pull request, not just when someone remembers to check.

## 🚀 Key Features
- **Structural Validation:** Ensures strict adherence to OpenAPI 3.0 standards.
- **Security Audit:** Flags insecure `http` protocols in server configurations to prevent unencrypted data transmission.
- **Governance Enforcement:** - Mandatory `description` tags for auditability and compliance.
  - Mandatory `operationId` for consistent SDK generation and Developer Experience (DX).
- **CLI-Native:** Designed for seamless integration into CI/CD pipelines.

  ## How it works

1. A developer opens a PR that includes an OpenAPI spec (YAML)
2. GitHub Actions triggers the linter automatically
3. The linter validates structure (OpenAPI 3.0 compliance), checks for insecure protocols (http instead of https), and enforces governance rules (required descriptions, operation IDs)
4. If any check fails, the PR is blocked with a clear error message
5. The developer fixes the issue and pushes again

The repo includes both a valid and invalid example spec (`api_spec_valid.yaml` and `api_spec_invalid.yaml`) so you can see exactly what passes and what gets flagged.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Libraries:** PyYAML, openapi-spec-validator
- **Architecture:** Modular CLI (argparse)

## 💻 Installation & Usage
```bash
git clone https://github.com/iroussos25/prudential-linter.git
cd prudential-linter
pip install -r requirements.txt
python linter.py api_spec_valid.yaml    # should pass
python linter.py api_spec_invalid.yaml  # should fail with specific errors
```
