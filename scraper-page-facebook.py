# # ps sayasuk2@Artes


# # selenium-related
# from selenium import webdriver
# from selenium.webdriver.edge.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from bs4 import BeautifulSoup as bs

# import csv

# # other necessary ones
# import time

# # set options as you wish
# option = Options()
# option.add_argument("--disable-infobars")
# option.add_argument("start-maximized")
# option.add_argument("--disable-extensions")



# EMAIL = "Paya moen tujoeh"
# PASSWORD = "521988"

# # EMAIL = "Canguek purei"
# # PASSWORD = "jagong"

# # EMAIL = "Meuge boh sidoem"
# # PASSWORD = "521988"

# # EMAIL = "Bruewak."
# # PASSWORD = "Jagong"

# # EMAIL = "Blang kaca."
# # PASSWORD = "jagong"

# # EMAIL = "Meuge mulieng"
# # PASSWORD = "521988"

# EMAIL = "Blang Thoe"
# PASSWORD = "Jagong"

# # EMAIL = "Meuge Manoek"
# # PASSWORD = "Jagong"

# # EMAIL = "Jamoek Plinchet"
# # PASSWORD = "521988"

# # EMAIL = "meuge pisang"
# # PASSWORD = "jagong"

EMAIL = "Asoe Rok"
PASSWORD = "521988"

# # EMAIL = "Hansep Chip"
# # PASSWORD = "jagong"

# # EMAIL = "Syara Tanyoe"
# # PASSWORD = "521988"

# # EMAIL = "Mugekameng"
# # PASSWORD = "Jagong"

# # EMAIL = "Muda Uteune"
# # PASSWORD = "jagong"

# # EMAIL = "Coet Gasap"
# # PASSWORD = "jagong"

# # EMAIL = "Awak Droe"
# # PASSWORD = "521988"

# # EMAIL = "Aneuk Jameun"
# # PASSWORD = "jagong"

# # EMAIL = "Canguek purei"
# # PASSWORD = "jagong"

# # EMAIL = "Syara Tanyoe"
# # PASSWORD = "521988"

# # Create Edge driver with options
# browser = webdriver.Edge(options=option)

# time.sleep(5)
# browser.get("http://facebook.com")
# browser.maximize_window()
# wait = WebDriverWait(browser, 10)

# email_field = wait.until(EC.visibility_of_element_located((By.NAME, 'email')))
# email_field.send_keys(EMAIL)
# time.sleep(2)
# pass_field = wait.until(EC.visibility_of_element_located((By.NAME, 'pass')))
# pass_field.send_keys(PASSWORD)
# time.sleep(2)
# pass_field.send_keys(Keys.RETURN)

# time.sleep(2)

# fields = ['URL']
# filename = 'Drain, Oregon.csv'

# data = []


# browser.get('https://web.facebook.com/groups/search/groups?q=buy%20and%20sell&filters=eyJmaWx0ZXJfZ3JvdXBzX2xvY2F0aW9uOjAiOiJ7XCJuYW1lXCI6XCJmaWx0ZXJfZ3JvdXBzX2xvY2F0aW9uXCIsXCJhcmdzXCI6XCIxMDc0MzM1NDI2MTk2MDJcIn0ifQ%3D%3D')

# ps sayasuk2@Artes



















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


import csv

# other necessary ones
import time

# set options as you wish
option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# EMAIL = "Paya moen tujoeh"
# PASSWORD = "521988"

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

# EMAIL = "Alah Kupike Soe"
# PASSWORD = "Airway12@Heights"

# EMAIL = "Meuge Manoek"
# PASSWORD = "Jagong"

# EMAIL = "Jamoek Plinchet"
# PASSWORD = "521988"

EMAIL = "meuge pisang"
PASSWORD = "jagong"

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
# PASSWORD = "521988"

# EMAIL = "Aneuk Jameun"
# PASSWORD = "jagong"

# EMAIL = "Canguek purei"
# PASSWORD = "jagong"

# EMAIL = "Syara Tanyoe"
# PASSWORD = "521988"

def open_url_in_browser(url):
    try:
        browser.get(url)
        time.sleep(1)  
    except:
        None

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
fields = ['Group Name', 'URL', 'Description', 'Members']
# filename = 'nike-3.csv'
# filename = 'arizona/hasil-url/buy-california.csv'
filename = 'Louisiana/city/hasil-scraping-Louisiana.csv'

# Membaca file CSV

# filename_csv = 'electronic-scraper - Sheet1.csv'
filename_csv = 'Louisiana/city/hasil-url-Louisiana - Sheet1.csv'
df = pd.read_csv(filename_csv)

# Mendapatkan URL dari kolom "G" dan membukanya satu persatu
for url in df['URL']:
    open_url_in_browser(url + 'about')
    # time.sleep(2)

    time.sleep(1)

    possible_button_texts = ["Lihat selengkapnya", "See more"]

    # Tunggu hingga salah satu tombol muncul (maksimal 10 detik)
    button_lengkapnya = None
    for button_text in possible_button_texts:
        try:
            button_lengkapnya = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.XPATH, f'//div[text()="{button_text}"]'))
            )
            # Jika salah satu tombol ditemukan, keluar dari loop
            break
        except:
            pass

    # Jika salah satu tombol ditemukan, klik
    if button_lengkapnya:
        button_lengkapnya.click()
    
    time.sleep(1)    

    html = browser.page_source

    soup = bs(html, 'html.parser')


    # try:
    #     button_lengkapnya = WebDriverWait(browser, 10).until(
    #         EC.presence_of_element_located((By.XPATH, '//div[text()="Lihat selengkapnya"]'))
    #     )
    #     button_lengkapnya.click()
    # except:
    #     pass


    # Daftar kemungkinan teks tombol


    try:
        title = soup.find('h1', class_='x1heor9g x1qlqyl8 x1pd3egz x1a2a7pz x193iq5w xeuugli').text.strip()
    except:
        title = ''
    
    try:
        member = soup.find('div', class_='x9f619 x1n2onr6 x1ja2u2z x78zum5 x2lah0s x1nhvcw1 x6s0dn4 x1a02dak x1q0g3np xexx8yu xwrv7xz x8182xy xmgb6t1 x1kgmq87').text.strip().replace('Grup Privat','').replace('Grup Publik','').replace('rb anggota',' K').replace('anggota','').replace('members','').replace('Private group','').replace('Public group','').replace('member','').replace('See less','')
    except:
        member = ''
    
        
    try:
        discription = soup.find('div', class_='xyamay9 x1pi30zi xsag5q8 x1swvt13').text.strip().replace('Lihat selengkapnya','')
    except:
        discription = ''    
    
    # print(url)
    # print(title)
    # print(member.replace('·',''))
    # print(discription)

    data_save = {
        'Group Name' : title, 
        'URL' : url, 
        'Description' : discription.replace('Lihat Lebih Sedikit', '').replace('See less',''), 
        'Members' : member.replace('·','')
    }
    data.append(data_save)
    print('Saving', data_save['URL'],data_save['Group Name'],data_save['Members'])
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)

    

    # Menutup browser pada akhir proses
browser.quit()



# data-visualcompletion="css-img"
# data-visualcompletion="css-img"
