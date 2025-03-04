
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
import os

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

# Set up Chrome options for headless execution
options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Run without UI
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
options.add_argument("--start-maximized")  # Open browser in full screen
options.add_argument("--disable-infobars") # Remove automation banner
options.add_argument("--disable-popup-blocking") # Disable pop-up

# Start WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open Naukri.com
driver.get("https://www.naukri.com/")
time.sleep(6)  # Wait for the page to load
print("Naukri.com opened successfully!")   
search_button = driver.find_element(By.XPATH, "//a[text()='Login']")  
search_button.click()
time.sleep(3)
driver.find_element(By.XPATH, "//input[@placeholder='Enter your active Email ID / Username']").send_keys("govind1999rao@gmail.com")
driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']").send_keys("Govind123@#")
time.sleep(1)
driver.find_element(By.XPATH, "//button[text()='Login']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//a[text()='View']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//ul[@class='collection']//span[contains(text(), 'Career profile')]").click()
time.sleep(3)
element = driver.find_element(By.XPATH, "//div[@class='desiredProfile']//span[text()='editOneTheme']")
element.click()
time.sleep(3)
locations = driver.find_elements(By.XPATH, "//div[@class='chipsContainer']//div//span")
if any(location.text.strip() == "Mumbai" for location in locations):
    driver.find_element(By.XPATH,"//div[@class='chipsContainer']//div[@title='Mumbai']//a[text()='Cross']").click()
    time.sleep(4)
    driver.find_element(By.XPATH, "//button[text()='Save']").click()
    time.sleep(3)
    print("Hi I am from If loop")
else:
    location_input = driver.find_element(By.XPATH, "//input[@id='locationSugg']")
    location_input.clear()
    location_input.send_keys("Mumbai")
    time.sleep(2)
    driver.find_element(By.XPATH, "//ul[@class='Sdrop']//div[text()='Mumbai']").click()
    time.sleep(4)
    driver.find_element(By.XPATH, "//button[text()='Save']").click()
    time.sleep(2)
    print("Hi I am from else loop")

driver.quit()
print("Browser closed...")