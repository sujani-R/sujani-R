from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.remote.webelement import WebElement

serv_obj = Service("C:\\Drivers\\chromedriver.exe")
driver = webdriver.Chrome()

#driver.get("https://testautomationpractice.blogspot.com/")
#driver.maximize_window()
#time.sleep(1)

#driver.find_element(By.XPATH, "//input[@id='sunday']").click() #single checkbox clicked
#time.sleep(1)
#checkboxes=driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]") #multiple checkbox clicked
#print(len(checkboxes))

#for i in range(len(checkboxes)):
#    checkboxes[i].click()

#for checkbox in checkboxes: #select only desired checkboxes
#    weekname=checkbox.get_attribute("id")
#    if weekname=="monday" or weekname=="wednesday":
#       checkbox.click()
#        time.sleep(1)

#for i in range(len(checkboxes)-2,len(checkboxes)):
#    checkboxes[i].click()
#    time.sleep(1)

#for checkbox in checkboxes:
#    if checkbox.is_selected():
#       checkbox.click()

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
time.sleep(1)
#driver.find_element(By.XPATH,"//a[@title='Show products in category Electronics'][normalize-space()='Electronics']").click()
#time.sleep(1)

links = driver.find_elements(By.CSS_SELECTOR, "a")
print (len(links)) #90
for link in links:
    print (link.text)

linkss= driver.find_element(By.XPATH, "//a")
print (linkss)
