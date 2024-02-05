import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

serv_obj = Service("C:\\Drivers\\chromedriver.exe")
driver = webdriver.Chrome()

# driver.get("http://www.deadlinkcity.com/")
# driver.maximize_window()
# time.sleep(2)

# alllinks=driver.find_elements(By.TAG_NAME,'a')
# count =0
# for link in alllinks:
#     url = link.get_attribute('href')
#     res=requests.head(url)
#     if res.status_code<=400:
#         print(url,"is broken")
#         count = count+1
#     else:
#         print(url,"is valid")
# print("total count",count)

driver.get("https://the-internet.herokuapp.com/dropdown")
driver.maximize_window()
time.sleep(1)

drpdwn_ele = driver.find_element(By.XPATH,"//select[@id='dropdown']")
drpdwn=Select(drpdwn_ele)
# drpdwn.select_by_visible_text("Option 1")
# time.sleep(1)
# drpdwn.select_by_value("2")
# time.sleep(1)
# time.sleep(2)
# drpdwn.select_by_value("2")
# time.sleep(2)

alloptions=drpdwn.options
print (len(alloptions))
#
# for option in alloptions:
#     print (option.text)

for option in alloptions:
   if option.text=="Option 1":
       option.click()
       time.sleep(1)
       break