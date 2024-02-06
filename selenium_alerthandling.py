from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

serv_obj = Service("C:\\Drivers\\chromedriver.exe")
driver = webdriver.Chrome()

# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# time.sleep(1)
# driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']").click()
# time.sleep(1)
# alertwindow=driver.switch_to.alert
# print (alertwindow.text)
# alertwindow.send_keys("welcome")
# #alertwindow.accept()
# alertwindow.dismiss()
# time.sleep(1)

# driver.get("https://mypage.rediff.com/login/dologin")
# time.sleep(1)
# driver.find_element(By.XPATH,"//input[@value='Login']").click()
# time.sleep(1)
# driver.switch_to.alert.accept()
# time.sleep(1)
# driver.close()

##authentication popup
# driver.get("https://the-internet.herokuapp.com/basic_auth")
# driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
# time.sleep(3)
# bypass the popup by providing cred in the driver.get command
# syntax is "https//uname:password@url.com" and check for login message

# driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
# time.sleep(2)
# driver.switch_to.frame("pacakagelistframe") #pass name of the frame or id or web element or index
# driver.find_element(By.XPATH, "//h5[normalize-space()='iFrame Demo']").click()
# time.sleep(1)
# driver.switch_to.default_content() #very imp ( go back to main page
#
# driver.switch_to.frame("pacakageframe")
# driver.find_element(By.LINK_TEXT,'webdriver').click()
# time.sleep(1)
# driver.switch_to.default_content()
#
# driver.switch_to.frame("classframe")
# driver.find_element(By.LINK_TEXT,'webdriver').click()
# time.sleep(1)
# driver.switch_to.default_content()

# driver.get("https://demo.automationtesting.in/Frames.html")
# time.sleep(2)
# driver.find_element(By.XPATH, "//a[normalize-space()='Iframe with in an Iframe']").click()
#
# outer_frame = driver.find_element(By.XPATH,"/html[1]/body[1]/section[1]/div[1]")
# driver.switch_to.frame(outer_frame)
#
# inner_frame= driver.find_element(By.XPATH,"//div[@class='container']")
# driver.switch_to.frame(inner_frame)
# driver.find_element(By.XPATH, "//input[@type='text']").send_keys("welcome")
# driver.switch_to.parent_frame() #outer iframe

driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(3)
windowid=driver.current_window_handle
print(windowid) #9E7F1CBB2604ABD93F4DCCD38A0D74D6 #1D335BDB7F5BFD559AF1A5EF7FA123B2
driver.find_element(By.XPATH, "//a[normalize-space()='OrangeHRM, Inc']").click()
time.sleep(5)
windowids=driver.window_handles

#approach1
# parentwindow=windowids[0]
# childwindow=windowids[1]
# print (parentwindow)
# print (childwindow)
# driver.switch_to.window(childwindow)
# print (driver.title)
# driver.switch_to.window(parentwindow)
# print (driver.title)
# driver.close()

#approach2
for win in windowids:
    driver.switch_to.window(win)
    print(driver.title)
    if driver.title == "OrangeHRM":
        driver.close()






