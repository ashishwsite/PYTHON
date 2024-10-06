from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

# Open a webpage (replace 'https://example.com' with your target URL)
driver.get("https://www.codewithharry.com/")

try:
  
    span_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="imgpreview2"]/div[1]/div[1]/span'))
    )

    # Fetch the text content of the span element
    span_text = span_element.text
    # Store the text content in a variable
    span_content = span_text
    # Print the content stored in the variable
    print("Span content:", span_content)
except Exception as e:
    print("An error occurred:", e)
finally:
    # Close the WebDriver
    driver.quit()
