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

# main board stock url
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

mb_f = open('sz_mb.csv', 'w')

for i in (range(len(mb_table))):
    for j in range(len(mb_table[i])):
        code = mb_table[i][j].td.u.text.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding)
        short_name = mb_table[i][j].findAll('td')[1].u.text.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding)
        full_name = mb_table[i][j].findAll('td')[2].text.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding)
        industry = mb_table[i][j].findAll('td')[3].text.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding)
        website = mb_table[i][j].findAll('td')[4].text.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding)
        mb_lst.append({'code': str(code) , 'short_name': short_name , 'full_name': full_name, 'industry': industry, 'website': website})
        mb_f.write(code +','+ short_name +','+ full_name + ',' +industry + ',' + website + '\n') 
mb_f.close()

# create a code list
code_lst = []
industry_lst = []
short_name_lst =[]
for i in mb_lst:
    code_lst.append(i['code'])
    industry_lst.append(i['industry'])
    short_name_lst.append(i['short_name'])
    
print(len(code_lst))
print(code_lst)

# announ scrap start here  
announ_url = 'http://disclosure.szse.cn/m/search0425.jsp'
driver.get(announ_url)

announ_lst = []

total_pages = 0
lst_no = 0

no_of_listed_co = len(code_lst)

announ_f = open('announ_lst.csv', 'w')

for code in code_lst:
    print(code)
    # Start date Input
    start_date =  driver.find_element_by_name('startTime')
    start_date.clear()
    start_date.send_keys('2015-01-01')
    
    # End date Input
    end_date =  driver.find_element_by_name('endTime')
    end_date.clear()
    end_date.send_keys('2017-12-28')
    
    # Stock code Input
    stockCode = driver.find_element_by_name('stockCode')
    stockCode.clear()
    stockCode.send_keys(code)
    driver.find_element_by_name('imageField').click()
    time.sleep(2)
    
    # Read page source
    soap = bs(driver.page_source, 'html.parser')
    
    # Find how many pages 
    page_limit = soap.find_all('span')[-6].text
    page_limit = int(page_limit)
    total_pages += page_limit
    print(page_limit)
    
    i = 1
    while i < page_limit:
        soap_2 = bs(driver.page_source, 'html.parser')
        announ = soap_2.find_all('td', {'class': 'td2'})
        # scrap data - url_link, name, code number for 1 to page_limit-1
        for j in announ:
            announ_url = 'http://disclosure.szse.cn' + j.a.get('href')
            announ_name = j.a.text.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding)
            announ_lst.append({'code': code, 'announ_name': announ_name , 'announ_url': announ_url})
            announ_f.write(str(code) +','+ str(short_name_lst[lst_no]) +','+ ',' +str(industry_lst[lst_no]) + ',' + announ_name +','+ announ_url + '\n')
        driver.find_element_by_xpath('//img[@src = "images2008/next.gif"]').click()
        i += 1
        time.sleep(2)
    
    # grab the last page
    soap_3 = bs(driver.page_source, 'html.parser')
    announ = soap_3.find_all('td', {'class': 'td2'})
    # scrap data - url_link, name, code number from last page
    for j in announ:
        announ_url = 'http://disclosure.szse.cn' + j.a.get('href')
        announ_name = j.a.text.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding)
        announ_lst.append({'code': code, 'announ_name': announ_name , 'announ_url': announ_url}) 
        announ_f.write(str(code) +','+ str(short_name_lst[lst_no]) +','+ ',' +str(industry_lst[lst_no]) + ',' + announ_name +','+ announ_url + '\n')
    
    print('the last announ of ' + str(code) + ' is ' + str(announ_lst[-1]['announ_name']))
    
    no_of_listed_co-=1 
    print('still have: '+ str(no_of_listed_co)+'\n')
    
    lst_no+=1
    
    # pause for 2 second
    time.sleep(2)
    
announ_f.close()    
   
    
#End Programe
print('no. of announ: ' + str(len(announ_lst)))
print('total pages is ' + str(total_pages))
print(code_lst)
