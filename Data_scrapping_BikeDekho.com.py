#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
import time
import pandas as pd
import os
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests


# In[2]:


url="https://www.bikedekho.com/new-bikes#all_brands"


# In[3]:


driver = webdriver.Chrome(executable_path=r'C:\Users\pavan\Desktop\business analytics\chromedriver.exe')
driver.implicitly_wait(10)
driver.get(url)


# In[4]:


soup= BeautifulSoup(driver.page_source,'html.parser')


# # >>MainBikeLink

# In[6]:


soup= BeautifulSoup(driver.page_source,'html.parser')
bikelink=soup.find_all('a',{'class':'BrIconNewCar'})
bikelink


# In[7]:


# soup= BeautifulSoup(driver.page_source,'html.parser')
# bikelink=soup.find_all('a',{'class':'BrIconNewCar'})
bikelinks=[]
for i in range(len(bikelink)):
    bikelinks.append('https://www.bikedekho.com'+bikelink[i].get('href'))
bikelinks


# In[9]:


driver.get(bikelinks[0])


# In[34]:


soup= BeautifulSoup(driver.page_source,'html.parser')
bikelink=soup.find_all('div',{'class':'gsc_col-sm-12 gsc_col-xs-12 gsc_col-md-8 listView holder posS'})
bikelink


# In[41]:


# bikelink
for a in bikelink:
    divs2 = a.find_all("h3")
    for b in divs2:
        strongs = b.find_all("a")
        for c in strongs:
            print(c)
#         for strong in strongs:
#             aa = strong.find_all("a")
#             for a in aa:
#                 print(a.text)


# In[42]:


bikename=[]
for j in bikelinks:
    driver.get(j)
    soup= BeautifulSoup(driver.page_source,'html.parser')
    bikelink=soup.find_all('div',{'class':'gsc_col-sm-12 gsc_col-xs-12 gsc_col-md-8 listView holder posS'})
    for a in bikelink:
        divs2 = a.find_all("h3")
        for b in divs2:
            strongs = b.find_all("a")
            for c in strongs:
                bikename.append(c)
bikename


# In[47]:


len(bikename)


# In[88]:


b_links=[]
for i in bikename:
    b_links.append(i.get('href'))
b_links


# # >>BikeName

# In[48]:


soup= BeautifulSoup(driver.page_source,'html.parser')
bikelink=soup.find_all('div',{'class':'gsc_col-sm-12 gsc_col-xs-12 gsc_col-md-8 listView holder posS'})
bikelink


# In[ ]:


bikename=[]
for j in bikelinks:
    driver.get(j)
    soup= BeautifulSoup(driver.page_source,'html.parser')
    bikelink=soup.find_all('div',{'class':'gsc_col-sm-12 gsc_col-xs-12 gsc_col-md-8 listView holder posS'})
    for a in bikelink:
        divs2 = a.find_all("h3")
        for b in divs2:
            strongs = b.find_all("a")
            for c in strongs:
                bikename.append(c)
bikename


# In[85]:


b_name=[]
for i in bikename:
    b_name.append(i.get('title'))
b_name


# # >>Bikepower

# In[54]:


soup= BeautifulSoup(driver.page_source,'html.parser')
bikelink=soup.find_all('div',{'class':'gsc_col-sm-12 gsc_col-xs-12 gsc_col-md-8 listView holder posS'})
bikelink


# In[57]:


bikepower=[]
for j in bikelinks:
    driver.get(j)
    soup= BeautifulSoup(driver.page_source,'html.parser')
    bikelink=soup.find_all('div',{'class':'gsc_col-sm-12 gsc_col-xs-12 gsc_col-md-8 listView holder posS'})
    for a in bikelink:
        divs2 = a.find_all("div",{'class':'clearfix'})
        for b in divs2:
            strongs = b.find_all("div",{'class':'dotlist'})
            for c in strongs:
                weak= c.find_all('span')
                for d in strongs:
                    bikepower.append(d)
bikepower


# In[84]:


b_power=[]
for i in bikepower:
    b_power.append(i.text)
b_power


# # >>Bikeprice

# In[73]:


soup= BeautifulSoup(driver.page_source,'html.parser')
bikelink=soup.find_all('div',{'class':'gsc_col-sm-12 gsc_col-xs-12 gsc_col-md-8 listView holder posS'})
bikelink


# In[79]:


bikeprice=[]
for j in bikelinks:
    driver.get(j)
    soup= BeautifulSoup(driver.page_source,'html.parser')
    bikelink=soup.find_all('div',{'class':'gsc_col-sm-12 gsc_col-xs-12 gsc_col-md-8 listView holder posS'})
    for a in bikelink:
        divs2 = a.find_all("div",{'class':'price'})
        for b in divs2:
            bikeprice.append(b)
#             strongs = b.find_all('span',{'class':'icon-cd_R'})
#             for c in strongs:
#                 bikeprice.append(c)
bikeprice


# In[81]:


b_price=[]
for i in bikeprice:
    b_price.append(i.text)
b_price


# # Csv_combine

# In[100]:


Main_bike_dekho_data = pd.DataFrame({'Bikelinks': b_links,'Bikename': b_name,'Bikepower': b_power,'Bike_price':b_price})
Main_bike_dekho_data


# In[101]:


Main_bike_dekho_data.to_csv('Main_bike_dekho_data.csv')

