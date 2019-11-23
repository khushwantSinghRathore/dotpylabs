import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.bewakoof.com/desi-collection')
print(req.status_code)
# print(req.content)

bs = BeautifulSoup(req.content,'html.parser')
# print(bs.prettify())
fp = open("fileName.csv","w")
fp.write('t-shirt , price , image')


for i in bs.find_all('div',{'class' : 'productCardBox'}):
    for Tname in bs.find_all('div',{'class' : 'productCarDetail'}):
        
        print(str(Tname.find_all('h3')[0].text))
        print(str(Tname.find_all('b')[0].text))
        fp.write(str(Tname.find_all('h3')[0].text))
        fp.write(',')
        fp.write(str(Tname.find_all('b')[0].text))
        fp.write(',')

        
    for img in bs.find_all('div',{'class' : 'productCardImg'}):
        fp.write(str(img.find_all('img').text))
        fp.write('\n')



