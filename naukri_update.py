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
time.sleep(3)
print(driver.title)

driver.quit()
