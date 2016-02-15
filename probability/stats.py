# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 11:11:18 2016

@author: peter
"""

import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import re

url = "http://lib.stat.cmu.edu/DASL/Datafiles/AlcoholandTobacco.html"

result = requests.get(url)
content = result.content

soup = bs(content, "html.parser")
stats = str(soup.find("pre"))

data = stats.splitlines()
data = [i.split(',') for i in data]

striped_data = []

for d in data:  
    strip = d[0]
    striped = re.split(r'\t+', strip)
    striped_data.append(striped)
    
striped_data = striped_data[1:-2]

column_names = striped_data[0]
data_rows = striped_data[1::]
df = pd.DataFrame(data_rows, columns=column_names)

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

sd = max(df['Alcohol']) - min(df['Alcohol'])
sd_tobacco = max(df['Tobacco']) - min(df['Tobacco'])

print("Alcohol mean: %s" % df['Alcohol'].mean())
print("Alcohol median: %s" % df['Alcohol'].median())
print("Tobacco mean: %s" % df['Tobacco'].mean())
print("Tobacco median: %s" % df['Tobacco'].median())
print("Range: %s" % sd)
print("Standard Deviation: %s" % df['Alcohol'].std())
print("Variance: %s" % df['Alcohol'].var())
print("Range Tobacco: %s" % sd_tobacco)
print("Standard Deviation Tobacco: %s" % df['Tobacco'].std())
print("Variance Tobacco: %s" % df['Tobacco'].var())

    
        

