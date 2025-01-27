from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
# Menyiapkan WebDriver (Chrome) dengan opsi headless

def scraping_etl() :
    options = Options()
    options.add_argument("--headless")  # Mode headless (tanpa GUI)
    options.add_argument("--no-sandbox")  # Penting untuk container Docker
    options.add_argument("--disable-dev-shm-usage")  # Kurangi konsumsi shared memory
    options.add_argument("--disable-gpu")  # Nonaktifkan GPU (opsional untuk headless)
    options.add_argument("--disable-extensions")  # Nonaktifkan ekstensi Chrome
    options.add_argument("--start-maximized")  # Maksimalkan window (opsional)
    options.add_argument("--window-size=1920,1080")  # Set ukuran window

    # Menyiapkan WebDriver dengan path yang benar (menambahkan Service)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # URL halaman web
    url = "https://www.indogold.id/harga-emas-hari-ini"
    driver.get(url)


    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "tab-single-price"))
    )

    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')

    table = soup.find('table', class_='tab-single-price')
    tbody = table.find('tbody')
    data_rows = []
    if table:
        tbody = table.find('tbody')
        if tbody:
            rows = tbody.find_all('tr')
            for row in rows:
                columns = row.find_all('td')
                data = [col.get_text(strip=True) for col in columns]
                data_rows.append(data)
        else:
            print("Elemen <tbody> tidak ditemukan")
    else:
        print("Tabel dengan kelas 'tab-single-price' tidak ditemukan")

    # Tutup browser
    driver.quit()

    columns = ['weight', 'antam_price', 'ubs_price']
    df = pd.DataFrame(data_rows[1:], columns=columns)
    df.head()
    # df.to_csv(r'C:\Users\ASUS\Downloads\Ikrar\Data\ETL Pipeline\ETL-Scraping-LM\Data\result.csv', index=False)