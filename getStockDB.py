import pymongo
from bs4 import BeautifulSoup
import requests
import dbstock
import time
stockDB = dbstock.connectDB('admin','stocks')

def compare_price(now_price,default_price):
    #(현재가격-기존가격)/기존가격 *100 == 퍼센트 이익율
    now_price>=default_price
    result = (now_price - default_price)/default_price*100
    return round(result,2)

#폭등주 찾기 함수
def find_soaring_stocks(changes):
    pass

def delete_comma(number):
    result = number.split(',')
    string = ''.join(result)
    return int(string)

class Stock(object):
    @staticmethod
    def market(type):
        if type == "Naver":
            return Naver()
        if type == "Daum":
            return Daum()
        assert 0 , "incorrect access" + type


class Naver(Stock):
    def stock(self,code):
        url = "https://finance.naver.com/item/sise.nhn?code={}".format(code)
        r = requests.get(url)
        data = r.text
        soup = BeautifulSoup(data,'html.parser')

        stockName = soup.findAll('div',{'class':'wrap_company'})
        stockPirce = soup.find(id='_nowVal')
        stockEndPrice = soup.findAll('span',{'class':'tah p11'})

        name = stockName[0].h2.a.string
        price = stockPirce.string
        endprice = stockEndPrice[2].string

        #stockDB.insert(code,code,name,price,endprice)
        col=stockDB.printDB(code)
        if col['endprice']==None:
            pass
        else:
            changes = compare_price(delete_comma(price),delete_comma(col['endprice']))
            now_changes = compare_price(delete_comma(price),delete_comma(col['price']))


        print('이름:{}'.format(col['name']))
        print('비교시작가:{}'.format(col['price']))
        print('현재가:{}'.format(price))
        print('전일종가:{}'.format(col['endprice']))
        print('전일 종가 대비 등락률:{}'.format(changes) )
        print('오늘 시작 대비 등락률:{}'.format(now_changes) )
        print("\n")

class Daum(Stock):
    @staticmethod
    def updateStock(code):
        url = "http://finance.daum.net/item/quote.daum?code={}".format(code)
        r = requests.get(url)
        data = r.text
        soup = BeautifulSoup(data,'html.parser')
        stockName = soup.find(id='topWrap')
        stockPrice = soup.findAll('em',{'class':'curPrice'})
        stockEndPrice = soup.findAll('dd',{'class':'txt_price'})

        name = stockName.div.h2.string
        price = stockPrice[0].string
        endprice = stockEndPrice[0].string

        stockDB.insert(code,code,name,price,endprice)

    def stock(self,code):

        url = "http://finance.daum.net/item/quote.daum?code={}".format(code)
        r = requests.get(url)
        data = r.text
        soup = BeautifulSoup(data,'html.parser')
        stockName = soup.find(id='topWrap')
        stockPrice = soup.findAll('em',{'class':'curPrice'})
        stockEndPrice = soup.findAll('dd',{'class':'txt_price'})

        name = stockName.div.h2.string
        price = stockPrice[0].string
        endprice = stockEndPrice[0].string

        # stockDB.insert(code,code,name,price,endprice)
        col=stockDB.printDB(code)
        if col['endprice'] !=None:
            changes = compare_price(delete_comma(price),delete_comma(col['endprice']))
            now_changes = compare_price(delete_comma(price),delete_comma(col['price']))

            if now_changes > 2:
                print('이름:{}'.format(col['name']))
                print('비교시작가:{}'.format(col['price']))
                print('현재가:{}'.format(price))
                print('전일종가:{}'.format(col['endprice']))
                print('전일 종가 대비 등락률:{}'.format(changes) )
                print('오늘 시작 대비 등락률:{}'.format(now_changes) )
                print("\n")


def main():

    stockDB = dbstock.connectDB('admin','stock_code')
    col = stockDB.printDB('code')
    stockCodeArr = col['code'].split()

    # print(stockCodeArr)
    stock1= Stock.market("Daum")
    # i=0
    # for code in stockCodeArr:
    #     stock1.updateStock(code)
    #     print("num{} code{}".format(i,code))
    #     i += 1

    while True:
        for code in stockCodeArr:
            stock1.stock(code)
        print("\n")


if __name__ == "__main__":
    main()
    #compare_price(408740,414500)
