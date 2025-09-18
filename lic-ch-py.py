import subprocess
import json
import os

def get_installed_packages():
    """Get a list of installed packages in the current Python environment."""
    result = subprocess.run(
        ["pip", "freeze"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    if result.returncode != 0:
        print("Error fetching installed packages.")
        return []
    return result.stdout.decode().splitlines()

def get_license_info():
    """Fetch license information for installed packages."""
    result = subprocess.run(
        ["pip-licenses", "--format", "json"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    if result.returncode != 0:
        print("Error fetching license information.")
        return []
    
    return json.loads(result.stdout.decode())

def display_licenses(licenses):
    """Display license information in a readable format."""
    for package in licenses:
        print(f"Package: {package['name']}")
        print(f"  Version: {package['version']}")
        print(f"  License: {package['license']}")
        print(f"  License File: {package.get('license_file', 'N/A')}")
        print("-" * 40)

def save_licenses_to_file(licenses, filename="licenses_report.json"):
    """Save the license report to a JSON file."""
    with open(filename, "w") as f:
        json.dump(licenses, f, indent=4)
    print(f"License information saved to {filename}")

if __name__ == "__main__":
    # Fetch and display license info for installed packages
    licenses = get_license_info()
    display_licenses(licenses)
    
    # Optionally save the report to a JSON file
    save_licenses_to_file(licenses)
