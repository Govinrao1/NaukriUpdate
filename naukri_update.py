from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

# Load credentials from environment variables
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

if not EMAIL or not PASSWORD:
    raise ValueError("EMAIL or PASSWORD environment variable is missing!")

# Set up Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Maximize browser window
options.add_argument("--disable-infobars")  # Remove automation banner
options.add_argument("--disable-popup-blocking")  # Disable pop-ups
options.add_argument("--no-sandbox")  # Required for CI/CD
options.add_argument("--disable-dev-shm-usage")  # Prevent memory issues

# Use Xvfb virtual display if running in GitHub Actions
if os.getenv("GITHUB_ACTIONS") == "true":
    options.add_argument("--headless")  # Enable headless mode for CI/CD
    options.add_argument("--disable-gpu")  # Disable GPU acceleration

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Open Naukri.com
    driver.get("https://www.naukri.com/")
    time.sleep(6)
    print("Naukri.com opened successfully!")

    # Login process
    driver.find_element(By.XPATH, "//a[text()='Login']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@placeholder='Enter your active Email ID / Username']").send_keys(EMAIL)
    driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']").send_keys(PASSWORD)
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[text()='Login']").click()
    time.sleep(5)

    # Navigate to Career Profile
    driver.find_element(By.XPATH, "//a[text()='View']").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//ul[@class='collection']//span[contains(text(), 'Career profile')]").click()
    time.sleep(3)

    # Edit profile
    driver.find_element(By.XPATH, "//div[@class='desiredProfile']//span[text()='editOneTheme']").click()
    time.sleep(3)

    # Check if "Mumbai" is already set
    locations = driver.find_elements(By.XPATH, "//div[@class='chipsContainer']//div//span")
    if any(location.text.strip() == "Mumbai" for location in locations):
        driver.find_element(By.XPATH, "//div[@class='chipsContainer']//div[@title='Mumbai']//a[text()='Cross']").click()
        time.sleep(4)
        driver.find_element(By.XPATH, "//button[text()='Save']").click()
        time.sleep(3)
        print("Location removed: Mumbai")
    else:
        location_input = driver.find_element(By.XPATH, "//input[@id='locationSugg']")
        location_input.clear()
        location_input.send_keys("Mumbai")
        time.sleep(2)
        driver.find_element(By.XPATH, "//ul[@class='Sdrop']//div[text()='Mumbai']").click()
        time.sleep(4)
        driver.find_element(By.XPATH, "//button[text()='Save']").click()
        time.sleep(2)
        print("Location added: Mumbai")

except Exception as e:
    print(f"Error: {e}")

finally:
    driver.quit()
    print("Browser closed...")
