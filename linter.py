import yaml
import argparse
import sys
from openapi_spec_validator import validate_spec

def lint_file(file_path: str):
    """
    Automates structural and security audits for OpenAPI specifications.
    Enforces 'Safety by Design' through custom governance rules.
    """
    try:
        with open(file_path, 'r') as file:
            spec = yaml.safe_load(file)
    except FileNotFoundError:
        print(f"❌ Error: File '{file_path}' not found.")
        sys.exit(1)

    # Validate against official OpenAPI 3.0 structural standards
    try:
        validate_spec(spec)
    except Exception as e:
        print(f"❌ Structural Validation Failed: {e}")
        return

    violations = []

    # SECURITY: Prevent unencrypted data transmission
    servers = spec.get('servers', [])
    for server in servers:
        url = server.get('url', '')
        if url.startswith('http://'):
            violations.append(f"SECURITY: Insecure protocol detected ({url}). HTTPS required.")

    # GOVERNANCE: Ensure auditability and Developer Experience (DX)
    paths = spec.get('paths', {})
    for path, methods in paths.items():
        for method, details in methods.items():
            if 'description' not in details:
                violations.append(f"GOVERNANCE: Missing 'description' in {method.upper()} {path}")
            
            if 'operationId' not in details:
                violations.append(f"DX: Missing 'operationId' in {method.upper()} {path}")

    # Final Output Report
    if not violations:
        print("🚀 Success: API Specification meets all Enterprise Standards.")
    else:
        print(f"⚠️  Found {len(violations)} Violations:")
        for v in violations:
            print(f"  - {v}")

def main():
    """CLI Entrypoint for the linter tool."""
    parser = argparse.ArgumentParser(description="API Governance & Security Linter")
    parser.add_argument("filename", help="Path to the OpenAPI YAML file")
    
    args = parser.parse_args()
    lint_file(args.filename)

if __name__ == "__main__":
    main()