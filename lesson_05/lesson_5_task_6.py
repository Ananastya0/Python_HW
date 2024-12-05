from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")

login = driver.find_element(By.ID, "username")
login.send_keys("tomsmith")
password = driver.find_element(By.ID, "password")
password.send_keys("SuperSecretPassword!")
driver.find_element(By.TAG_NAME, "button").click()

driver.quit()