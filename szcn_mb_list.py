# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 21:41:09 2017

@author: lenovo
"""

import urllib.request as request
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time
import sys



url = 'http://www.szse.cn/main/mainboard/ssgsxx/ssgslb/'

driver = webdriver.Chrome(r'C:\Users\lenovo\Anaconda3\pkgs\chromedriver-2.33-h6c80334_0\Library\bin\chromedriver')
driver.get(url)


mb_table = []

page=0
while page < 48:
    soup = bs(driver.page_source, 'html.parser')
    mb_table.append(soup.findAll('tr', {'bgcolor':['#F8F8F8', '#ffffff']}))
    driver.find_element_by_class_name('cls-navigate-next').click()
    page += 1
    time.sleep(2)
    
mb_lst = []

f = open('sz_mb.csv', 'w')

for i in (range(len(mb_table))):
    for j in range(len(mb_table[i])):
        code = mb_table[i][j].td.u.text.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding)
        short_name = mb_table[i][j].findAll('td')[1].u.text.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding)
        full_name = mb_table[i][j].findAll('td')[2].text.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding)
        industry = mb_table[i][j].findAll('td')[3].text.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding)
        website = mb_table[i][j].findAll('td')[4].text.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding)
        mb_lst.append({'code': code , 'short_name': short_name , 'full_name': full_name, 'industry': industry, 'website': website})
        f.write(code +','+ short_name +','+ full_name + ',' +industry + ',' + website + '\n') 
f.close()


        
    

