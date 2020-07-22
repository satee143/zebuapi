from bs4 import BeautifulSoup
import requests

url_webpage = 'https://www.ceneo.pl/Podzespoly_komputerowe;discount.htm'
ceneo_page = requests.get(url_webpage)
soup = BeautifulSoup(ceneo_page.content, 'html.parser')
discounts_percents = soup.find_all('span', {'class': 'price-discount_label'})
products_titles = soup.find_all('a', {'class': 'go-to-product js_conv js_clickHash js_seoUrl'})
prices_list = soup.find_all('span', {'class' : 'price'})
categories = soup.find_all('a', {'class' : {'link'}})
parameters = soup.find_all('ul', {'class' : {'prod-params cat-prod-row__params'}})
items = dict()


def get_discounts(dictionary_items):
    for discount_percent in discounts_percents:
        dictionary_items['discount percent'] = discount_percent.get_text()
    for product_title in products_titles:
        dictionary_items['product title'] = product_title.get_text()
        dictionary_items['href'] = 'https://www.ceneo.pl' + product_title.get('href')
    for prices in prices_list:
        dictionary_items['price'] = prices.get_text() + ' zł'
    for category in categories:
        dictionary_items['category'] = category.get_text().strip()
    for params in parameters: 
        dictionary_items['parameters'] = '\n' + params.get_text().strip()

    return dictionary_items.items()


def get_info():
    dictionary = get_discounts(items)
    for key, value in dictionary:
        print(key, ':',  value)


get_info()