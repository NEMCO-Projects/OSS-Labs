# before run this code should be install venv using apt intall python3-venv -y
# create .env using python3 -m venv .env
# activate .env using source .env/bin/activate
# install required python packages using pip install -r requirements.txt
# then run this code as python3 lic-ch-py.py


import subprocess
import json

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
        print(f"Package: {package['Name']}")
        print(f"  Version: {package['Version']}")
        print(f"  License: {package['License']}")
        print("-" * 40)

if __name__ == "__main__":
    licenses = get_license_info()
    display_licenses(licenses)
