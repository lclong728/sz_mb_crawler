# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 20:46:34 2018

@author: lenovo
"""

import matplotlib.pyplot as plt
import numpy as np
import re

# Open data file
All_announ = []

# Extract file to a list of dict
'''for i in announ_lst.readlines():
    a = i.spilt(',')
    code = a[0]
    com_name = a[1]
    industry = a[2]
    announ = a[3]
    announ_url= a[4]
    All_announ.append({'code': code, 'short_name': com_name, 'industy': industry, 'announ_name': announ , 'announ_url': announ_url})
'''    
class Search_Engine:
    
    def __init__(self, file_name):
        self.load_data(file_name)
        
    def Load_data(self, file_name):
        with open(file_name, 'r') as data:
            self.orginial_data = data.readlines()
               
        self.auunoun_lst = []
        for shock in self.orginial_data:
            info = shock.spilt(',')
            code = info[0]
            com_name = info[1]
            industry = info[2]
            announ = info[3]
            announ_url= info[4]
            self.auunoun_lst.append({'code': code, 'short_name': com_name, 'industy': industry, 'announ_name': announ , 'announ_url': announ_url})

    def Filter(self, filter_cond):
        for key in filter_cond.keys():
            
            if key == 'code':
                
                
        
    


