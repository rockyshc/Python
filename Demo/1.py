# -*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    target = 'https://www.biqukan.com/1_1094/5403177.html'
    req = requests.get(url=target)
#    print(req.text)
    html = req.text
#    Use BeautifulSoup4
    bf = BeautifulSoup(html)
    texts = bf.find_all('div', class_ = 'showtxt')
#    print(texts)
    print(texts[0].text.replace('\xa0' * 8, '\n\n'))

