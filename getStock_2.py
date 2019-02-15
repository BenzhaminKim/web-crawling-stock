
from bs4 import BeautifulSoup
from urllib.request import urlopen

def stocks(code):
    my_url = "http://finance.daum.net/item/quote.daum?code={}".format(code)
    uClient = urlopen(my_url)
    Page_html = uClient.read()
    soup = BeautifulSoup(Page_html,'html.parser')
    stockName = soup.findAll('div',{'class':'wrap_company'})
    print('이름:{}'.format(stockName[0].h2.a.string))
stocks(238490)
