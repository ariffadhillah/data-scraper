# selenium-related
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import os

from bs4 import BeautifulSoup

import csv

# other necessary ones
import time
import requests
import json

headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36' 
} 



# set options as you wish
option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

def open_url_in_browser(url):
    try:
        browser.get(url)
        time.sleep(1)  
    except:
        None

# Create Edge driver with options
dataitems = []
fields = ['URL']
filename = 'Dodge.csv'
browser = webdriver.Edge(options=option)
for x in range(1,291):
    # Menunggu 5 detik
    time.sleep(5)
    
    # Mendapatkan URL halaman berdasarkan nomor halaman

    url = f"https://www.motion.com/misvc/mi/services/json/search.searchResults?facet_attributes.MANUFACTURER_NAME=Dodge&pageNo={x}&category=Bearings%3EMounted%20Bearings%3EPillow%20Block%20Bearings&isTaxonomyPage=true"
    
    # Mencetak URL
    print(url)
    
    # Membuka URL di browser
    browser.get(url)
    browser.maximize_window()



    html = browser.page_source

    soup = bs(html, 'html.parser')

    section_div = soup.find('div', {'hidden':'true'}).text.strip()

    data = json.loads(section_div)

    item_nos = []
    for item in data['searchResponse']['itemList']:
        item_nos.append(item['itemNo'])

    # Buat URL untuk setiap item menggunakan nilai 'itemNo'
    for item_no in item_nos:
        url_detail = f"https://www.motion.com/products/sku/{item_no}"
        
        data_save = {
            'URL': url_detail
        }
        dataitems.append(data_save)
        print('Saving', data_save['URL'])

            # Menulis ke file CSV
        with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writerow(data_save)











# 530
















































    # item_nos.append(item['itemNo'])

# print(item_nos)

# time.sleep(100)

# # filename_csv = 'electronic-scraper - Sheet1.csv'
# filename_csv = 'url.csv'
# df = pd.read_csv(filename_csv)

# # Mendapatkan URL dari kolom "G" dan membukanya satu persatu
# for url in df['URL']:
#     open_url_in_browser(url)
#     # time.sleep(2)
# # 697950324326
#     time.sleep(.5)

#     html = browser.page_source

#     soup = bs(html, 'html.parser')

#     part_Number = ''
#     case_Design = ''
#     casing_ = ''

#     time.sleep(.5)
#     part_Number = soup.find('h1', class_='col-12 col-md title-wrapper ng-star-inserted').text.strip()    
#     # print(part_Number.replace('CR Seals (SKF)','').replace(' ',''))


#     case_Design_tag = soup.find('div', string='Case Design')
#         # Jika ditemukan, temukan elemen <p> berikutnya
#     if case_Design_tag:
#         case_Design = case_Design_tag.find_next_sibling('div').get_text(strip=True)
#         # print(case_Design)
#     else:
#         print("Tidak dapat menemukan Case Design.")

#     casing_tag = soup.find('div', string='Casing')
#         # Jika ditemukan, temukan elemen <p> berikutnya
#     if casing_tag:
#         casing_ = casing_tag.find_next_sibling('div').get_text(strip=True)
#         # print(casing_)
#     else:
#         print("Tidak dapat menemukan Casing.")
    
#     print(part_Number.replace('CR Seals (SKF)','').replace(' ',''))
#     print(case_Design)
#     print(casing_)


#     # # Direktori tempat Anda ingin menyimpan gambar
#     # save_dir = 'image_folder'

#     # # Membuat direktori jika belum ada
#     # os.makedirs(save_dir, exist_ok=True)

#     # # Iterasi melalui setiap tag gambar dan mengunduhnya
#     # for img_tag in div_tag_image.find_all('img'):
#     #     # Mendapatkan URL gambar
#     #     img_url = img_tag['src']
        
#     #     # Tambahkan skema jika tidak ada
#     #     if not img_url.startswith('http'):
#     #         img_url = 'https://productcatalog.martinsprocket.com' + img_url

#     #     # Mendapatkan nama file dari URL gambar
#     #     img_filename = os.path.basename(img_url)
#     #     print(img_filename)

#     #     # Mengunduh gambar
#     #     img_data = requests.get(img_url).content

#     #     # Menyimpan gambar ke dalam direktori dengan nama file yang sesuai
#     #     with open(os.path.join(save_dir, img_filename), 'wb') as img_file:
#     #         img_file.write(img_data)

#     #     print(f"Gambar {img_filename} berhasil diunduh.")
