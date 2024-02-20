from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

serv_obj = Service("C:\\Drivers\\chromedriver.exe")
driver = webdriver.Chrome()
# driver.get("https://opensource-demo.orangehrmlive.com")
# time.sleep(1)
# driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
# driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
# driver.find_element(By.XPATH,"//button[@type='submit']").click()
# time.sleep(5)
# admin=driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[1]/a[1]")
# time.sleep(2)
# usr_mngmt= driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[2]/nav[1]/ul[1]/li[1]/span[1]")
# time.sleep(2)
# usr= driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[2]/nav[1]/ul[1]/li[1]/ul[1]/li[1]")
# time.sleep(2)
#
# #mouse hover action
# act= ActionChains(driver)
# act.move_to_element(admin).move_to_element(usr_mngmt).move_to_element(usr).click().perform()
# time.sleep(2)

# rightclick
# driver.get("https://swisnl.github.io/jQuery-contextMenu/demo")
# time.sleep(2)
# button=driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
# act= ActionChains(driver)
# act.context_click(button).perform()
# time.sleep(2)

# double click
# driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick")
# time.sleep(2)
# driver.switch_to.frame("iframeResult")
#
# button = driver.find_element(By.XPATH, "//button[@ondblclick='myFunction()']")
# act=ActionChains(driver)
# act.double_click(button).perform()
# time.sleep(2)

# drag and drop
# driver.get("https://www.globalsqa.com/demo-site/draganddrop/#Photo%20Manager")
# driver.maximize_window()
# time.sleep(3)
# myframe=driver.find_element(By.XPATH, "//iframe[@class='demo-frame lazyloaded']")
# driver.switch_to.frame(myframe)
# source = driver.find_element(By.XPATH, "//img[@alt='The peaks of High Tatras']")
# target = driver.find_element(By.XPATH, "//div[@id='trash']")
# act = ActionChains(driver)
# act.drag_and_drop(source, target).perform()
# time.sleep(2)

# driver.get("https://seleniumbase.io/demo_page")
# time.sleep(3)
# min =driver.find_element(By.XPATH, "//input[@id='mySlider']")
# print ("before moving")
# print(min.location)
# act= ActionChains(driver)
# act.drag_and_drop_by_offset(min, 224,0).perform()
# # negative number to decrease the slider
# #in verticle sliders change y axis parameters
# print ("after moving")
# print(min.location)

##scrolling
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
# scroll by pixels
# driver.execute_script("window.scrollBy(0,3000)","")  # to execute java script
# value=driver.execute_script("return window.pageYoffset;")
# print

#scroll till element is displayed
flag= driver.find_element(By.XPATH,"//img[@alt='Flag of India']")
driver.execute_script("arguments[0].scrollIntoView();", flag)
time.sleep(2)
value=driver.execute_script("return window.pageYoffset;")
print (value)

#scroll till end of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
#to scroll up to start of the page
driver.execute_script("window.scrollTo(0,-document.body.scrollHeight);")
time.sleep(2)


