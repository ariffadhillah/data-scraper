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
browser.get("https://www.motion.com")
browser.maximize_window()
wait = WebDriverWait(browser, 20)

time.sleep(2)

# filename_csv = 'electronic-scraper - Sheet1.csv'
# filename_csv = 'motion-products---15.csv'

filename_csv = 'hasil/Dodge-image - Sheet1.csv'
df = pd.read_csv(filename_csv)

# Mendapatkan URL dari kolom "G" dan membukanya satu persatu
# Ukuran gambar yang diinginkan
desired_width = 560
desired_height = 500

# Direktori tempat Anda ingin menyimpan screenshot
import os

# Direktori tempat Anda ingin menyimpan screenshot
folder_name = "folder_image"

# Membuat direktori jika belum ada
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Mendapatkan URL dari kolom "G" dan membukanya satu persatu
for url in df['Image url']:
    open_url_in_browser(url)
    time.sleep(1)
    print(url)
    browser.execute_script("document.body.style.backgroundColor = 'white';")
    time.sleep(2)

    # Ambil ukuran jendela browser
    window_size = browser.get_window_size()
    window_width = window_size['width']
    window_height = window_size['height']

    # Hitung koordinat untuk mengambil gambar tengah-tengah dengan pergeseran ke atas
    left = int((window_width - desired_width) / 2) - 30  # Geser ke kanan sebesar 50 piksel
    top = int((window_height - desired_height) / 2) - 65  # Geser ke atas sebesar 50 piksel
    right = left + desired_width 
    bottom = top + desired_height
    
    # Ambil screenshot
    screenshot = browser.get_screenshot_as_png()
    
    # Konversi ke mode RGB
    image = Image.open(BytesIO(screenshot)).convert('RGB')
    
    # Cropping gambar sesuai dengan koordinat yang dihitung
    cropped_image = image.crop((left, top, right, bottom))
    
    # Ambil bagian terakhir dari URL sebagai nama file
    file_name = url.split('/')[-1]
    # Hilangkan karakter non-alfanumerik dari nama file
    file_name = ''.join(c for c in file_name if c.isalnum() or c in ['-', '_']).replace('jpg','').replace('png','')
    # Tambahkan ekstensi file
    file_name +=  ".jpg"
    
    # Simpan sebagai file jpg di dalam folder folder_image
    file_path = os.path.join(folder_name, file_name)
    cropped_image.save(file_path)

# Tutup Webbrowser
browser.quit()



