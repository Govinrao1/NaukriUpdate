from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_argument("--headless")  # Ensures Chrome runs in headless mode (no UI)
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")  # Required in GitHub Actions
options.add_argument("--disable-dev-shm-usage") 

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.naukri.com/")
time.sleep(5)
print(driver.title)
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
