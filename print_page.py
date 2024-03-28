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
from PIL import Image
from io import BytesIO  # Menambahkan impor ini

import time
import pandas as pd
import time
import os

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
browser = webdriver.Edge(options=option)

time.sleep(2)
browser.get("https://www.tritanpt.com/")
browser.maximize_window()
wait = WebDriverWait(browser, 20)

time.sleep(2)

# filename_csv = 'electronic-scraper - Sheet1.csv'
# filename_csv = 'motion-products---15.csv'

filename_csv = 'Pillow Blocks - HCP Series.csv'
df = pd.read_csv(filename_csv)


for url in df['URL Page PDF']:
    open_url_in_browser(url)
    time.sleep(1)
    print(url)
    time.sleep(2)
        
    pdf_link_tag = soup.find('a', text='Download PDF')

    # Dapatkan URL dari tag <a>
    pdf_url = pdf_link_tag['href']

    # Unduh konten PDF
    pdf_content = requests.get(pdf_url).content

    # Tentukan nama file PDF dari URL
    pdf_filename = os.path.basename(url).replace('.html', '.pdf')

    # Menyimpan konten PDF sebagai file
    with open(pdf_filename, 'wb') as pdf_file:
        pdf_file.write(pdf_content)

    print(f"File PDF berhasil disimpan sebagai {pdf_filename}")
