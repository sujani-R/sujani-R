from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.remote.webelement import WebElement

serv_obj = Service("C:\\Drivers\\chromedriver.exe")
driver = webdriver.Chrome()

#driver.get("https://www.snapdeal.com/")
#driver.maximize_window()
#driver.get("https://www.amazon.com/")
#driver.maximize_window()
#time.sleep (2)
#driver.back()
#driver.forward()
#driver.refresh()
#driver.quit()

##### find elements
#driver.get("https://demo.nopcommerce.com/")
#driver.maximize_window()
#element = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
#element.send_keys("iphone")
#time.sleep(2)

##multiple web elements
#element1: WebElement= driver.find_element(By.XPATH, "//div[@class='footer']//a")
#print(element1.text) #Sitemap

##when element is not present : thrown error is nosuchelementexception
#login_elemenet = driver.find_element(By.LINK_TEXT, "Log") ##log is incorrect webelement
#login_elemenet.click()

#FIND ELEMENETS WITH MULTIPLE elements
#driver.get("https://demo.nopcommerce.com/")
#elements = driver.find_elements(By.XPATH,"//div[@class='footer']//a")
#print(len(elements)) #23
#print (elements[0].text)
#for ele in elements:
  #  print(ele.text)#23 elements list

#elements not avilable
#login_element1 = driver.find_element(By.LINK_TEXT, "Log") ##log is incorrect webelement
#print(len(login_element1))

##get attribute vs text)
driver.get("https://admin-demo.nopcommerce.com/login/")
time.sleep(1)
email = driver.find_element(By.XPATH, "//input[@id='Email']")
email.clear()
email.send_keys("suj.gmail.com")
print(email.text) #none returns inner text
print(email.get_attribute("value")) # suj.gmail.com

lgin_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
print (lgin_btn.text) #LOG IN
print (lgin_btn.get_attribute("value")) #none
