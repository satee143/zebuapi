import pytest
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup

# import readexcel

datas = [[505001], [506001], [507002], [500082], [500071]]
urls = [['https://www.accuweather.com/en/in/505001/505001/weather-forecast/537536_pc'],
        ['https://www.accuweather.com/en/in/506001/506001/weather-forecast/545409_pc']]


@pytest.mark.parametrize('data', urls)
def test_login(data):
    '''options = Options()
    options.headless = True
    options.add_argument('--no-sandbox')  # Bypass OS security model
    options.add_argument('--disable-gpu')  # applicable to windows os only
    options.add_argument('start-maximized')  #
    options.add_argument('disable-infobars')
    options.add_argument("--disable-extensions")
    options.add_argument("--window-size=1080,1920")
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'

    options.add_argument('user-agent={0}'.format(user_agent))
    driver = webdriver.Chrome(executable_path='/storage/emulated/0/Download/a1.exe',options=options)
    driver.get('https://www.accuweather.com')
    time.sleep(3)
    element=driver.find_element_by_name('query')
    element.send_keys(data[0])
    time.sleep(5)
    element.send_keys(Keys.RETURN)
    time.sleep(5)
    driver.find_element_by_xpath('//div[@class="search-results"]/a').click()
    driver.find_element_by_xpath('//*[text()="Daily"]').click()
    time.sleep(2)
    pincode=driver.find_element_by_xpath('//span/h1').text
    url=driver.current_url
    print(pincode.strip())'''
    agent = {"User-Agent": "Mozilla/5.0"}
    request_data = requests.get(data[0], headers=agent)
    beautiful_data = request_data.text
    # print(beautiful_data)
    dataa = BeautifulSoup(beautiful_data, 'html.parser')
    '''
        print(dataa)
        data1=dataa.find(class_='two-column-page-content')
        datax=dataa.find_all(class_='date')
        print(data1)
        data2=data1.find(class_='content-module')
        data3=data2.find(class_='content-module')
        day_data=data3.find_all(class_='date')
        print(day_data)
       #day_of_the_weather=[days_data.find(class_='dow').get_text().strip() for days_data in datax]
    
        date_of_the_weather=[days_data.find(class_='sub').get_text().strip() for days_data in datax]
        high_temp_of_the_day=[int(days_data.find(class_='high').get_text().strip().replace("°","")) for days_data in dataa.find_all(class_='temps')]
        low_temp_of_the_day=[int(days_data.find(class_='low').get_text().strip().replace("/ ","").replace("°","")) for days_data in dataa.find_all(class_='temps')]
        weather_type_of_the_day=[days_data.get_text().strip() for days_data in dataa.find_all(class_='phrase')]
    
    
    
    
        weather_stuff=pd.DataFrame(
            {
             'DATE':date_of_the_weather,
             'HIGH TEMP':high_temp_of_the_day,
             'LOW TEMP':low_temp_of_the_day,
             'TYPE OF WEATHER':weather_type_of_the_day
            }
        )
        weather_stuff.reset_index(drop=True)
    
        print(weather_stuff)
        #filename=str(pincode)+".xlsx"
        #sheetname = str(pincode)
        #print(filename,sheetname)
        weather_stuff.to_excel('weather.xlsx',sheet_name='sheetname')'''
