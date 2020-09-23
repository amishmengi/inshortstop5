import requests
from bs4 import BeautifulSoup
inshorts_url="https://inshorts.com/en/read"
def checker() :
    response=requests.get(inshorts_url)
    soup=BeautifulSoup(response.content,'html.parser')
    for i in range(0,5):
         news1=soup.find_all('div', class_=["news-card-title news-right-box"])[i]
         title=news1.find('span',attrs={'itemprop':"headline"}).string
         y=i+1
         print(y,". ",title,sep="")       
checker()
