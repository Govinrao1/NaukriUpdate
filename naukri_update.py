from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# Fetch email and password from environment variables
email = os.getenv("NAUKRI_EMAIL")
password = os.getenv("NAUKRI_PASSWORD")

# Set up Chrome options
options = Options()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-blink-features=AutomationControlled")  # Avoid detection
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

# Initialize ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 30)  # Initialize WebDriverWait with a 30-second timeout

try:
    # Navigate to Naukri.com
    driver.get("https://www.naukri.com/")
    time.sleep(3)
    print("Navigated to Naukri.com")

    # Click on the 'Login' button
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Login']")))
    driver.execute_script("arguments[0].click();", login_button)
    print("Clicked on Login button...")

    # Enter email
    email_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter your active Email ID / Username']")))
    email_input.send_keys("govind1999rao@gmail.com")
    print("Entered email...")

    # Enter password
    password_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter your password']")))
    password_input.send_keys("Govind123@#")
    print("Entered password...")

    # Click on the 'Login' button
    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']")))
    driver.execute_script("arguments[0].click();", submit_button)
    print("Logged in successfully...")

    # Wait for the profile page to load
    time.sleep(5)
    # Click on the 'View' button
    view_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > main > div > div > div.user-details.br-10.border.left-section > div > div.other-info-wrapper > div.view-profile-wrapper > a")))
    driver.execute_script("arguments[0].click();", view_button)
    print("Clicked on 'View' button...")

    # Wait for the 'Career profile' section to load
    time.sleep(5)

    # Click on 'Career profile'
    career_profile_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='collection']//span[contains(text(), 'Career profile')]")))
    driver.execute_script("arguments[0].click();", career_profile_button)
    print("Clicked on 'Career profile' button...")

    # Wait for the 'Edit' button to appear
    time.sleep(5)

    # Click on the 'Edit' button
    edit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='desiredProfile']//span[text()='editOneTheme']")))
    driver.execute_script("arguments[0].click();", edit_button)
    print("Clicked on 'Edit' button...")

    # Wait for the location section to load
    time.sleep(5)

    # Check if 'Mumbai' is present in the locations
    locations = driver.find_elements(By.XPATH, "//div[@class='chipsContainer']//div//span")
    if any(location.text.strip() == "Mumbai" for location in locations):
        remove_mumbai_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='chipsContainer']//div[@title='Mumbai']//a[text()='Cross']")))
        driver.execute_script("arguments[0].click();", remove_mumbai_button)
        print("Removed 'Mumbai' from locations...")
    else:
        location_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='locationSugg']")))
        location_input.clear()
        location_input.send_keys("Mumbai")
        mumbai_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='Sdrop']//div[text()='Mumbai']")))
        driver.execute_script("arguments[0].click();", mumbai_option)
        print("Added 'Mumbai' to locations...")

    # Click on the 'Save' button
    save_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Save']")))
    driver.execute_script("arguments[0].click();", save_button)
    print("Saved changes...")

except TimeoutException as e:
    print(f"An error occurred: {e}")
    driver.save_screenshot("error_screenshot.png")
finally:
    # Close the browser
    driver.quit()
    print("Browser closed...")
