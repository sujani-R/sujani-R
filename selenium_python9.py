from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

serv_obj = Service("C:\\Drivers\\chromedriver.exe")
driver = webdriver.Chrome()
# driver.get("https://jqueryui.com/datepicker/")
#
# driver.switch_to.frame(0) #switch to frame mm/dd/yyyy format
# ##when website allows date to be picked using send keys method
# #driver.find_element(By.XPATH, "//input[@id='datepicker']").send_keys("12/02/2024")
# #time.sleep(2)
#
# ## when website doesnt allow send_keys method
# year= "2025"
# month ="February"
# date="12"
# driver.find_element(By.XPATH, "//input[@id='datepicker']").click()
# while True:
#     mon= driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/span[1]").text
#     yr= driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/span[2]").text
#     if mon==month and yr==year:
#         break
#     else:
#         driver.find_element(By.XPATH, " //span[@class='ui-icon ui-icon-circle-triangle-e']").click() #years greater than present year
#         #driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-w']").click() #years less than present year
#
# #date selection
# dates=driver.find_elements(By.XPATH, "/html[1]/body[1]/div[1]/table[1]/tbody/tr/td/a")
# #print (dates[10].text)
# for i in range(1,32):
#     if dates[i].text == date:
#         dates[i].click()
#         time.sleep(2)
#         break

#second case with drop downs in date picker
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.find_element(By.XPATH, "//input[@id='dob']").click()
time.sleep(1)
datepicker_month=Select(driver.find_element(By.XPATH, "//select[@aria-label='Select month']"))
datepicker_month.select_by_visible_text("Dec")
datepicker_year=Select(driver.find_element(By.XPATH, "//select[@aria-label='Select year']"))
datepicker_year.select_by_visible_text("1990")

dates= driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for i in range(1,32):
    if dates[i].text == "25":
        dates[i].click()
        time.sleep(2)
        break



