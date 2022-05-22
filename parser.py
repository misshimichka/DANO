import requests
from bs4 import BeautifulSoup

address = "https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%93%D0%BE%D1%80%D0%BE%D0%B4%D0%B0_%D0%BD%D0%B0_%D1%80%D0%B5%D0%BA%D0%B0%D1%85"
response = requests.get(address)
tag = response.content.decode()


soup = BeautifulSoup (tag, 'html.parser')
x = soup.find_all("a")[5:-80]

for i in x:
    addr = "https://ru.wikipedia.org"
    addr += i.get("href")
    response = requests.get(addr)
    a_1 = response.content.decode()
    soup1 = BeautifulSoup(a_1, 'html.parser')
    x1 = soup1.find_all("a")[5:-53]
    for j in x1:
        if j.get("title") is not None:
            print(j.get("title"))
