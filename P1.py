import os
import time
import hmac
import hashlib
import sys
import subprocess
import logging

# Auto-install dependencies
try:
    import requests
except ImportError:
    print("\033[1;31mInstalling requests package...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests

try:
    from dotenv import load_dotenv
except ImportError:
    print("\033[1;31mInstalling python-dotenv package...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "python-dotenv"])
    from dotenv import load_dotenv

logging.basicConfig(filename='key2.log', level=logging.INFO, format='%(asctime)s: %(message)s')
load_dotenv()

def get_device_fingerprint():
    try:
        result = subprocess.check_output(['termux-telephony-deviceinfo']).decode()
        return hashlib.sha256(result.encode()).hexdigest()
    except:
        return hashlib.sha256(f"{os.geteuid()}{os.getlogin()}".encode()).hexdigest()

def get_trigger_pat():
    pat = os.getenv("JINN_TRIGGER_PAT")
    if not pat:
        print("\033[1;33mJINN_TRIGGER_PAT not found in .env file.")
        pat = input("\033[1;32mPlease enter your JINN_TRIGGER_PAT: ")
        if not pat:
            print("\033[1;31mError: PAT is required!")
            logging.error("JINN_TRIGGER_PAT not provided")
            return None
    return pat

def trigger_workflow(key, repo="Hassan-jinn/Nalla", workflow_id="verify_key.yml"):
    pat = get_trigger_pat()
    if not pat:
        return False

    url = f"https://api.github.com/repos/{repo}/actions/workflows/{workflow_id}/dispatches"
    headers = {
        "Authorization": f"token {pat}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {"ref": "main", "inputs": {"key": key}}

    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 204:
            logging.info("Workflow triggered successfully")
            print(f"\033[1;32mVerification in progress, please wait...")
            return True
        else:
            logging.error(f"Workflow trigger failed: {response.status_code}")
            print(f"\033[1;31mWorkflow trigger failed: {response.status_code}")
            return False
    except Exception as e:
        logging.error(f"Error triggering workflow: {str(e)}")
        print(f"\033[1;31mError: {str(e)}")
        return False

def show_payment_options(key):
    print('\033[1;97m══════════════════════════════════════════════')
    print(f"\033[1;31m  YOUR KEY NOT APPROVED CONTACT ADMIN")
    print(f"\033[1;34m  07 DAY's APPROVE RS 100")
    print(f"\033[1;34m  15 DAY's APPROVE RS 200")
    print(f"\033[1;34m  30 DAY's APPROVE RS 350")
    print('\033[1;97m══════════════════════════════════════════════')
    print(f"\033[1;33m BINANCE ID : 936186916 ")
    print(f"\033[1;33m JAZZ CASH  : 0326 6189817 : M HASSAN")
    print(f"\033[1;33m EASYPAISA  : 0318 9713740 : M HASSAN")
    print(f"\033[1;31m Note : SEND PAYMENT PROOF ON WHATSAPP")
    print(f"\n\033[1;32m Your Login Key is  :\033[1;36m {key}")
    print(f"\n\033[1;33m [1] CONTACT WITH ME ON WHATSAPP")
    print(f"\033[1;33m [2] CONTACT WITH ME ON FACEBOOK")

    adi = input(f" \033[1;32m[•] CHOICE : ")
    if adi.lower() in ['a', '1', '01']:
        handle_whatsapp_contact(key)
    else:
        os.system('xdg-open https://www.facebook.com/profile.php?id=1623021375&mibextid=ZbWKwL')

def handle_whatsapp_contact(key):
    url_wa = "https://api.whatsapp.com/send?phone=+923189713740&text="
    tk = f"Approve%20OLD&RNDM%20Key:%20{key}"
    subprocess.check_output(["am", "start", url_wa + tk])
    time.sleep(2)

def key2():
    fingerprint = get_device_fingerprint()
    key = f"JINN-[{fingerprint}]-H"
    print(f" \033[1;32m TOOL IS PAID YOU NEED APPROVAL ")

    if trigger_workflow(key):
        # Temporary: Assuming success after trigger
        time.sleep(5)  # Wait for workflow to run
        print(f"\033[1;32mTOOL LOGIN SUCCESSFULLY")
    else:
        show_payment_options(key)

if __name__ == "__main__":
    key2()
