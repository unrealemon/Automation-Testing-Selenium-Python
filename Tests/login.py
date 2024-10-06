from selenium import webdriver
from chromedriver_py import binary_path
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
import time

from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome()

driver.get("https://banglalink.net/en")
time.sleep(2)

driver.maximize_window()
time.sleep(2)

driver.find_element(By.XPATH, "(//img[@alt='User Avatar'])[1]").click()
time.sleep(2)


driver.find_element(By.XPATH,"//div[contains(text(),'Login')]").click()
time.sleep(2)

driver.find_element(By.XPATH, "//a[contains(text(),'Login with Password')]").click()
time.sleep(2)

driver.find_element(By.XPATH, "//input[@id='basic_mobileNumber']").send_keys("01990926360")
time.sleep(2)

driver.find_element(By.XPATH, "//body/div[@id='__next']/div[4]/div[2]/div[1]/div[2]/form[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/input[1]").send_keys("P1234567")
time.sleep(2)

driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
time.sleep(5)

element = driver.find_element(By.XPATH, "//header/div[2]/div[1]/div[2]/button[1]")
time.sleep(2)
element.click()
time.sleep(5)

actions = ActionChains(driver)
element = driver.find_element(By.XPATH, "//body/div[3]/div[1]/div[3]/div[1]/div[1]/div[2]")
time.sleep(5)
actions.move_to_element(element).perform()
time.sleep(5)

driver.find_element(By.XPATH, "//body/div[3]/div[1]/div[3]/div[1]/div[1]/div[2]")
time.sleep(10)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(2)

driver.close()
driver.quit()
print("Test finished")

