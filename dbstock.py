import pymongo
from bs4 import BeautifulSoup
import requests

class connectDB(object):
    def __init__(self,database,table):
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = self.myclient[database]
        self.mytable = self.mydb[table]
        if self.mydb and self.mytable:
            print("connect Success")


    def insert(self,id=None,code=None,name=None,price=None,endprice=None):
        index = 'cospi'+id
        if self.mytable.count_documents({'_id':index}):
            self.updateDB(id,code,name,price,endprice)
        else:
            self.mylist = [
                {"_id":"cospi"+id,"code":code,"name":name,"price":price,"endprice":endprice}
            ]
            x = self.mytable.insert_many(self.mylist)
            print("Inserted!")


    def print_all(self):
        for row in  self.mytable.find():
            print(row)

    def printDB(self,id):
        index = 'cospi'+id
        row = self.mytable.find_one({'_id':index})
        return row

    def updateDB(self,id=None,code=None,name=None,price=None,endprice=None):
        index = 'cospi'+id
        myquery = {'_id':index}
        newvalues = {"$set":{"code":code,"name":name,"price":price,"endprice":endprice}}
        self.mytable.update_one(myquery,newvalues)
        print("updated!")

# db1 = connectDB('admin','stocks')
# # db1.insert('test','test','test','test','test')
# db1.printDB('test')
