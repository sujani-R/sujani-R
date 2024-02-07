from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

# ops = webdriver.ChromeOptions()
# ops.add_argument("--disable-notifications")  # to remove the notification popup from website

serv_obj = Service("C:\\Drivers\\chromedriver.exe")
#driver = webdriver.Chrome(service=serv_obj, options=ops) #to remove the notification popup from website
driver = webdriver.Chrome()

# driver.get("https://whatmylocation.com/")
# time.sleep(2)

# driver.get("https://testautomationpractice.blogspot.com")
# time.sleep(2)

#count number of rows and coloums
# rows= len(driver.find_elements(By.XPATH,"//div[@id='HTML1']//div[@class='widget-content']//tr"))
# cols= len(driver.find_elements(By.XPATH,"//div[@id='HTML1']//div[@class='widget-content']//tr[1]/th"))
# print(rows,cols)
#
# #read specific row and col data
# data= driver.find_elements(By.XPATH,"//div[@id='HTML1']//div[@class='widget-content']//tbody//tr[5]//td[1]")
# print(data[0].text) #Master In Selenium

#read all rows and cols data
# for r in range(2,8):
#     for c in range(1,5):
#         data =driver.find_elements(By.XPATH,"//div[@id='HTML1']//div[@class='widget-content']//tbody//tr["+str(r)+"]//td["+str(c)+"]")
#         data=driver.find_elements(By.XPATH,"div[@id='HTML1']//div[@class='widget-content']//tbody//tr["+str(r)+"]//td["+str(c)+"]")
#         print (data[0].text)
#     print()

#get a coloumn
# for r in range(2,8):
#     author= driver.find_elements(By.XPATH,"//div[@id='HTML1']//div[@class='widget-content']//tbody//tr["+str(r)+"]//td[2]")
#     name=(author[0].text)
#     #print (name)
#     if name=="Mukesh":
#         book=driver.find_elements(By.XPATH,"//div[@id='HTML1']//div[@class='widget-content']//tbody//tr["+str(r)+"]//td[1]")
#         price= driver.find_elements(By.XPATH,"//div[@id='HTML1']//div[@class='widget-content']//tbody//tr["+str(r)+"]//td[4]")
#         print (book[0].text)
#         print (price[0].text)

#dynamic tables
driver.get("https://opensource-demo.orangehrmlive.com")
time.sleep(1)
driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(5)
driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[1]/a[1]").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[2]/nav[1]/ul[1]/li[1]/span[1]").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[2]/nav[1]/ul[1]/li[1]/ul[1]/li[1]").click()

time.sleep(2)