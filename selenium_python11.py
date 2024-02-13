from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
# import os
# loc = os.getcwd()

from selenium.webdriver.support.select import Select

serv_obj = Service("C:\\Drivers\\chromedriver.exe")
driver = webdriver.Chrome()
# driver.get("https://text-compare.com/")
# time.sleep(1)
#
# # ctrl+A #keyboard actions
# input1 = driver.find_element(By.XPATH, "//textarea[@id='inputText1']")
# input2 = driver.find_element(By.XPATH, "//textarea[@id='inputText2']")
# input1.send_keys("welcome")
# act = ActionChains(driver)
# act.key_down(Keys.CONTROL)
# act.send_keys("a")
# act.key_up(Keys.CONTROL)
# act.perform()
#
# #control +c
# act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
#
# #tab key
# act.send_keys(Keys.TAB).perform()
#
# #control+v
# act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
#

# file downloads
# def chrome_setup():
#     from selenium.webdriver.chrome.service import Service
#     serv_obj = Service("C:\\Drivers\\chromedriver.exe")
#     #to download the file in desired location
#     prefernces={"download.default_directory": loc, "plugins.always_open_pdf_externally": True}
#     # second prefrence is to download the pdf file in desired loc instead of opening it
#     ops= webdriver.ChromeOptions()
#     ops.add_experimental_option("prefs", prefernces)
#
#     driver = webdriver.Chrome(service=serv_obj, options=ops)
#     return driver
#
# driver = chrome_setup()
# driver.get("https://file-examples.com/index.php/sample-documents-download/")
# driver.find_element(By.XPATH, "//a[@href='https://file-examples.com/index.php/sample-documents-download/sample-doc-download/']")

#file uploads
driver.get("https://fileport.io/")
driver.find_element(By.XPATH, "//button[@id='upload-button']").send_keys("Sample Documents")
time.sleep(3)