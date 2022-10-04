# import requests
# from bs4 import BeautifulSoup


# url="https://tengrinews.kz/kazakhstan_news/situatsiyu-kazahstansko-rossiyskoy-granitse-478548/"
# response=requests.get(url)
# soup=BeautifulSoup(response.text,"lxml")
# data=soup.find("div",class_="tn-article-grid")
# name=data.find("a",class_="tn-article-title").text
# time=data.find("time").text
# ul=soup.find("ul", class_="tn-list")
# seen=ul.find("span",class_="tn-text-preloader-dark").text
# print(name , time, seen)


import xlsxwriter
from comments import array
def writer(parametr):
    book=xlsxwriter.Workbook(r"C:\Users\Дулат\Projects_in_Python\data.xlsx")

    page=book.add_worksheet("новости")

    row=0
    column=0

    page.set_column("A:A",20)
    page.set_column("B:B",20)
    page.set_column("C:C",20)
    # page.set_column("D:D",20)

    for  item in parametr():
        page.write(row,column,item[0])
        page.write(row,column+1,item[1])
        page.write(row,column+2,item[2])

        row+=1

    book.close()   

writer(array)

