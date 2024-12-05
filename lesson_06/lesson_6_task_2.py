from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

driver.find_element(By.ID, "newButtonName").send_keys("SkyPro")
driver.find_element(By.ID, "updatingButton").click()
button = driver.find_element(By.ID, "updatingButton").text
print(button)


driver.quit()