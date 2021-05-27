import requests, hashlib
from bs4 import BeautifulSoup

url = "PAST YOUR URL HERE"

s = requests.session()
response = s.get(url)

soup = BeautifulSoup(response.content, "lxml")

str = soup.h3.string
hash = hashlib.md5(str.encode()).hexdigest()

myobj = {'hash' : hash}

flag = s.post(url, date = myobj)

print(output.text)
