# 🛡️ API Governance & Security Linter

A professional Python-based CLI tool designed to automate the governance and security audit of OpenAPI specifications. 

## 🏛️ Project Vision
In high-stakes enterprise environments (like Finance and Healthcare), API consistency and security are non-negotiable. This tool was built to bridge the gap between "working code" and "safe, compliant infrastructure" by enforcing "Safety by Design" principles.

## 🚀 Key Features
- **Structural Validation:** Ensures strict adherence to OpenAPI 3.0 standards.
- **Security Audit:** Flags insecure `http` protocols in server configurations to prevent unencrypted data transmission.
- **Governance Enforcement:** - Mandatory `description` tags for auditability and compliance.
  - Mandatory `operationId` for consistent SDK generation and Developer Experience (DX).
- **CLI-Native:** Designed for seamless integration into CI/CD pipelines.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Libraries:** PyYAML, openapi-spec-validator
- **Architecture:** Modular CLI (argparse)

## 💻 Installation & Usage
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
