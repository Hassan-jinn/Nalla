import os
import sys
import requests
import base64
import logging

logging.basicConfig(filename='key_verification.log', level=logging.INFO)

def verify_key(key):
    pat = os.getenv("GITHUB_PAT")
    if not pat:
        print("Error: GitHub PAT not configured")
        sys.exit(1)

    url = "https://api.github.com/repos/Hassan-jinn/Approval/contents/Apv.txt"
    headers = {
        "Authorization": f"token {pat}",
        "Accept": "application/vnd.github.v3+json"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            content = base64.b64decode(response.json()['content']).decode('utf-8').strip()
            if key in content:
                print("Key verified successfully")
                logging.info(f"Key {key} verified")
                sys.exit(0)  # Success
            else:
                print("Key not approved")
                logging.warning(f"Key {key} not found")
                sys.exit(1)  # Failure
        else:
            print(f"API error: {response.status_code}")
            logging.error(f"API error: {response.status_code}")
            sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        logging.error(f"Error verifying key: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    key = os.getenv("INPUT_KEY")
    verify_key(key)
