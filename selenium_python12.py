from xml.etree.ElementPath import ops

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
serv_obj = Service("C:\\Drivers\\chromedriver.exe")
driver = webdriver.Chrome()
# driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
# time.sleep(1)

#bootstrap dropdown
# driver.find_element(By.XPATH, "//span[@id='select2-billing_country-container']").click()
# countries= driver.find_element(By.XPATH, "//span[@id='select2-billing_country-container']")
# print (len(countries))
# for country in countries:
#     if country.text == "India":
#         country.click()
#         break

# capture screenshot
#driver.maximize_window()
#driver.save_screenshot("C:\\Users\\sujan\\PycharmProjects\\pythonProject\\selenium_python12.png")
#driver.get_screenshot_as_file("C:\\Users\\sujan\\PycharmProjects\\pythonProject\\selenium_python12.png")
#driver.get_screenshot_as_png("C:\\") #as base64() file

#tabs and windows
# driver.get("https://demo.nopcommerce.com/")
# time.sleep(2)
# #to open in new tab by pressing ctrl and enter keys
# Reglink=Keys.CONTROL + Keys.RETURN
# driver.find_element(By.LINK_TEXT, "Register").send_keys(Reglink)
# time.sleep(3)

# #open new tab and switch to new tab (new features in selenium4
# driver.get("https://demo.nopcommerce.com/")
# driver.switch_to.new_window('tab') #opens new tab
# driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

# driver.get("https://demo.nopcommerce.com/")
# driver.switch_to.new_window('window') #opens new windpw
# driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

#handling cookies
# driver.get("https://demo.nopcommerce.com/")
# cookies=driver.get_cookies()
# print (len(cookies))#3
# for cookie in cookies:
#     print(cookie.get('name'),":",cookie.get('value'))

# #add new cookie to the browser
# driver.add_cookie({'name':'Mycookie','value':'123456'})
# print ("after adding new cookie")
# cookies=driver.get_cookies()
# print (len(cookies))#4
# # if no remains same then browser is not supporting cookie functions
#
# #delete a cookie from browser
# driver.delete_cookie("Mycookie")
# cookies=driver.get_cookies()
# print (len(cookies))#3
#
# #delete all cookies
# driver.delete_all_cookies()
# cookies=driver.get_cookies()
# print (len(cookies))#0

#headless mode testing, testcases will execute in back end UI will not come up
def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:\\Drivers\\chromedriver.exe")
    webdriver.ChromeOptions()
    ops.headless = True
    driver = webdriver.Chrome(service=serv_obj,options=ops)
    return driver

driver = headless_chrome()
driver.get("https://demo.nopcommerce.com")
print(driver.title)
print (driver.current_url)
driver.quit()









