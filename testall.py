import unittest 
from selenium import webdriver 

class AmazonHomePage(unittest. TestCase):

	def setUp(self):

		self.driver = webdriver.Firefox(executable_path='mypath') 
		self.driver.get('http://www.google.com')

	def test_load_home_page(self):

		self.get_title=self.driver.title

	def tearDown(self):

		self.driver.close()