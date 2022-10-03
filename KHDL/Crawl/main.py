from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import numpy as np
import pandas as pd
import csv


def handleArea(s: str):
    try:
        if s != '':
            return s.split(' ')[0]
        return s
    except:
        return ''


def handleType(s: str):
    try:
        return s.replace('Loại tin đăng: ', '')
    except:
        return ''


def handleAddress(s: str):
    result = ""
    if s.find(',') > 1:
        try:
            arr = s.split(',')
            for item in arr:
                if item.find('Phường') != -1 or item.find('Xã') != -1:
                    result += item.lstrip().rstrip() + ", "
            return result + arr[-2]
        except:
            return result
    else:
        return result


def handlePrice(price: str, area: str):
    result = ''
    try:
        if price != 'Thỏa thuận':
            if price.find('m²') != -1:
                if price.find('triệu') == -1:
                    result = str(float(price.split(' ')[0]) * float(area))
                else:
                    result = str(float(price.split(' ')[0]) * float(area) * 1000)
            elif price.find('tỷ') != -1:
                result = str(float(price.split(' ')[0]) * 1000)
    except:
        pass
    return result

def write_csv(row, file_name):
    with open(file_name, mode='a', newline='', encoding='utf-8-sig') as outfile:
        writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(row)

write_csv(['Title', 'Address', 'Type', 'Area', 'Price'], '1.csv')
write_csv(['Title', 'Address', 'Type', 'Area', 'Price'], '2.csv')

options = Options()
options.add_argument('--headless')
options.add_argument(
    'user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"')

raw_data = []
cleaned_data =[]

num_of_page = 100
# num_of_page = 2
for i in range(1, num_of_page + 1):
    print('Trang số', str(i))
    driver = webdriver.Chrome(
        ChromeDriverManager().install(), options=options)  # , options=options
    driver.get("https://batdongsan.com.vn/nha-dat-ban-da-nang/p" + str(i))

    elements = driver.find_elements(
        by=By.CSS_SELECTOR, value=".js__product-link-for-product-id")
    links = [el.get_attribute('href') for el in elements]

    for link in links:
        driver_detail = webdriver.Chrome(
            ChromeDriverManager().install(), options=options)
        driver_detail.get(link)
        title_detail = driver_detail.find_element(
            By.CLASS_NAME, "pr-title").get_attribute('textContent')
        address_detail = driver_detail.find_element(
            By.CLASS_NAME, "re__pr-short-description").get_attribute('textContent')
        type_detail = driver_detail.find_element(
            By.CLASS_NAME, "re__pr-specs-product-type").get_attribute('textContent')
        area_detail = ""
        price_detail = ""

        t1 = driver_detail.find_elements(
            by=By.CSS_SELECTOR, value=".re__pr-short-info > .re__pr-short-info-item > .title")
        t2 = driver_detail.find_elements(
            by=By.CSS_SELECTOR, value=".re__pr-short-info > .re__pr-short-info-item > .value")
        temp1 = [el.text for el in t1]
        temp2 = [el.text for el in t2]
        for _ in range(len(temp1)):
            if temp1[_] == 'Mức giá':
                price_detail = temp2[_]
            elif temp1[_] == 'Diện tích':
                area_detail = temp2[_]
        raw_data.append([title_detail, address_detail,
                    type_detail, area_detail, price_detail])
        write_csv([title_detail, address_detail,
                    type_detail, area_detail, price_detail], '1.csv')

        
        area_detail = handleArea(area_detail)
        price_detail = handlePrice(price_detail, area_detail)
        cleaned_data.append([title_detail, handleAddress(address_detail),
                    handleType(type_detail), area_detail, price_detail])
        write_csv([title_detail, handleAddress(address_detail),
                    handleType(type_detail), area_detail, price_detail], '2.csv')
        driver_detail.close()

    driver.close()

print(np.array(raw_data).shape)
df = pd.DataFrame(raw_data, columns=['Title', 'Address', 'Type', 'Area', 'Price'])
df.to_csv('raw_data.csv', encoding="utf-8-sig")

df1 = pd.DataFrame(cleaned_data, columns=['Title', 'Address', 'Type', 'Area', 'Price'])
df1.to_csv('cleaned_data.csv', encoding="utf-8-sig")