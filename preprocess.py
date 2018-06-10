
# coding: utf-8

# In[1]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from subprocess import check_output
import sys
import csv
#####
folderAddress = "input"
#####

info = pd.read_csv(folderAddress + "/sku_info.csv")

# # info 1000 rows x 5 columns id:0-999
attr = pd.read_csv(folderAddress + "/sku_attr.csv")
# # attr  6776 rows x 3 columns
sales = pd.read_csv(folderAddress + "/sku_sales.csv")
# # sales 2127485 rows x 7 columns
prom = pd.read_csv(folderAddress + "/sku_prom.csv")



# In[2]:


sales.iloc[:5]


# In[3]:


def loadCsv(address):
    with open(address) as csvDataFile:
        info=[]
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            info.append(row)
    return info[1:]


# In[4]:


def deleteCol(a,num):
    for row in a :
        del row[num]
    return a


# In[32]:


id_brand_cat_map = {}
thirdcat_id_map ={}
info=[]
attr=[]
sales=[]
prom=[]
info = loadCsv(folderAddress + "/sku_info.csv")
#delete first and second catagory


attr = loadCsv(folderAddress + "/sku_attr.csv")
sales =  loadCsv(folderAddress + "/sku_sales.csv")
prom = loadCsv(folderAddress + "/sku_prom.csv")


# In[ ]:


for i in sales:
    for k in info:
        if i[0] == k[0]:
            i.append(k[2])
            break
    


# In[ ]:


def reformatdate(a):
    temp = ''
    for i in a:
        if i=='-':
            i='/'
        temp = temp+i
    return temp


# In[ ]:


for i in sales:
    i.append('')
    i.append('')
    


# In[ ]:


index=0
num = len(sales)
for i in sales:
    index=index+1
    if index%10==0:
        print(str(index)+"/"+str(num)+" has been finished")
    
    for k in prom:
        date = reformatdate(i[2])
        if k[0] == date and k[1] == i[0]:
            i[9] = k[3]
            i[8]=1
            break
        elif k[0] == date and k[1]=='-999' and k[2]==i[-1]:
            i[9] = k[3]
            i[8]=1
            break


# In[24]:


csvfile = "sale+prom.csv"
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(sales)

