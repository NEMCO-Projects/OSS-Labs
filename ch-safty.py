import subprocess
import json

def check_vulnerabilities():
    """Check for vulnerabilities in installed packages."""
    result = subprocess.run(
        ["safety", "check", "--json"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    if result.returncode != 0:
        print("Error checking vulnerabilities.")
        return []
    
    return json.loads(result.stdout.decode())

def display_vulnerabilities(vulnerabilities):
    """Display vulnerability information in a readable format."""
    if not vulnerabilities:
        print("No vulnerabilities found.")
        return
    
    for vuln in vulnerabilities:
        print(f"Package: {vuln['package_name']}")
        print(f"  Severity: {vuln['severity']}")
        print(f"  Vulnerability: {vuln['description']}")
        print(f"  Advisory: {vuln['advisory_url']}")
        print("-" * 40)

def save_vulnerabilities_to_file(vulnerabilities, filename="vulnerabilities_report.json"):
    """Save the vulnerability report to a JSON file."""
    with open(filename, "w") as f:
        json.dump(vulnerabilities, f, indent=4)
    print(f"Vulnerability information saved to {filename}")

if __name__ == "__main__":
    # Fetch and display vulnerabilities
    vulnerabilities = check_vulnerabilities()
    display_vulnerabilities(vulnerabilities)
    
    # Optionally save the report to a JSON file
    save_vulnerabilities_to_file(vulnerabilities)
