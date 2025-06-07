# app_health_checker.py

import requests

def check_app_health(url):
    try:
        response = requests.get(url, timeout=5)
        status_code = response.status_code

        if status_code == 200:
            print(f"✅ Application is UP (Status Code: {status_code})")
        else:
            print(f"❌ Application might be DOWN (Status Code: {status_code})")
    except requests.RequestException as e:
        print(f"❌ ERROR: Unable to connect to the application - {e}")

if __name__ == "__main__":
    # Example: OrangeHRM demo site
    check_app_health("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
