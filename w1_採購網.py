import datetime
import requests
from bs4 import BeautifulSoup
import csv  
from selenium import webdriver
from selenium.webdriver.common.by import By



url = 'https://web.pcc.gov.tw/pis/'
#搜尋欄內容
org = '國土測繪中心'
org_id = '3.1.100.1'
today = datetime.date.today()
# print(today.year - 1911, today.month, today.day, sep = '/')

driver = webdriver.Chrome()
driver.get(url)
driver.find_element(By.ID, 'orgName').send_keys(org)
driver.find_element(By.ID, 'orgId').send_keys(org_id)
# driver.find_element(By.ID, "tenderStartDate").click()
# driver.find_element(By.ID, 'tenderStartDate').send_keys('113/03/01')
driver.find_element(By.ID, 'basicIsSpdtDateTypeId').click()
driver.find_element(By.ID, 'basicTenderSearchId').click()
   
    
# 開個csv
with open('testa.csv', 'w', newline = '') as f:
    writer = csv.writer(f)
    
    # 訪問權限+解析
    new_url = driver.current_url
    r = requests.get(new_url)
    sp = BeautifulSoup(r.text, 'lxml')
    
    table = sp.find('table', class_ = 'tb_01')
    rows = table.find_all('tr')
    # rows = sp.find('table', class_ = 'tb_01').tbody.find_all('tr')
    
    # 標題
    list_ = []
    ths = rows[0].find_all('th')
    for i in range(0, len(ths)-1):
        clean_data = ths[i].text.strip()
        print(clean_data, end = ' ')
        list_.append(clean_data)
    writer.writerow(list_)
        
    # 內容
    for row in rows:
        list_ = []
        tds = row.find_all('td')
        for i in range(0, len(tds)-1):
            clean_data = tds[i].text.strip()
            print(clean_data, end = ' ')
            list_.append(clean_data)
        print('\n')
        writer.writerow(list_)
        


    