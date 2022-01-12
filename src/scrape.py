#!/usr/local/bin/python -B
# scrape.py

import os
import warnings
import requests
from time import sleep
from datetime import datetime
from selenium import webdriver


warnings.filterwarnings('ignore')

options = webdriver.FirefoxOptions()
options.headless = True
driver = webdriver.Firefox(options=options)

driver.get('https://leetcode.com/{username}/'.format(username=os.environ['LEETCODE_USERNAME']))
sleep(3)

if 'day' in driver.find_elements_by_css_selector('div.ant-spin-container')[2].find_element_by_css_selector('li:first-child > a > span.css-6jjn9s').text:
    requests.get(os.environ['HEALTHCHECKS_URL'] + '/fail', timeout=10)
else:
    requests.get(os.environ['HEALTHCHECKS_URL'], timeout=10)