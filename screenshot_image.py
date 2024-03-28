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

filename_csv = 'tristan - Tristan.csv'
df = pd.read_csv(filename_csv)

# Mendapatkan URL dari kolom "G" dan membukanya satu persatu
# Ukuran gambar yang diinginkan
desired_width = 800
desired_height = 800



# Direktori tempat Anda ingin menyimpan screenshot
folder_name = "PDF_FILE"

# Membuat direktori jika belum ada
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# # Mendapatkan URL dari kolom "G" dan membukanya satu persatu
# for url in df['URL Page PDF']:
#     open_url_in_browser(url)
#     time.sleep(1)
#     print(url)
#     browser.execute_script("document.body.style.backgroundColor = 'white';")
#     time.sleep(2)

#     # Ambil ukuran jendela browser
#     window_size = browser.get_window_size()
#     window_width = window_size['width']
#     window_height = window_size['height']

#     # Hitung koordinat untuk mengambil gambar tengah-tengah dengan pergeseran ke atas
#     left = int((window_width - desired_width) / 2)
#     top = int((window_height - desired_height) / 2) - 65  # Geser ke atas sebesar 50 piksel
#     right = left + desired_width
#     bottom = top + desired_height
    
#     # Ambil screenshot
#     screenshot = browser.get_screenshot_as_png()
    
#     # Konversi ke mode RGB
#     image = Image.open(BytesIO(screenshot)).convert('RGB')
    
#     # Cropping gambar sesuai dengan koordinat yang dihitung
#     cropped_image = image.crop((left, top, right, bottom))
    
#     # Ambil bagian terakhir dari URL sebagai nama file
#     file_name = url.split('/')[-1]
#     # Hilangkan karakter non-alfanumerik dari nama file
#     file_name = ''.join(c for c in file_name if c.isalnum() or c in ['-', '_']).replace('pdf','').replace('pdf','')
#     # Tambahkan ekstensi file
#     file_name +=  ".pdf"
    
#     # Simpan sebagai file jpg di dalam folder folder_image
#     file_path = os.path.join(folder_name, file_name)
#     cropped_image.save(file_path)

# # Tutup Webbrowser
# browser.quit()




import os
import time
from PIL import Image
from io import BytesIO
import pyautogui
from fpdf import FPDF

# Inisialisasi PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)

# # Iterate through URLs
# for url in df['URL Page PDF']:
#     # Open URL in browser
#     open_url_in_browser(url)
#     time.sleep(1)
#     print(url)
#     browser.execute_script("document.body.style.backgroundColor = 'white';")
#     time.sleep(2)

#     # Ambil ukuran layar
#     screen_width, screen_height = pyautogui.size()

#     # Ambil screenshot layar
#     screenshot = pyautogui.screenshot()

#     # Ambil bagian tengah dari screenshot
#     desired_width = 800  # Misalnya, lebar yang diinginkan
#     desired_height = 600  # Misalnya, tinggi yang diinginkan
#     left = int((screen_width - desired_width) / 2)
#     top = int((screen_height - desired_height) / 2) - 65  # Geser ke atas sebesar 65 piksel
#     right = left + desired_width
#     bottom = top + desired_height
#     cropped_screenshot = screenshot.crop((left, top, right, bottom))

#     # Simpan screenshot dalam file PDF
#     pdf.add_page()
#     file_name = url.split('/')[-1].replace('.pdf', '') + ".pdf"
#     pdf_file_path = os.path.join(folder_name, file_name)
#     pdf.set_xy(0, 0)
#     pdf.image(screenshot, x=800, y=80, w=890)
#     pdf.output(pdf_file_path)

# # Tutup Webbrowser
# browser.quit()




from PIL import Image

# Iterate through URLs
for url in df['URL Page PDF']:
    # Open URL in browser
    open_url_in_browser(url)
    time.sleep(1)
    print(url)
    # browser.execute_script("document.body.style.backgroundColor = 'white';")
    time.sleep(2)

    # Ambil ukuran layar
    screen_width, screen_height = pyautogui.size()

    # Ambil screenshot layar
    screenshot = pyautogui.screenshot()

    # Ambil bagian tengah dari screenshot
    desired_width = 800  # Misalnya, lebar yang diinginkan
    desired_height = 600  # Misalnya, tinggi yang diinginkan
    left = int((screen_width - desired_width) / 2)
    top = int((screen_height - desired_height) / 2) - 65  # Geser ke atas sebesar 65 piksel
    right = left + desired_width
    bottom = top + desired_height
    cropped_screenshot = screenshot.crop((left, top, right, bottom))

    # Simpan screenshot dalam file gambar sementara
    temp_image_path = os.path.join(folder_name, "temp_screenshot.png")
    cropped_screenshot.save(temp_image_path)

    # Tambahkan halaman baru ke PDF dan masukkan gambar
    pdf.add_page()
    file_name = url.split('/')[-1].replace('.pdf', '') + ".pdf"
    pdf_file_path = os.path.join(folder_name, file_name)
    pdf.set_xy(0, 0)
    pdf.image(temp_image_path, x=800, y=800, w=800)  # Gunakan file gambar sementara
    pdf.output(pdf_file_path)

    # Hapus file gambar sementara
    os.remove(temp_image_path)

# Tutup Webbrowser
browser.quit()
