from dataclasses import dataclass
from os import times_result
from urllib import request, response
import requests
from bs4 import BeautifulSoup
from time import sleep

url="https://tengrinews.kz/kazakhstan_news/iin-rossiyan-rech-ministra-musina-astaninskom-tsone-snyali-479104/"
response=requests.get(url)
soup=BeautifulSoup(response.text,"lxml")
data=soup.find_all("div",class_="tn-tape-item")


def array():
    for i in data:
        img_url="https://tengrinews.kz"+i.find("a",class_="tn-tape-title").get("href")
        desc=i.find("a",class_="tn-tape-title").text
        time=i.find("time").text 
        yield desc,time, img_url

array()
# text=data.find("a",class_="tn-tape-title")
