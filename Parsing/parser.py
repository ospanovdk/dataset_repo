from os import times_result
from urllib import request, response
import requests
from bs4 import BeautifulSoup
from time import sleep


headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0"}
def get_url():

    # sleep(0)
    url="https://tengrinews.kz/"
    response=requests.get(url,headers=headers)
    soup=BeautifulSoup(response.text,"lxml")
    data=soup.find("div", class_="tn-main-news-grid").find_all(class_="tn-main-news-item")


    for i in data:
        # span=i.find("span",class_="tn-main-news-title").text
        # time=i.find("ul",class_="tn-data-list").text.replace("\n","")
        # seen=i.find("span",class_="tn-text-preloader-dark").text
        href="https://tengrinews.kz" +i.find("a").get("href")
        yield href
#         print(href)
# get_url()


def array():

    for card_url in get_url():
        print(card_url)
        response=requests.get(card_url,headers=headers)
    # #     # sleep(1)
        soup=BeautifulSoup(response.text,"lxml")
    #     print(soup)
    #     break
        data=soup.find("div",class_="tn-comment-list")

        # text=data.find("div",class_="tn-comment-item-content-text")
        print(data)
        break

        # theme=data.find("span",class_="tn-content-title").text

        # describe=data.find("article",class_="tn-news-text").text.replace("\t","")
        # url_image="https://tengrinews.kz/"+data.find("img").get("src")

        # print(theme,describe,url_image,end="")
 
array()



# image=soup.find("div",class_="tn-image-container")
# jpg=image.find("img",loading="lazy").get("scr")
