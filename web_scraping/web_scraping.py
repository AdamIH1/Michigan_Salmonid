import os
import time 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By 
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from soupsieve import select 

url = "https://www2.dnr.state.mi.us/fishstock/"
PATH = "/Users/adamisaiahhansen/downloads/projects/chromedriver"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

browser = webdriver.Chrome(executable_path = PATH, options=options)
browser.get(url) 

element_start_year = browser.find_element_by_id("StartYear")
select = Select(element_start_year)

try: 
    select.select_by_visible_text('2021')
except NoSuchElementException: 
    print('The item does not exist')


element_end_year = browser.find_element_by_id("EndYear")
select = Select(element_end_year)

try: 
    select.select_by_index(0)
except NoSuchElementException: 
    print('The item does not exist')

element_start_month = browser.find_element_by_id("StartMonth")
select = Select(element_start_month)

try: 
    select.select_by_index(0)
except NoSuchElementException: 
    print('The item does not exist')

element_end_month = browser.find_element_by_id("EndMonth")
select = Select(element_end_month)

try: 
    select.select_by_index(0)
except NoSuchElementException: 
    print('The item does not exist')


submit_button = browser.find_element_by_id("submitQueryBtn")

submit_button.click()

export_button = WebDriverWait(browser, 20)
export_button = browser.find_element_by_id("exportQueryBtn")
export_button.click()