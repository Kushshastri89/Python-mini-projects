from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import os
from time import sleep

# Load environment variables from .env file
load_dotenv()

# Access username and password from .env
username = os.getenv("INSTA_USER")
password = os.getenv("INSTA_PASS")

# Launch browser
service = ChromeService(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

browser.implicitly_wait(3)
browser.get('https://www.instagram.com/')
sleep(2)

# Locate input fields
username_input = browser.find_element(By.NAME, "username")
password_input = browser.find_element(By.NAME, "password")

# Send values from environment
username_input.send_keys(username)
password_input.send_keys(password)

# Click login
login_button = browser.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

sleep(300)  # Let it stay open for observation
browser.quit()
