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




# response = requests.get(url, headers=headers)
# html = response.text  

# # Membuat objek BeautifulSoup
# soup = BeautifulSoup(html, 'html.parser')
# input_element = soup.find('input', {'id': 'dataset'})

# # Mendapatkan nilai dari atribut value
# value = input_element['value']

# # Mengonversi nilai menjadi objek Python
# data = json.loads(value)
# data_json = json.dumps(data, indent=4)
# # data = json.loads(data_json)
# # print(data_json)

# # Mengambil data dari objek Python
# partnumbers_B = [sublist[0] for sublist in data["data"]]
# shaftDiameter_D = [sublist[1] for sublist in data["data"]]
# shaftHeight_E = [sublist[2] for sublist in data["data"]]
# mountingHoleCentertoCenter_F = [sublist[3] for sublist in data["data"]]
# housingLength_G = [sublist[4] for sublist in data["data"]]
# housingWidth_H = [sublist[5] for sublist in data["data"]]
# basicDynamicLoadRating_I = [sublist[6] for sublist in data["data"]]
# basicStaticLoadRating_J = [sublist[7] for sublist in data["data"]]


# # Menampilkan data
# url_link = []
# for part_numbers_B, shaft_Diameter_D, shaft_Height_E, mounting_Hole_Center_to_Center_F, housing_Length_G, housing_Width_H, basic_Dynamic_Load_Rating_I, basic_Static_Load_Rating_J in zip( partnumbers_B, shaftDiameter_D, shaftHeight_E, mountingHoleCentertoCenter_F, housingLength_G, housingWidth_H, basicDynamicLoadRating_I, basicStaticLoadRating_J ):

#     url_link.append('https://www.tritanpt.com/online-catalog/mounted/pillow-blocks/hcp-series/ucp-series/'+part_numbers_B+'.html' )
#     part_numbers = part_numbers_B 
#     shaft_Diameter =  shaft_Diameter_D 
#     shaft_Height = shaft_Height_E 
#     mounting_Hole_Center_to_Center = mounting_Hole_Center_to_Center_F 
#     housing_Length = housing_Length_G 
#     housing_Width = housing_Width_H 
#     basic_Dynamic_Load_Rating = basic_Dynamic_Load_Rating_I 
#     basic_Static_Load_Rating = basic_Static_Load_Rating_J 
    
# # print(url_link) 
# for url_details in url_link:
#     response = requests.get(url_details, headers=headers)
#     print(url_details)
#     print(part_numbers)
#     print(shaft_Diameter)
#     print(shaft_Height)
#     print(mounting_Hole_Center_to_Center)
#     print(housing_Length)
#     print(housing_Width)
#     print(basic_Dynamic_Load_Rating)
#     print(basic_Static_Load_Rating)


#     # print(part_numbers) 
#     # print(shaft_Diameter) 
#     # print(shaft_Height) 
#     # print(mounting_Hole_Center_to_Center) 
#     # print(housing_Length) 
#     # print(housing_Width) 
#     # print(basic_Dynamic_Load_Rating) 
#     # print(basic_Static_Load_Rating) 
#     # print(' ') 
#     # print(' ') 
#     # print(' ') 






# Dapatkan data JSON
response = requests.get(url, headers=headers)
html = response.text  
soup = BeautifulSoup(html, 'html.parser')
input_element = soup.find('input', {'id': 'dataset'})
value = input_element['value']
data = json.loads(value)

# Menyiapkan daftar URL dan data
url_link = []
partnumbers_B = []
shaftDiameter_D = []
shaftHeight_E = []
mountingHoleCentertoCenter_F = []
housingLength_G = []
housingWidth_H = []
basicDynamicLoadRating_I = []
basicStaticLoadRating_J = []

for sublist in data["data"]:
    partnumbers_B.append(sublist[0])
    shaftDiameter_D.append(sublist[1])
    shaftHeight_E.append(sublist[2])
    mountingHoleCentertoCenter_F.append(sublist[3])
    housingLength_G.append(sublist[4])
    housingWidth_H.append(sublist[5])
    basicDynamicLoadRating_I.append(sublist[6])
    basicStaticLoadRating_J.append(sublist[7])
    url_link.append('https://www.tritanpt.com/online-catalog/mounted/pillow-blocks/hcp-series/ucp-series/' + sublist[0] + '.html')

# Kunjungi setiap URL dan tampilkan data
for url_details, part_numbers, shaft_Diameter, shaft_Height, mounting_Hole_Center_to_Center, housing_Length, housing_Width, basic_Dynamic_Load_Rating, basic_Static_Load_Rating in zip(url_link, partnumbers_B, shaftDiameter_D, shaftHeight_E, mountingHoleCentertoCenter_F, housingLength_G, housingWidth_H, basicDynamicLoadRating_I, basicStaticLoadRating_J):
    response = requests.get(url_details, headers=headers)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    
    # Tampilkan data untuk setiap URL
    print("URL:", url_details)
    print("Part Number:", part_numbers)
    print("Shaft Diameter:", shaft_Diameter)
    print("Shaft Height:", shaft_Height)
    print("Mounting Hole Center to Center:", mounting_Hole_Center_to_Center)
    print("Housing Length:", housing_Length)
    print("Housing Width:", housing_Width)
    print("Basic Dynamic Load Rating:", basic_Dynamic_Load_Rating)
    print("Basic Static Load Rating:", basic_Static_Load_Rating)
    print()