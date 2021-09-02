from selenium import webdriver
driver = webdriver.Firefox()
driver.get("https://www.datafolks.com")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="https://datafolks.com/Portfolio"]')))
btn.click()

btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="https://datafolks.com/Services"]')))
btn.click()

btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="https://datafolks.com/Contacts"]')))
btn.click()

driver.quit()





