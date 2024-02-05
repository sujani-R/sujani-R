from selenium import webdriver
from selenium.common import ElementNotVisibleException, WebDriverException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

serv_obj = Service("C:\\Drivers\\chromedriver.exe")
driver = webdriver.Chrome()

mywait = WebDriverWait(driver, 10) #explicit wait declaration 10 secs #basic
#mywait = WebDriverWait(driver, 10,poll_frequency=2, ignored_exceptions=[ElementNotVisibleException, WebDriverException, TimeoutException, Exceptions]) #advanced

driver.implicitly_wait(10) #seconds, this applies to all the statements below #implicit wait

driver.get("https://www.google.com/")
driver.maximize_window()

driver.find_element(By.NAME, "q").send_keys("selenium")
driver.find_element(By.NAME, "q").submit()
time.sleep(1) #reduces the performance of the script

#driver.find_element(By.XPATH,"//a[@href='https://www.selenium.dev/']//h3[@class='LC20lb MBeuO DKV0Md'][normalize-space()='Selenium']").click()
#time.sleep(1)
#driver.quit() #implicit wait ends here , its default value is 0 secs

#explicit wait usage
link = mywait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='https://www.selenium.dev/']//h3[@class='LC20lb MBeuO DKV0Md'][normalize-space()='Selenium']")))
link.click()
driver.quit()