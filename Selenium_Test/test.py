from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the Chrome driver
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_argument('--disable-infobars')
options.add_argument('--disable-extensions')
options.add_argument('--start-maximized')
options.add_argument('--remote-debugging-port=9222')
driver = webdriver.Chrome(options=options)

# Navigate to the Twitter home page
driver.get("https://x.com/i/flow/login")
time.sleep(5)
username_ele = driver.find_element(By.XPATH, "//input[@name='text']")
username_ele.send_keys('Ramashish2024')
nextbtn_ele = driver.find_element(By.XPATH, "//span[contains(text(),'Next')]")
nextbtn_ele.click()
time.sleep(5)
password = driver.find_element(By.XPATH, "//input[@name='password']")
password.send_keys('Vardan1234@')
loginbtn = driver.find_element(By.XPATH, "//span[contains(text(),'Log in')]")
loginbtn.click()
time.sleep(5)

# trading

# Wait until the trending topics section is visible
trending_section = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//section[contains(@aria-labelledby, 'accessible-list')]"))
)

# Find the trending topics within the section
trending_topics = trending_section.find_elements(
    By.XPATH, ".//span[contains(@class, 'css-901oao')]")

# Extract the top 5 topics
top_5_topics = [topic.text for topic in trending_topics[:5]]
print(top_5_topics)
