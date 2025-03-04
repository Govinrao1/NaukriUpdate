from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

# if not EMAIL or not PASSWORD:
#     raise ValueError("EMAIL or PASSWORD environment variable is missing!")

# Set up Chrome options for GitHub Actions
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Required for GitHub Actions
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")

# Initialize WebDriver
driver = webdriver.Chrome(options=options)

try:
    # Open Naukri.com
    driver.get("https://www.naukri.com/")
    wait = WebDriverWait(driver, 15)  # Wait for elements

    print("Naukri.com opened successfully!")

    # Login process
    search_button = wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Login']")))
    search_button.click()

    email_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your active Email ID / Username']")))
    email_input.send_keys(EMAIL)

    password_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']")
    password_input.send_keys(PASSWORD)

    driver.find_element(By.XPATH, "//button[text()='Login']").click()

    print("Logged in successfully!")

    # Navigate to Career Profile
    profile_view = wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='View']")))
    profile_view.click()

    career_profile = wait.until(EC.presence_of_element_located((By.XPATH, "//ul[@class='collection']//span[contains(text(), 'Career profile')]")))
    career_profile.click()

    print("Navigated to Career Profile.")

    # Edit profile
    edit_button = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='desiredProfile']//span[text()='editOneTheme']")))
    edit_button.click()

    print("Editing profile...")

    # Check if "Mumbai" is already set
    locations = driver.find_elements(By.XPATH, "//div[@class='chipsContainer']//div//span")
    if any(location.text.strip() == "Mumbai" for location in locations):
        remove_button = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='chipsContainer']//div[@title='Mumbai']//a[text()='Cross']")))
        remove_button.click()

        save_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Save']")))
        save_button.click()

        print("Removed Mumbai from location.")
    else:
        location_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='locationSugg']")))
        location_input.clear()
        location_input.send_keys("Mumbai")

        mumbai_option = wait.until(EC.presence_of_element_located((By.XPATH, "//ul[@class='Sdrop']//div[text()='Mumbai']")))
        mumbai_option.click()

        save_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Save']")))
        save_button.click()

        print("Added Mumbai to location.")

except Exception as e:
    print(f"Error: {e}")

finally:
    driver.quit()
    print("Browser closed.")
