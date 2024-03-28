# import os
# import requests
# from bs4 import BeautifulSoup

# # URL dan nama file yang diinginkan
# url = "https://www.tritanpt.com/online-catalog/mounted/mechanical-drawing/ucfss-series/UCFSS204-12.html"
# desired_filename = os.path.basename(url).replace(".html", "")

# # Ambil HTML dari URL
# response = requests.get(url)
# html = response.text

# # Buat objek BeautifulSoup
# soup = BeautifulSoup(html, "html.parser")

# # Temukan tag img dengan id "mech_drawing"
# img_tag = soup.find("img", id="mech_drawing")

# # Ambil URL gambar dari atribut src
# img_url = img_tag["src"]

# # Tambahkan skema jika tidak ada
# if not img_url.startswith("http"):
#     img_url = "https://www.tritanpt.com" + img_url

# # Unduh gambar
# img_data = requests.get(img_url).content

# # Simpan gambar dengan nama yang diinginkan
# with open(desired_filename + ".jpg", "wb") as img_file:
#     img_file.write(img_data)

# print("Gambar telah disimpan sebagai:", desired_filename + ".jpg")






import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import pandas as pd


df = pd.read_csv('tristan - Tristan.csv')  # Ganti 'nama_file.csv' dengan nama file yang sebenarnya

# Ambil URL dari kolom 'url'
urls = df['URL Page PDF'][670:]

# Cetak URL
for url in urls:
    print(url)

    folder_path = "folder_image_img"

    # Mengambil nama file gambar dari URL
    image_name = os.path.basename(urlparse(url).path).split(".")[0]  # Mendapatkan bagian tanpa ekstensi

    # Mengakses URL dan mengambil HTML
    response = requests.get(url)
    html = response.text

    # Membuat objek BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Mendapatkan tag img dengan id "mech_drawing"
    img_tag = soup.find('img', id='mech_drawing')

    # Mendapatkan URL gambar
    img_url = "https://www.tritanpt.com" + img_tag['src']

    # Mendapatkan konten gambar
    img_content = requests.get(img_url).content

    # Membuat folder jika belum ada
    os.makedirs(folder_path, exist_ok=True)

    # Menyimpan gambar dengan nama yang sesuai di folder yang ditentukan
    image_path = os.path.join(folder_path, f"{image_name}.jpg")
    with open(image_path, 'wb') as img_file:
        img_file.write(img_content)

    print(f"Gambar berhasil disimpan sebagai {image_path}")
