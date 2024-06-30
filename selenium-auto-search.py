from selenium import webdriver
from selenium.webdriver.firefox.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service('/usr/bin/geckodriver')

driver = webdriver.Firefox(service=service)
driver.get("https://www.google.com")

search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, 'q'))
)

search_box.send_keys('Python JSON PARSE')

search_box.submit()

#driver.quit()
