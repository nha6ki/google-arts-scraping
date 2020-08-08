# scrapy shell https://artsandculture.google.com/partner
# ページの最下部までスクロールする
import time
import pandas as pd
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://artsandculture.google.com/partner')

SCROLL_PAUSE_TIME = 0.5
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
for i in range(100):
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)        # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")

partner_url_list = []
elements = driver.find_elements_by_xpath("//a[@class='e0WtYb']")
for el in elements:
    partner_url_list.append(el.get_attribute("href"))

pd.Series(partner_url_list).to_csv('all_partner.csv')
