import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://www.divan.ru/category/svet"
driver.get(url)
time.sleep(3)

products = driver.find_elements(By.CSS_SELECTOR, 'div.WdR1o')

parsed_data = []

for product in products:
    try:

        title = product.find_element(By.CSS_SELECTOR, 'div.lsooF span').text
        price = product.find_element(By.CSS_SELECTOR, 'div.pY3d2 span').text
        link = product.find_element(By.CSS_SELECTOR, 'a.LlPhw').get_attribute('href')

        parsed_data.append([title, price, link])
    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")
        continue

driver.quit()

with open("divan.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название', 'Цена', 'Ссылка'])
    writer.writerows(parsed_data)
