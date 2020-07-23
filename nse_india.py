from selenium import webdriver

driver = webdriver.Chrome(executable_path='c:/drivers/chromedriver.exe')
driver.get('https://www1.nseindia.com/live_market/dynaContent/live_analysis/gainers/niftyGainers1.json')
