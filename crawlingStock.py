from bs4 import BeautifulSoup
import requests

url = "https://www.naver.com/"
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data,'html.parser')

print(soup)
# title = soup.findAll('span',{'class':'td_t'})
# print(title[0].string)
