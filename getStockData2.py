
from bs4 import BeautifulSoup
import requests


stockCodeArr = ['238490','023440', '014825', '039130', '000660']

def stock(code):
    url = "https://finance.naver.com/item/sise.nhn?code={}".format(code)
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data,'html.parser')

    stockName = soup.findAll('div',{'class':'wrap_company'})
    stockPirce = soup.find(id='_nowVal')
    stockEndPrice = soup.findAll('span',{'class':'tah p11'})
    # print('이름:{}'.format(stockName[0].h2.a.string))
    # print('현재가격:{}'.format(stockPirce.string))
    # print('전일종가:{}\n'.format(stockEndPrice[2].string))

for codenumbers in stockCodeArr:
    stock(codenumbers)

class stocks(object):
    firstPrice = None
    name = None
    price = 0

    def __init__(self,code):
        self.url= "https://finance.naver.com/item/sise.nhn?code={}".format(code)
        r = requests.get(self.url)
        data = r.text
        soup = BeautifulSoup(data,'html.parser')
        stockName = soup.findAll('div',{'class':'wrap_company'})
        stockPrice = soup.find(id='_nowVal')
        stockEndPrice = soup.findAll('span',{'class':'tah p11'})
        self.name = stockName[0].h2.a.string
        self.price = stockPrice.string
        self.firstPrice = stockEndPrice[2].string


    def getstocks(self):
        print("이름:{} 현재가:{} 전일종가{}".format(self.name,self.price,self.firstPrice))

stock1 = stocks('007390')
stock1.getstocks()
