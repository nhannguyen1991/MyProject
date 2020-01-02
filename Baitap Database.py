# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 19:01:23 2019

@author: nhan.nguyen
"""
import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=VNM1903L0008;'
                      'Database=QUAN_LY_NHAN_VIEN;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()



f = open("C:\\Users\\nhan.nguyen\\Documents\\1. Python\\IMic\\Buoi 11\\DATA_FILE.txt")
data = f.read()

class Product:
    productId = "";
    productName = "";
    productPrice = "";
    productQty ="";
    #hàm tạo mặc định
    def __init__(self):
        pass

import re
listProduct = re.split('{SAN_PHAM|}SAN_PHAM',data)
listProduct = list(filter(None,listProduct))
listProduct = list(filter(lambda x: x != '\n', listProduct))

#print(listProduct)
productTable=[]
for i in range(len(listProduct)):
    p = listProduct[i]
    listAttribute = p.split('\n')
    listAttribute = list(filter(None, listAttribute));
    product = Product()
    #print(listAttribute)
    for j in range(len(listAttribute)):
        productAtribute = listAttribute[j].split(': ')
        if productAtribute[0] == "ID_SP":
            product.productId = productAtribute[1]
        if productAtribute[0] == "TEN_SP":
            product.productName = productAtribute[1]
        if productAtribute[0] == "GIA_SP":
            product.productPrice = productAtribute[1].replace(',','')[:-3]
        if productAtribute[0] == "SL_SP":
            product.productQty = productAtribute[1]
    productTable.append(product)

#for p in productTable:
    #print(p.productId ,"---",p.productName,"---",p.productPrice,"---",p.productQty)
cursor.execute("delete from PRODUCT")
for p in productTable:
    col1 = p.productId
    col2 = p.productName
    col3 = p.productPrice
    col4 = p.productQty
    s="INSERT INTO PRODUCT VALUES('"+col1+"', '"+col2+"', '"+col3+"', "+col4+")"
    
    #print(s)
    cursor.execute(s)
    conn.commit()

cursor.execute("select*from dbo.PRODUCT")

for row in cursor:
    print(row)
print("Done!!")  
    
    
    
    