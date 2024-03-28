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
# 56CPJ7E8 
# Create Edge driver with options
browser = webdriver.Edge(options=option)

time.sleep(2)
browser.get("https://www.motion.com")
browser.maximize_window()
wait = WebDriverWait(browser, 20)

time.sleep(2)

data = []
fields = ['Brand' , 'URL' , 'Part Number' , 'Base To Bore Centerline' , 'Bearing Series' , 'Bolt Center To Center Length' , 'Bore Diameter' , 'Bore Length' , 'Expansion Type' , 'Grease Type' , 'Housing Construction' , 'Housing Material' , 'Housing Type' , 'Insert Material' , 'Locking Device' , 'Lubrication' , 'Maximum Speed' , 'Mounting Type' , 'Radial Dynamic Load Capacity' , 'Radial Static Load Capacity' , 'Relubricatable' , 'Sealing Type' , 'Sensor Ready' , 'Shaft Attachment' , 'Standoff Included' , 'Suitable For High Temp App' , 'Suitable For Washdown Environment' , 'Take Up Frame Size' , 'Type Of Bearing' , 'Image' , 'Image url']

filename = 'hasil/hasil-scraping-Dodge----2.csv'


# filename_csv = 'electronic-scraper - Sheet1.csv'
filename_csv = 'Dodge.csv'
df = pd.read_csv(filename_csv)

# Mendapatkan URL dari kolom "G" dan membukanya satu persatu
for url in df['URL']:
    open_url_in_browser(url)
    # time.sleep(2)
# 697950324326
    time.sleep(1)

    html = browser.page_source

    soup = bs(html, 'html.parser')

    part_Number_B = ''
    base_To_Bore_Centerline = ''
    bearing_Series = ''
    bolt_Center_To_Center_Length = ''
    bore_Diameter = ''
    bore_Length = ''
    expansion_Type = ''
    grease_Type = ''
    housing_Construction = ''
    housing_Material = ''
    housing_Type = ''
    insert_Material = ''
    iocking_Device = ''
    lubrication__ = ''
    maximum_Speed = ''
    mounting_Type = ''
    radial_Dynamic_Load_Capacity =''
    radial_Static_Load_Capacity = ''
    relubricatable = ''
    sealing_Type = ''
    sensor_Ready = ''
    shaft_Attachment = ''
    standoff_Included= ''
    suitable_For_High_Temp_App = ''
    suitable_For_Washdown_Environment = ''
    take_Up_Frame_Size = ''
    type_Of_Bearing = ''
    

    # browser.execute_script("window.scrollTo(0, window.scrollY + 800);") 



    # # Cari tombol dengan teks "Show More" dan atribut data-testid "expand-fold-button" menggunakan XPath
    # try:
    #     show_more_button = WebDriverWait(browser, 10).until(
    #         EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Show More') and @data-testid='expand-fold-button']"))
    #     )
    #     show_more_button.click()
    #     print("Tombol berhasil diklik.")
    # except Exception as e:
    #     print(f"Terjadi kesalahan: {e}")

    time.sleep(.5)
    # seal_Type = soup.find('div', {'data-testid' : 'item-description'}, class_='item-description text-secondary mb-12p').text.strip()    
    part_Number_B = soup.find('h1', class_='col-12 col-md title-wrapper ng-star-inserted').text.strip()  

    try:
        base_To_Bore_Centerline_tag = soup.find_all('div', string='Base To Bore Centerline')[0]
        if base_To_Bore_Centerline_tag:
            base_To_Bore_Centerline = base_To_Bore_Centerline_tag.find_next_sibling('div').get_text(strip=True)
            # print(base_To_Bore_Centerline)
        else:
            print("Tidak dapat menemukan Base To Bore Centerline.")
    except:
        base_To_Bore_Centerline_tag = ''


    bearing_Series_tag = soup.find('div', string='Bearing Series')
    if bearing_Series_tag:
        bearing_Series = bearing_Series_tag.find_next_sibling('div').get_text(strip=True)
        # print(base_To_Bore_Centerline)
    else:
        print("Tidak dapat menemukan Bearing Series.")



    bolt_Center_To_Center_Length_tag = soup.find('div', string='Bolt Center To Center Length')
    if bolt_Center_To_Center_Length_tag:
        bolt_Center_To_Center_Length = bolt_Center_To_Center_Length_tag.find_next_sibling('div').get_text(strip=True)
        # print(bolt_Center_To_Center_Length)
    else:
        print("Tidak dapat menemukan Bolt Center To Center Length.")

    try:

        bore_Diameter_tag = soup.find_all('div', string='Bore Diameter')[0]
        if bore_Diameter_tag:
            bore_Diameter = bore_Diameter_tag.find_next_sibling('div').get_text(strip=True)
            # print(bolt_Center_To_Center_Length)
        else:
            print("Tidak dapat menemukan Bore Diameter.")
    except:
        bore_Diameter_tag = ''


    bore_Length_tag = soup.find('div', string='Bore Length')
    if bore_Length_tag:
        bore_Length = bore_Length_tag.find_next_sibling('div').get_text(strip=True)
        # print(bolt_Center_To_Center_Length)
    else:
        print("Tidak dapat menemukan Bore Length.")

    expansion_Type_tag = soup.find('div', string='Expansion Type')
    if expansion_Type_tag:
        expansion_Type = expansion_Type_tag.find_next_sibling('div').get_text(strip=True)
        # print(bolt_Center_To_Center_Length)
    else:
        print("Tidak dapat menemukan Expansion Type.")

    grease_Type_tag = soup.find('div', string='Grease Type')
    if grease_Type_tag:
        grease_Type = grease_Type_tag.find_next_sibling('div').get_text(strip=True)
        # print(bolt_Center_To_Center_Length)
    else:
        print("Tidak dapat menemukan Grease Type.")


    housing_Construction_tag = soup.find('div', string='Housing Construction')
    if housing_Construction_tag:
        housing_Construction = housing_Construction_tag.find_next_sibling('div').get_text(strip=True)
        # print(bolt_Center_To_Center_Length)
    else:
        print("Tidak dapat menemukan Housing Construction.")


    housing_Material_tag = soup.find('div', string='Housing Material')
    if housing_Material_tag:
        housing_Material = housing_Material_tag.find_next_sibling('div').get_text(strip=True)
        # print(bolt_Center_To_Center_Length)
    else:
        print("Tidak dapat menemukan Housing Material.")

    housing_Type_tag = soup.find('div', string='Housing Type')
    if housing_Type_tag:
        housing_Type = housing_Type_tag.find_next_sibling('div').get_text(strip=True)
        # print(bolt_Center_To_Center_Length)
    else:
        print("Tidak dapat menemukan Housing Type.")

    insert_Material_tag = soup.find('div', string='Insert Material')
    if insert_Material_tag:
        insert_Material = insert_Material_tag.find_next_sibling('div').get_text(strip=True)
        # print(bolt_Center_To_Center_Length)
    else:
        print("Tidak dapat menemukan Insert Material.")

    iocking_Device_tag = soup.find('div', string='Locking Device')
    if iocking_Device_tag:
        iocking_Device = iocking_Device_tag.find_next_sibling('div').get_text(strip=True)
        # print(bolt_Center_To_Center_Length)
    else:
        print("Tidak dapat menemukan Locking Device.")


    lubrication_tag = soup.find('div', string='Lubrication')
    if lubrication_tag:
        lubrication__ = lubrication_tag.find_next_sibling('div').get_text(strip=True)
        # print(bolt_Center_To_Center_Length)
    else:
        print("Tidak dapat menemukan Lubrication.")


    maximum_Speed_tag = soup.find('div', string='Maximum Speed')
    if maximum_Speed_tag:
        maximum_Speed = maximum_Speed_tag.find_next_sibling('div').get_text(strip=True)
        # print(bolt_Center_To_Center_Length)
    else:
        print("Tidak dapat menemukan Maximum Speed.")

    
    try:
        mounting_Type_tag = soup.find_all('div', string='Mounting Type')[0]
        if mounting_Type_tag:
            mounting_Type = mounting_Type_tag.find_next_sibling('div').get_text(strip=True)
            # print(bolt_Center_To_Center_Length)
        else:
            print("Tidak dapat menemukan Mounting Type.")
    except:
        mounting_Type_tag = ''


    radial_Dynamic_Load_Capacity_tag = soup.find('div', string='Radial Dynamic Load Capacity')
    if radial_Dynamic_Load_Capacity_tag:
        radial_Dynamic_Load_Capacity = radial_Dynamic_Load_Capacity_tag.find_next_sibling('div').get_text(strip=True)
        # print(bolt_Center_To_Center_Length)
    else:
        print("Tidak dapat menemukan Radial Dynamic Load Capacity.")


    radial_Static_Load_Capacity_tag = soup.find('div', string='Radial Static Load Capacity')
    if radial_Static_Load_Capacity_tag:
        radial_Static_Load_Capacity = radial_Static_Load_Capacity_tag.find_next_sibling('div').get_text(strip=True)
        # print(bolt_Center_To_Center_Length)
    else:
        print("Tidak dapat menemukan Radial Static Load Capacity.")


    relubricatable_tag = soup.find('div', string='Relubricatable')
    if relubricatable_tag:
        relubricatable = relubricatable_tag.find_next_sibling('div').get_text(strip=True)
        # print(bolt_Center_To_Center_Length)
    else:
        print("Tidak dapat menemukan Relubricatable.")


    sealing_Type_tag = soup.find('div', string='Sealing Type')
    if sealing_Type_tag:
        sealing_Type = sealing_Type_tag.find_next_sibling('div').get_text(strip=True)
        # print(bolt_Center_To_Center_Length)
    else:
        print("Tidak dapat menemukan Sealing Type.")


    sensor_Ready_tag = soup.find('div', string='Sensor Ready')
    if sensor_Ready_tag:
        sensor_Ready = sensor_Ready_tag.find_next_sibling('div').get_text(strip=True)
        # print(bolt_Center_To_Center_Length)
    else:
        print("Tidak dapat menemukan Sensor Ready.")


    shaft_Attachment_tag = soup.find('div', string='Shaft Attachment')
    if shaft_Attachment_tag:
        shaft_Attachment = shaft_Attachment_tag.find_next_sibling('div').get_text(strip=True)
        # print(bolt_Center_To_Center_Length)
    else:
        print("Tidak dapat menemukan Shaft Attachment.")


    standoff_Included_tag = soup.find('div', string='Standoff Included')
    if standoff_Included_tag:
        standoff_Included = standoff_Included_tag.find_next_sibling('div').get_text(strip=True)
        # print(bolt_Center_To_Center_Length)
    else:
        print("Tidak dapat menemukan Standoff Included.")


    suitable_For_High_Temp_App_tag = soup.find('div', string='Suitable For High Temp App')
    if suitable_For_High_Temp_App_tag:
        suitable_For_High_Temp_App = suitable_For_High_Temp_App_tag.find_next_sibling('div').get_text(strip=True)
        # print(bolt_Center_To_Center_Length)
    else:
        print("Tidak dapat menemukan Suitable For High Temp App.")


    suitable_For_Washdown_Environment_tag = soup.find('div', string='Suitable For Washdown Environment')
    if suitable_For_Washdown_Environment_tag:
        suitable_For_Washdown_Environment = suitable_For_Washdown_Environment_tag.find_next_sibling('div').get_text(strip=True)
        # print(bolt_Center_To_Center_Length)
    else:
        print("Tidak dapat menemukan Suitable For Washdown Environment.")

    take_Up_Frame_Size_tag = soup.find('div', string='Take Up Frame Size')
    if take_Up_Frame_Size_tag:
        take_Up_Frame_Size = take_Up_Frame_Size_tag.find_next_sibling('div').get_text(strip=True)
        # print(bolt_Center_To_Center_Length)
    else:
        print("Tidak dapat menemukan Take Up Frame Size.")

    type_Of_Bearing_tag = soup.find('div', string='Type Of Bearing')
    if type_Of_Bearing_tag:
        type_Of_Bearing = type_Of_Bearing_tag.find_next_sibling('div').get_text(strip=True)
        # print(bolt_Center_To_Center_Length)
    else:
        print("Tidak dapat menemukan Type Of Bearing.")







    # time.sleep(10)
    div_tag_image = soup.find("app-img", {"id": "img-rollover"})
    img_tag  = div_tag_image.find('source')
    img_url = '' + img_tag['srcset']
    srcset_value = img_tag['srcset']
    # Membagi nilai menjadi daftar URL gambar
    img_urls = srcset_value.split(',')

    # Loop melalui setiap URL gambar
    for img_url in img_urls:
        # Menghapus spasi ekstra
        img_url = img_url.strip()
        # Ambil nama file dari URL gambar
        img_filename = img_url.split('/')[-1]
        # print(img_filename)
        # Mendapatkan URL gambar
        

    data_save = {
        'Brand': 'Dodge',
        'URL' : url,
        'Part Number' : "'"+part_Number_B.replace('Dodge','').replace(' ',''),
        'Base To Bore Centerline' : "'"+base_To_Bore_Centerline,
        'Bearing Series' : "'"+bearing_Series,
        'Bolt Center To Center Length' : "'"+bolt_Center_To_Center_Length,
        'Bore Diameter' : "'"+bore_Diameter,
        'Bore Length' :  "'"+bore_Length,
        'Expansion Type' :  expansion_Type,
        'Grease Type' :  "'"+grease_Type,
        'Housing Construction' : housing_Construction,
        'Housing Material' : housing_Material,
        'Housing Type' : "'"+housing_Type,
        'Insert Material' : insert_Material,
        'Locking Device' : iocking_Device,
        'Lubrication' : lubrication__,
        'Maximum Speed' : "'"+maximum_Speed,
        'Mounting Type' : "'"+mounting_Type,
        'Radial Dynamic Load Capacity' : "'"+radial_Dynamic_Load_Capacity,
        'Radial Static Load Capacity' : "'"+radial_Static_Load_Capacity,
        'Relubricatable' : relubricatable,
        'Sealing Type' : "'"+sealing_Type,
        'Sensor Ready' : sensor_Ready,
        'Shaft Attachment' : shaft_Attachment,
        'Standoff Included' : standoff_Included,
        'Suitable For High Temp App' : suitable_For_High_Temp_App,
        'Suitable For Washdown Environment' : suitable_For_Washdown_Environment,
        'Take Up Frame Size' : "'"+take_Up_Frame_Size,
        'Type Of Bearing' : type_Of_Bearing,
        'Image' : img_filename.replace('.jpg','').replace('.png',''),
        'Image url' : 'https://www.motion.com' +img_url        
    
    }
        
    data.append(data_save)
    print('Saving', data_save['Part Number'], data_save['URL'])
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        for item in data:
            writer.writerow(item)

print('Data is successfully saved in the file', filename)





    # # Direktori tempat Anda ingin menyimpan gambar
    # save_dir = 'image_folder'

    # # Membuat direktori jika belum ada
    # os.makedirs(save_dir, exist_ok=True)

    # # Iterasi melalui setiap tag gambar dan mengunduhnya
    # for img_tag in div_tag_image.find_all('img'):
    #     # Mendapatkan URL gambar
    #     img_url = img_tag['src']
        
    #     # Tambahkan skema jika tidak ada
    #     if not img_url.startswith('http'):
    #         img_url = 'https://productcatalog.martinsprocket.com' + img_url

    #     # Mendapatkan nama file dari URL gambar
    #     img_filename = os.path.basename(img_url)
    #     print(img_filename)

    #     # Mengunduh gambar
    #     img_data = requests.get(img_url).content

    #     # Menyimpan gambar ke dalam direktori dengan nama file yang sesuai
    #     with open(os.path.join(save_dir, img_filename), 'wb') as img_file:
    #         img_file.write(img_data)

    #     print(f"Gambar {img_filename} berhasil diunduh.")
