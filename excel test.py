# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 18:35:59 2017

@author: lenovo
"""

import pandas

df = pandas.read_excel('sz_cn.xlsx')
#print the column names
print (len(df))
print(df.loc[1])
f = open("sz_mb.txt", 'w')

#for i in range(len(df)):
#    f.write(df.loc[i])

f.close()
    
#get the values for a given column
#values = df['A股代码'].values
#get a data frame with selected columns
#FORMAT = ['Arm_id', 'DSPName', 'Pincode']
#df_selected = df[FORMAT]
#print(df_selected)