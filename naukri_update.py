from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

email = os.getenv("NAUKRI_EMAIL")
password = os.getenv("NAUKRI_PASSWORD")

options = Options()
options.add_argument("--headless=new")  # New headless mode
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")  # Set window size for proper rendering

# Initialize ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.naukri.com/")
wait = WebDriverWait(driver, 20)  # Increase wait time

# Take screenshot for debugging
# driver.save_screenshot("debug_screenshot.png")

# Click Login button
try:
    search_button = wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Login']")))
    driver.execute_script("arguments[0].scrollIntoView();", search_button)
    driver.execute_script("arguments[0].click();", search_button) 
    print("Clicked on Login button...")
except:
    print("Login button not found via normal method, trying JavaScript execution.")
    search_button = driver.execute_script("return document.evaluate(\"//a[text()='Login']\", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;")
    if search_button:
        search_button.click()
    else:
        print("Login button still not found. Printing page source for debugging:")
        print(driver.page_source)

# Ensure Email input is visible and scroll into view
email_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter your active Email ID / Username']")))
driver.execute_script("arguments[0].scrollIntoView();", email_input)
email_input.send_keys(email)

# Ensure Password input is visible and scroll into view
password_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter your password']")))
driver.execute_script("arguments[0].scrollIntoView();", password_input)
password_input.send_keys(password)

# Click Login button using JavaScript
login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']")))
driver.execute_script("arguments[0].click();", login_button)

# Take a screenshot after login attempt
# driver.save_screenshot("after_login.png")
print("Loggedin successfully...")

# Click on 'View' button
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='View']"))).click()
print("Clicked on View button...")

# Click on 'Career profile'
wait.until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='collection']//span[contains(text(), 'Career profile')]"))).click()
print("Clicked on Career profile button...")
# driver.save_screenshot("Career_profile.png")
time.sleep(1)

# Click on 'editOneTheme'
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='desiredProfile']//span[text()='editOneTheme']")))
driver.execute_script("arguments[0].click();", element)
print("Clicked on Edit pencil button...")
# driver.save_screenshot("Edit_Pencil.png")

# Check if 'Mumbai' is present and update location
locations = driver.find_elements(By.XPATH, "//div[@class='chipsContainer']//div//span")
if any(location.text.strip() == "Mumbai" for location in locations):
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='chipsContainer']//div[@title='Mumbai']//a[text()='Cross']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Save']"))).click()
    print("Hi, I am from If loop")
    # driver.save_screenshot("location_isthere.png")
else:
    location_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='locationSugg']")))
    location_input.clear()
    location_input.send_keys("Mumbai")
    wait.until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='Sdrop']//div[text()='Mumbai']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Save']"))).click()
    print("Hi, I am from Else loop")
    # driver.save_screenshot("location_notthere.png")

# Close browser
driver.quit()
print("Browser closed...")

