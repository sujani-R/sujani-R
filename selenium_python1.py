from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
serv_obj = Service("C:\\Drivers\\chromedriver.exe")
driver = webdriver.Chrome()
# driver = webdriver.Chrome

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

time.sleep(7)

driver.find_element(By.NAME, 'username').clear()
driver.find_element(By.NAME, 'username').send_keys('Admin')
driver.find_element(By.NAME, 'password').clear()
driver.find_element(By.NAME, 'password').send_keys('admin123')
driver.find_element(By.CLASS_NAME,"orangehrm-login-button").click()
time.sleep(3)
act_title = driver.title
print (act_title)
exp_title = "OrangeHRM"

if act_title == exp_title:
    print("tc passed")
else:
    print("tc failed")

#driver.close()
