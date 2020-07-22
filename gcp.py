from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote('34.96.205.81:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
driver.get('http://www.nseindia.com')
print(driver.title)
