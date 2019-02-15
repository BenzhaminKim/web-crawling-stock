
from bs4 import BeautifulSoup
import requests


stockCodeArr = ['002210','014825','008730']


def stocks(code):
    url = "http://finance.daum.net/item/quote.daum?code={}".format(code)
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data,'html.parser')

    stockName = soup.find(id='topWrap')
    stockPrice = soup.findAll('em',{'class':'curPrice'})
    stockEndPrice = soup.findAll('dd',{'class':'txt_price'})
    print('이름:{}'.format(stockName.div.h2.string))
    print('현재가격:{}'.format(stockPrice[0].string))
    print('전일종가:{}\n'.format(stockEndPrice[0].string))

for codenumbers in stockCodeArr:
    stocks(codenumbers)
