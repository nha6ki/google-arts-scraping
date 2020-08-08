# scrapy shell https://artsandculture.google.com/partner

import csv
import pandas as pd


partner_list = pd.read_csv('all_partner.csv',index_col=0).values.flatten()

for partner in partner_list:
    partner_name = partner.replace('https://artsandculture.google.com/partner/','')
    fetch(partner)
    img_url_list = []
    href_list = response.css('.e0WtYb').xpath('@href').getall()
    for href in href_list:
        if 'asset' in href:
            if not('search' in href):
                img_url_list.append('https://artsandculture.google.com' + href)
    if len(img_url_list) == 0:
        continue
    pd.Series(img_url_list).to_csv('./assets/' + partner_name + '.csv')
