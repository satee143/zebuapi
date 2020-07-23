import time

# import pytest, openpyxl
# from bs4 import BeautifulSoup
# import requests
# import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = True
options.add_argument('--no-sandbox')  # Bypass OS security model
options.add_argument('--disable-gpu')  # applicable to windows os only
options.add_argument('start-maximized')  #
options.add_argument('disable-infobars')
options.add_argument("--disable-extensions")
options.add_argument("--window-size=1080,1920")
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
options.add_argument('user-agent={0}'.format(user_agent))

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get('https://www.moneycontrol.com')
stock = input("Enter the stock u want to quote")
quote = driver.find_element_by_id('search_str').send_keys(stock)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="autosuggestlist"]/ul/div/div/li/a/span').click()
time.sleep(2)
stock_name = driver.find_element_by_xpath('//h1[@class="pcstname"]').text
Date_as_on = driver.find_element_by_xpath('//*[@class="display_lastupd"]').text
sector = driver.find_element_by_xpath('//*[@id="sec_quotes"]/div[2]/div/div[1]/span[6]/a').text
p_e = driver.find_element_by_xpath('//li[1]/ul[1]/li[2]/*[@class="value_txtfr"]').text
pledge = driver.find_element_by_xpath(
    '//*[@id="sec_shrhldPat"]/div/div/div[1]/div/div[1]/div/table/tbody/tr[2]/td[2]/span').text
day_low = driver.find_element_by_xpath('//div[@class="clearfix lowhigh_band todays_lowhigh_wrap"]/div[1]').text
day_high = driver.find_element_by_xpath('//div[@class="clearfix lowhigh_band todays_lowhigh_wrap"]/div[3]').text
eq_capital = driver.find_element_by_xpath('//li[1]/ul[1]/li[1]/*[@class="value_txtfr"]').text
face_value = driver.find_element_by_xpath('//li[3]/ul[1]/li[3]/*[@class="value_txtfr"]').text
book_value = driver.find_element_by_xpath('//li[1]/ul[1]/li[3]/*[@class="value_txtfr"]').text
beta = driver.find_element_by_xpath(
    '//*[@id="div_bse_livebox_wrap"]/div[1]/div[2]/div[2]/div/ul/li[1]/div[2]/span[2]').text

promoter_hodling = driver.find_element_by_xpath(
    '//*[@id="sec_shrhldPat"]/div/div/div[1]/div/div[1]/div/table/tbody/tr[1]/td[2]/span').text
mf_holding = driver.find_element_by_xpath('//tr[7]/td[2]/span').text
finacial_companies_holding = driver.find_element_by_xpath('//tr[5]/td[2]/span').text
insurance_companies_holding = driver.find_element_by_xpath('//tr[6]/td[2]/span').text
public_holding = driver.find_element_by_xpath('//tr[9]/td[2]/span').text
ratios = driver.find_element_by_xpath('/html/body/section[14]/div/div/div/div[4]/ul/li[8]/a')
driver.execute_script("arguments[0].click();", ratios)
main_window_handle = driver.current_window_handle
window_handles = driver.window_handles
driver.switch_to.window(window_handles[1])
time.sleep(4)
eps_2 = driver.find_element_by_xpath('//*[@id="standalone-new"]/div[1]/table/tbody/tr[3]/td[4]').text
eps_1 = driver.find_element_by_xpath('//*[@id="standalone-new"]/div[1]/table/tbody/tr[3]/td[3]').text
eps_0 = driver.find_element_by_xpath('//*[@id="standalone-new"]/div[1]/table/tbody/tr[3]/td[2]').text
debt_eq_ratio = driver.find_element_by_xpath('//*[@id="standalone-new"]/div[1]/table/tbody/tr[22]/td[2]').text
divedent = driver.find_element_by_xpath('//*[@id="standalone-new"]/div[1]/table/tbody/tr[8]/td[2]').text
driver.switch_to.window(main_window_handle)
time.sleep(4)
driver.maximize_window()
sale = driver.find_element_by_xpath('/html/body/section[14]/div/div/div/div[4]/ul/li[6]/a')
driver.execute_script("arguments[0].click();", sale)
driver.switch_to.window(driver.window_handles[2])
if 'bank' not in sector:
    sales_2 = driver.find_element_by_xpath('//*[@id="standalone-new"]/div[1]/table/tbody/tr[2]/td[4]').text
    sales_1 = driver.find_element_by_xpath('//*[@id="standalone-new"]/div[1]/table/tbody/tr[2]/td[3]').text
    sales_0 = driver.find_element_by_xpath('//*[@id="standalone-new"]/div[1]/table/tbody/tr[2]/td[2]').text

print(stock_name, Date_as_on, p_e, day_low, day_high, eq_capital, face_value, promoter_hodling, mf_holding,
      finacial_companies_holding, insurance_companies_holding, sales_0, sales_1, sales_2, eps_0, eps_1, eps_2)
### Validating P/E
Negatives = []
Postives = []
if float(p_e) <= 20:
    Postives.append('P/E is less than 20')
else:
    Negatives.append('P/E is greater than 20')
if float(debt_eq_ratio) <= 1:
    Postives.append('Debt Equity Ratio is lessthan 1')
else:
    Negatives.append('Debt Equity Ratio is lessthan 1')
divident_percentage = float(day_low) / float(divedent)
if int(divident_percentage) in range(2, 6):
    Postives.append('Divdident is Good Percentage')
else:
    Negatives.append('Divident is Lesser Percentage')
if float(promoter_hodling) > 75:
    Postives.append('Promoter Holding is greater than 75%')
else:
    Negatives.append("Promoter Holding is less than 75%")

if float(public_holding) <= 10:
    Postives.append("Public Holding is less than 10%")
else:
    Negatives.append('Public Holding is greater than 10%')
if float(sales_2.replace(',', '')) >= float(sales_1.replace(',', '')) >= float(sales_0.replace(',', '')):
    Postives.append('Sales Growth Year on Year')
else:
    Negatives.append('No Sales Growth ')
if float(beta) <= 1:
    Postives.append('BETA is less than 1%')
else:
    Negatives.append('BETA greater than 1%')

if float(eps_2) >= float(eps_1) > float(eps_0):
    Postives.append('EPS is Year on Year Growth')
else:
    Negatives.append('NO EPS growth')

print(stock_name)
print('POSTIVES\t\t\t\t\t', '----', 'NEGATIVES')
for x, y in zip(Postives, Negatives):
    print(x, '\t\t\t\t\t', y)

print("POSTIVES OF THE STOCK")
for x in Postives:
    print(x)

print("NEGATIVES OF THE STOCK")
for x in Negatives:
    print(x)
