import pymongo
from bs4 import BeautifulSoup
import requests
import dbstock


stockDB = dbstock.connectDB('admin','stock_code')
col = stockDB.printDB('code')
print("col:{}".format(col['code']))
result = col['code'].split()

print(result)
# for index in result:
#     print(index)
