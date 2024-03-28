# import os
# import requests
# from bs4 import BeautifulSoup

# # URL halaman yang berisi tautan untuk mengunduh file PDF
# url = "https://www.tritanpt.com/online-catalog/mounted/mechanical-drawing/ucf-series/UCF209-45MM.html"

# # Mengakses URL dan mengambil HTML
# response = requests.get(url)
# html = response.text

# # Membuat objek BeautifulSoup
# soup = BeautifulSoup(html, 'html.parser')

# # Temukan tag <a> dengan teks "Download PDF"
# pdf_link_tag = soup.find('a', string='Download PDF')

# # Dapatkan URL dari tag <a>
# pdf_url = pdf_link_tag['href']

# # Unduh konten PDF
# pdf_content = requests.get(pdf_url).content

# # Tentukan nama file PDF dari URL
# pdf_filename = os.path.basename(url).replace('.html', '.pdf')

# # Menyimpan konten PDF sebagai file
# with open(pdf_filename, 'wb') as pdf_file:
#     pdf_file.write(pdf_content)

# print(f"File PDF berhasil disimpan sebagai {pdf_filename}")





import os
import requests
from bs4 import BeautifulSoup

# URL halaman yang berisi tautan untuk mengunduh file PDF
url = "https://www.tritanpt.com/online-catalog/mounted/mechanical-drawing/ucf-series/UCF209-45MM.html"

# Mengakses URL dan mengambil HTML
response = requests.get(url)
html = response.text

# Membuat objek BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Temukan tag <a> dengan teks "Download PDF"
pdf_link_tag = soup.find('a', string='Download PDF')

# Dapatkan URL dari tag <a>
pdf_url = pdf_link_tag['href']

# Unduh konten PDF secara bertahap
with requests.get(pdf_url, stream=True) as r:
    r.raise_for_status()
    pdf_filename = "UCFSS204-12.pdf"  # Nama file PDF yang akan disimpan
    with open(pdf_filename, 'wb') as pdf_file:
        for chunk in r.iter_content(chunk_size=8192):  # Mengunduh file dalam potongan 8KB
            pdf_file.write(chunk)

print(f"File PDF berhasil disimpan sebagai {pdf_filename}")
