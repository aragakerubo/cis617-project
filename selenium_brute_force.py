from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# AWS login URL (IAM user)
AWS_LOGIN_URL = "https://signin.aws.amazon.com/console"

# Test users
users = ["alice", "bob", "charlie", "diana"]
account_id_or_alias = "your-account-alias-or-id"  # Replace this

# Set password (intentionally incorrect to simulate failed login)
password = "WrongPassword123!"

# Setup driver
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
driver = webdriver.Chrome(options=options)

for username in users:
    try:
        driver.get(AWS_LOGIN_URL)
        time.sleep(2)

        # Click on 'IAM user?' to show account alias field
        driver.find_element(By.ID, "iam_user_link").click()
        time.sleep(1)

        # Enter account alias or ID
        driver.find_element(By.ID, "account").send_keys(account_id_or_alias)
        driver.find_element(By.ID, "next_button").click()
        time.sleep(2)

        # Enter IAM username
        driver.find_element(By.ID, "username").send_keys(username)

        # Enter password
        driver.find_element(By.ID, "password").send_keys(password)

        # Submit the form
        driver.find_element(By.ID, "signin_button").click()
        time.sleep(3)

        # Screenshot the result
        driver.save_screenshot(f"{username}_login_attempt.png")

        print(f"Attempted login for: {username}")

    except Exception as e:
        print(f"Error with {username}: {e}")

    # Pause before next attempt
    time.sleep(2)

driver.quit()

