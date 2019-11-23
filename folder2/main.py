import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.bewakoof.com/desi-collection')
print(req.status_code)
# print(req.content)

bs = BeautifulSoup(req.content,'html.parser')

print(bs.prettify())