# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 19:55:40 2017

@author: lenovo
"""

import urllib.request as request
from bs4 import BeautifulSoup as bs
import sys
from selenium import webdriver


url = 'http://www.szse.cn/main/mainboard/ssgsxx/ssgslb/'

web = request.urlopen(url).read()

soap = bs(web, 'html.parser')

page_html = soap.findAll('input', {'class':'cls-navigate-next'})

mb_table = []
driver = webdriver.Chrome(r'C:\Users\lenovo\Anaconda3\pkgs\chromedriver-2.33-h6c80334_0\Library\bin\chromedriver')
driver.get('http://www.szse.cn/main/mainboard/ssgsxx/ssgslb/')
button = driver.find_element_by_class_name('cls-navigate-next')
button.click()

i = 0
while i < 49:
    mb_table.append(soap.findAll('tr', {'bgcolor':['#F8F8F8', '#ffffff']}))
    soap = bs(request.urlopen('http://www.szse.cn/main/mainboard/ssgsxx/ssgslb/').read(), 'html.parser')
    i += 1
    
print(len(mb_table))

'''for i in range(2,49):
    print(page_html[0]['onclick'])
    page_html[0]['vaonclicklue'] = 
    print(page_html[0]['onclick'])
    print(soap.findAll('tr', {'bgcolor':['#F8F8F8', '#ffffff']})[0])
    #mb_table.append(soap.findAll('tr', {'bgcolor':['#F8F8F8', '#ffffff']}  ))'''

#print(mb_table[1][0])



'''mb_lst = []

for i in (range(len(mb_table))):
    for j in range(len(mb_table[i])):
        code = mb_table[i][j].td.u.text
        short_name = mb_table[i][j].findAll('td')[1].u.text
        full_name = mb_table[i][j].findAll('td')[2].text
        industry = mb_table[i][j].findAll('td')[3].text
        website = mb_table[i][j].findAll('td')[4].text
        mb_lst.append({'code': code , 'short_name': short_name , 'full_name': full_name, 'industry': industry, 'website': website})'''
    

