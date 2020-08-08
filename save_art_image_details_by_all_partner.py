# scrapy shell https://artsandculture.google.com/partner

import os
import csv
import pandas as pd
import urllib.error
import urllib.request


# https://note.nkmk.me/python-download-web-images/
def download_file(url, dst_path):
    try:
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(dst_path, mode='wb') as local_file:
                local_file.write(data)
    except urllib.error.URLError as e:
        print(e)

def download_file_to_dir(url, dst_dir):
    download_file(url, os.path.join(dst_dir, os.path.basename(url)))


partner_list = pd.read_csv('all_partner.csv',index_col=0).values.flatten()

# Error: 500, 501
for partner in partner_list:
    partner_name = partner.replace('https://artsandculture.google.com/partner/','')
    try:
        art_url_list = pd.read_csv('./assets/' + partner_name + '.csv',index_col=0).values.flatten()
    except:
        continue
    try:
        os.makedirs('Images/'+partner_name)
        os.makedirs('Details/'+partner_name)
    except:
        pass
    for idx, art_url in enumerate(art_url_list):
        fetch(art_url)
        img_url = 'https:' + response.xpath("//img/@src").get()
        try:
            download_file_to_dir(img_url, 'Images/'+partner_name)
            os.rename('Images/'+partner_name+'/'+img_url.split('/')[-1], 'Images/'+partner_name+'/'+str(idx))
        except:
            continue
        details = response.css('li.XD0Pkb *::text').getall()
        pd.Series(details).to_csv('./Details/'+partner_name+'/'+str(idx)+'.csv')
