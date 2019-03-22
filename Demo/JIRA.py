# -*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    target = 'https://sapjira.wdf.sap.corp/projects/FPA64'
    req = requests.get(url=target, verify=False)
    print(req.text)