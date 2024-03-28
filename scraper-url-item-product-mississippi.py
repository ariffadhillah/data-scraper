# ps sayasuk2@Artes
# Oklahoma City

# selenium-related
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs

import pandas as pd



import csv

# other necessary ones
import time

# set options as you wish
option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")


# https://productcatalog.martinsprocket.com/views/productinfo.aspx?Part_Number=80BS43%201%207/16&Website_CategoryName=Sprockets&Website_Code=SP1


EMAIL = "Paya moen tujoeh"
PASSWORD = "521988"

# EMAIL = "Canguek purei"
# PASSWORD = "jagong"

# EMAIL = "Meuge boh sidoem"
# PASSWORD = "521988"

# EMAIL = "Bruewak."
# PASSWORD = "Jagong"

# EMAIL = "Blang kaca."
# PASSWORD = "jagong"

# EMAIL = "Meuge mulieng"
# PASSWORD = "521988"

# EMAIL = "Blang Thoe"
# PASSWORD = "Jagong"

# EMAIL = "Meuge Manoek"
# PASSWORD = "Jagong"

# EMAIL = "Jamoek Plinchet"
# PASSWORD = "521988"

# EMAIL = "meuge pisang"
# PASSWORD = "jagong"

# EMAIL = "Asoe Rok"
# PASSWORD = "521988"

# EMAIL = "Hansep Chip"
# PASSWORD = "jagong"

# EMAIL = "Syara Tanyoe"
# PASSWORD = "521988"

# EMAIL = "Mugekameng"
# PASSWORD = "Jagong"

# EMAIL = "Muda Uteune"
# PASSWORD = "jagong"

# EMAIL = "Coet Gasap"
# PASSWORD = "jagong"

# EMAIL = "Awak Droe"
# PASSWORD = "jagong"

# EMAIL = "Aneuk Jameun"
# PASSWORD = "jagong"

# EMAIL = "Canguek purei"
# PASSWORD = "jagong"

# EMAIL = "Syara Tanyoe"
# PASSWORD = "521988"

# Create Edge driver with options
browser = webdriver.Edge(options=option)

time.sleep(5)
browser.get("http://facebook.com")
browser.maximize_window()
wait = WebDriverWait(browser, 10)

email_field = wait.until(EC.visibility_of_element_located((By.NAME, 'email')))
email_field.send_keys(EMAIL)
time.sleep(2)
pass_field = wait.until(EC.visibility_of_element_located((By.NAME, 'pass')))
pass_field.send_keys(PASSWORD)
time.sleep(2)
pass_field.send_keys(Keys.RETURN)

time.sleep(2)

data = []
fields = ['URL']
filename = 'hasil-url/Outdoor equipment-1.csv'
browser.get('https://web.facebook.com/groups/feed/')

# kota Boulder, NevadaCaliente, Nevada
# kota Carson, Nevada

time.sleep(10)

search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[aria-label="Search groups"]')))
# search_input.send_keys("buy and sales, Idaho")
# search_input.send_keys("bicycle sales")

# search_input.send_keys("sell/trade/buy")
# search_input.send_keys("Shoes selling in Oregon")
# search_input.send_keys("Clothing selling in Oregon")
# search_input.send_keys("Fishing gear Sale")
# search_input.send_keys("Collectibles selling in Oregon")
# search_input.send_keys("Vinyl records selling in Oregon")
# search_input.send_keys("Sports equipment sales")
# search_input.send_keys("Furniture sales")
# search_input.send_keys("Sell and buy")
# search_input.send_keys("sell/buy/trade")

# search_input.send_keys("Stamps sales")
# search_input.send_keys("Dinnerware sales")
# search_input.send_keys("Instruments sales")
# search_input.send_keys("Baby items sales")
# search_input.send_keys("Baby stuff sales")
# search_input.send_keys("Baby strore")
# search_input.send_keys("Toddler stuff sales")
# search_input.send_keys("Baby/Toddler/Kids Items For Sale")
# search_input.send_keys("Motorcycles sales")
# search_input.send_keys("Collectors sales")
# search_input.send_keys("Home decor")
# search_input.send_keys("Home appliance")
# search_input.send_keys("Music equipment")
# search_input.send_keys("Sporting equipment")
# search_input.send_keys("Audio / Hifi")
# search_input.send_keys("snowboard")
# search_input.send_keys("Antique sales")
# search_input.send_keys("Antique strore")
search_input.send_keys("Outdoor equipment")
# search_input.send_keys("Clothes sales")
# search_input.send_keys("Dj equipment sales")
# search_input.send_keys("HiFI Audio sales")
# search_input.send_keys("electronics sales")
# search_input.send_keys("electronics Items For Sale in Arkansas")
# search_input.send_keys("Furniture Items For Sale in Arkansas")
# search_input.send_keys("Sneakers/Shoes Items For Sale")
# search_input.send_keys("sneakers sale")
# search_input.send_keys("sneakers store")
# search_input.send_keys("Shoes sales")
# search_input.send_keys("Shoes store")
# search_input.send_keys("Furniture sales")
# search_input.send_keys("Furniture store")
# search_input.send_keys("cars sales")
# search_input.send_keys("cars part sales")
# search_input.send_keys("Cameras sales")
# search_input.send_keys("Piano sales")
# search_input.send_keys("ski board sales")
# search_input.send_keys("Video games sales")
# search_input.send_keys("Shirt sales")
# search_input.send_keys("Audio equipment sales")
# search_input.send_keys("Gym Fitness Equipment sales")




time.sleep(3)
search_input.send_keys(Keys.RETURN)

span_element = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.XPATH, '//span[text()="Groups"]'))
)

# Klik pada elemen span
span_element.click()

# Membaca file CSV

df = pd.read_csv('city/mississippi-city - Sheet1.csv')

# Mencari elemen input dengan atribut aria-label="Kota"
search_input_kota = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[aria-label="City"]')))

# Loop melalui setiap nilai di kolom "city"
# for kota_text in df['city']:
# # for kota_text in df['city']:


for index, row in df.iloc[0:].iterrows():
# for index, row in df.iloc[24:].iterrows():
# for index, row in df.iloc[48:].iterrows():
    kota_text = row['city']

    search_input_kota.clear()
    search_input_kota.send_keys(kota_text)


        # print(search_input_kota)    
        # Mencari elemen span dengan teks yang sesuai
    span_element_kota = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, f'//span[text()="{kota_text}"]')))
        
        # Klik pada elemen span
    time.sleep(2)
    span_element_kota.click()
    time.sleep(5)
    print(f"Name City  { kota_text}")


        # Melakukan parsing untuk mendapatkan URL grup
    html = browser.page_source
    soup = bs(html, 'html.parser')

    time.sleep(15) 
    search_results = soup.find('div', {'aria-label': 'Search results'})
    for find_a in search_results.find_all('a', {'aria-hidden': 'true'}, href=True):
        urlGrup = find_a.get('href')
        name_grup = find_a.text.strip()
        # print(f"Text: {name_grup}, Href: {urlGrup}")

        data_save = {
            'URL': urlGrup
        }
        data.append(data_save)
        print('Saving', data_save['URL'])

            # Menulis ke file CSV
        with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writerow(data_save)


        # Menunggu hingga elemen div muncul
    div_element_clear_text = WebDriverWait(browser, 10).until( EC.presence_of_element_located((By.CSS_SELECTOR, f'[aria-label="Clear filter City: {kota_text}"]')))
        
        # Klik pada elemen div
    div_element_clear_text.click()
    time.sleep(5)
    
    # try:

    # except:
    #     None
# ... (lanjutan kode)
