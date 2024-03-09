import requests
from bs4 import BeautifulSoup
import time
import csv
import json


url = "https://www.tritanpt.com/online-catalog/mounted/pillow-blocks/hcp-series/"

# payload = {
#        'q': 'oil seal',
#        'facet_attributes.MANUFACTURER_NAME' : 'CR Seals (SKF)',
#        'pageNo' : '4'
# }

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
}

# response = requests.get(url, headers=headers)
# html = response.text  


# soup = BeautifulSoup(html, 'html.parser')
# input_element = soup.find('input', {'id': 'dataset'})

# value = input_element['value']

# dataitem = json.loads(value)

# data_json = json.dumps(dataitem, indent=4)

# data = json.loads(data_json)


# partnumber_item = [sublist[0] for sublist in data["data"]]
# for partnumber in partnumber_item:
#     part_number = partnumber 

# shaft_Diameter_item = [sublist[1] for sublist in data["data"]]
# for shaftDiameter in shaft_Diameter_item:
#     shaft_Diameter = shaftDiameter

# mounting_Hol_item = [sublist[2] for sublist in data["data"]]
# for mountingHol in mounting_Hol_item:
#     mounting_Hol = mountingHol 

# housing_Length_item = [sublist[3] for sublist in data["data"]]
# for housingLength in housing_Length_item:
#     housing_Length = housingLength 


# print(part_number, shaft_Diameter, mounting_Hol, housing_Length)




response = requests.get(url, headers=headers)
html = response.text  

# Membuat objek BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
input_element = soup.find('input', {'id': 'dataset'})

# Mendapatkan nilai dari atribut value
value = input_element['value']

# Mengonversi nilai menjadi objek Python
data = json.loads(value)
data_json = json.dumps(data, indent=4)
# data = json.loads(data_json)
print(data_json)

# Mengambil data dari objek Python
part_numbers = [sublist[0] for sublist in data["data"]]
shaft_diameters = [sublist[1] for sublist in data["data"]]
mounting_hols = [sublist[2] for sublist in data["data"]]
housing_lengths = [sublist[3] for sublist in data["data"]]

# Menampilkan data
for part_number, shaft_diameter, mounting_hol, housing_length in zip(part_numbers, shaft_diameters, mounting_hols, housing_lengths):
    print('part number  : ' + part_number ) 
    print('shaft diameter  : ' + shaft_diameter )
    print('mounting hol  :  ' + mounting_hol )
    print('housing length  :  ' + housing_length )
    print( )
    print( )

