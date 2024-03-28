import requests
from bs4 import BeautifulSoup
import time
import csv
import json
import os


page = "https://www.tritanpt.com/online-catalog/mounted/stainless-steel-units/ucflss-series/"


data = []
fields = ['Brand' , 'Part Number' , 'Series' , 'Shaft Diameter' , 'Shaft Height (in)' , 'Mounting Hole Center-to-Center (in)' , 'Housing Length (in)' , 'Housing Width (in)' , 'Basic Dynamic Load Rating' , 'Basic Static Load Rating' , 'Insert Number' , 'Housing Number' , 'Image' , 'Drawing' , 'URL Page PDF']


headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
}

filename = 'Stainless Steel Units - UCFLSS Series.csv'

# Dapatkan data JSON
response = requests.get(page, headers=headers)
html = response.text  
soup = BeautifulSoup(html, 'html.parser')
input_element = soup.find('input', {'id': 'dataset'})
value = input_element['value']
data_Jason = json.loads(value)

# Menyiapkan daftar URL dan data
url_link = []
partnumbers_B = []
shaftDiameter_D = []
shaftHeight_E = []
mountingHoleCentertoCenter = []
housingLength = []
# housingWidth = []
basicDynamicLoadRating = []
basicStaticLoadRating = []

for sublist in data_Jason["data"]:
    partnumbers_B.append(sublist[0])
    shaftDiameter_D.append(sublist[1])
    housingLength.append(sublist[2])
    mountingHoleCentertoCenter.append(sublist[3])

    # housingWidth.append(sublist[4])
    
    basicDynamicLoadRating.append(sublist[4])
    basicStaticLoadRating.append(sublist[5])
    url_link.append(page + sublist[0] + '.html')

for url_details, part_numbers, shaft_Diameter, housing_Length, mounting_Hole_Center_to_Center, basic_Dynamic_Load_Rating, basic_Static_Load_Rating in zip( url_link, partnumbers_B, shaftDiameter_D, housingLength, mountingHoleCentertoCenter, basicDynamicLoadRating, basicStaticLoadRating ):


    response = requests.get(url_details, headers=headers)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    
    # Tampilkan data untuk setiap URL
    print("URL:", url_details)

    details_page = soup.find('div', id="series-data")
    series_C = details_page.find('h1', {'style':'margin-left: 120px;'}).text.strip()

    insert_no_element = soup.find('td', string='Insert No.')
    text_siblings_insert_K = insert_no_element.find_next_sibling('td')
    insert_Number = text_siblings_insert_K.get_text(strip=True)

    housing_no_element = soup.find('td', string='Housing No.')
    text_siblings_housing_no_L = housing_no_element.find_next_sibling('td')
    housing_Number = text_siblings_housing_no_L.get_text(strip=True)

    first_img_tag = soup.find('div', id='photobox').find('img')

    # Mendapatkan URL gambar
    img_url = first_img_tag['src']

    # Tambahkan skema jika tidak ada
    if not img_url.startswith('http'):
        img_url = 'https://www.tritanpt.com' + img_url

    # Ambil nama file gambar
    img_filename_M = os.path.basename(img_url)

    # Persiapkan direktori penyimpanan
    save_dir = 'image_folder'
    os.makedirs(save_dir, exist_ok=True)

    # Unduh gambar
    img_data = requests.get(img_url).content

    # Menyimpan gambar ke dalam direktori dengan nama file yang sesuai
    with open(os.path.join(save_dir, img_filename_M), 'wb') as img_file:
        img_file.write(img_data)

    img_filename = img_filename_M.replace('.jpg','').replace('.png','') 


    a_tag = soup.find('a', id='md_button')

    # Dapatkan nilai atribut href dari elemen <a>
    url_tag = 'https://www.tritanpt.com'+a_tag['href']

    data_save = {
        'Brand' : 'Tritan',
        'Part Number' :"'"+part_numbers,
        'Series' : "'"+series_C,
        'Shaft Diameter' :  "'"+shaft_Diameter,
        'Shaft Height (in)' : ' ',
        'Housing Length (in)' : "'"+housing_Length,
        'Mounting Hole Center-to-Center (in)' : "'"+mounting_Hole_Center_to_Center,
        'Housing Width (in)' : ' ',
        'Basic Dynamic Load Rating' : "'"+basic_Dynamic_Load_Rating,
        'Basic Static Load Rating' : "'"+basic_Static_Load_Rating,
        'Insert Number' : "'"+insert_Number,
        'Housing Number' : "'"+housing_Number,
        'Image' : "'"+img_filename,
        'Drawing' : "'"+os.path.basename(url_tag).split('.')[0],
        'URL Page PDF' : url_tag

    }
    data.append(data_save)
    print('Saving', data_save['Part Number'])
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        for item in data:
            writer.writerow(item)

print('Data is successfully saved in the file', filename)
