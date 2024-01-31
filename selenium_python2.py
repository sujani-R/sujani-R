from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:\\Drivers\\chromedriver.exe")
driver = webdriver.Chrome()

# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.maximize_window()
# time.sleep(5)

# print(driver.title)  #OrangeHRM
# print(driver.current_url)  #https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
# print (driver.page_source)
# driver.quit()

driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.maximize_window()
time.sleep(3)
searchbox = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
print(searchbox.is_displayed())  # true
print(searchbox.is_enabled())  # true

# is_selected() only for radio buttons and check boxes

radio_btn = driver.find_element(By.XPATH, "//input[@id='gender-male']")
print(radio_btn.is_selected())  # false
radio_btn.click()
print(radio_btn.is_selected())  # true
time.sleep(5)
# driver.close() : doesnt kill process of the browser in the background also closes only one window (focused browser)
# driver.quit() : kills browser specific process and closes all the windows
#driver.find_element(By.LINK_TEXT,"nopCommerce]").click() #need to scrol down
driver.close()
driver.quit()

