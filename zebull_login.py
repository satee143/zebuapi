import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

driver = webdriver.Chrome()

driver.get('https://www.zebull.in/')
driver.find_element(By.XPATH, "//input[@type='email']").send_keys('DEL16035')
time.sleep(5)
driver.find_element(By.XPATH, "//input[@type='Submit']").click()
time.sleep(5)

# text=driver.find_element(By.XPATH,"//mat-label[@class='fontFam']").text
# print(text)
# if text=='M-PIN':
#     driver.find_element(By.XPATH, "//input[@type='password']").send_keys('069025')
#     time.sleep(5)
#     submit = wait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='login100-form-btn']")))
#     submit.click()
# else:
driver.find_element(By.XPATH, "//input[@type='password']").send_keys('Sdusa@143')
time.sleep(5)
submit = wait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='login100-form-btn']")))
submit.click()
time.sleep(5)
driver.find_element(By.XPATH, "//input[@id='userName']").send_keys('a')
driver.find_element(By.XPATH, "//input[@id='pass']").send_keys('a')
submit = wait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='login100-form-btn']")))
submit.click()

print(driver.find_element(By.XPATH,
                          '/html/body/scripts/app-root/app-home/mat-sidenav-container/mat-sidenav-content/mat-toolbar/div/button/span').text)
driver.close()
