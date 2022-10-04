# print("Hello World!")

# a=int(input("Введите первое число -  "))
# b=int(input("Введите второе число -  "))

# def sum():
#     S=pow(a*b,2)
#     M=a^2+b^2
#     if S>M:
#         print("Сумма квадратов больше!")
#     else:
#         print("Квадрат суммы чисел больше!")
# sum()


# №1 a=int(input("Введите стаж работы - "))
# b=int(input("Введите сумму зарплаты - "))
# if a>=2 and a<5:
#     b=b*1.02
#     print("Надбавка составит - ",b,"+2%")
# elif a>=5 and a<10:
#     b=b*1.05
#     print("Надбавка составит - ",b,"+5%")
# else:
#     print("На ваш не рассчитан надбавка!")



# a=int(input("Начальная сумма товара - "))
# if a>=500 and a<1000:
#     sum=a*0.95
#     print("The price with sale will be 5%- ",sum )
# elif a>1000:
#     sum=a*0.9
#     print("The price with sale will be 10%- ",sum )


# from random import randint
# n=int(input())
# a=[randint(10,12) for i in range(n)]
# print(a)
# max1=1
# k=1
# for i in range(1,n):
#     if a[i]==a[i-1]:
#         k+=1
#     else:
#         if k>=max1:
#             max1=k
#         k=1
# if k>max1:
#     max1=k
# print(max1)

# from random import randint 
# n=int(input("Введите длину массива - "))
# a=[randint(-10,10) for i in range(n)]
# print(a)
# count_chet=0
# count_nechet=0
# for i in a:
#     if i%2==0:
#         count_chet+=1
#     else:
#         count_nechet+=1
# print("Chetnyie -",count_chet)
# print("NeChetnyie -",count_nechet)
# if count_chet> count_nechet:
#     print("Четных цифр больше!")
# else:
#     print("Reverse")

# from random import randint
# from tkinter import N 
# n=int(input("Введите сколько строк должен содержать массив - "))
# m=int(input("Введите сколько столбцов должен содержать массив - "))
# a=[[randint(-10,10) for j in range(m)]  for i in range(n)]
# print(a)
# mas=[]
# for i in range(n):
#     for j in range(m):
#         mas[i][j]=a[i][j]
#     print(mas,end=" ")

# from sys import unraisablehook
# import requests
# from bs4 import BeautifulSoup

# url="https://quotes.toscrape.com/"
# response= requests.get(url)
# soup=BeautifulSoup(response.text, 'lxml')
# quotos=soup.find_all('span',class_='text')
# for quot in quotos:
#     print(quot.text)

number = 1
 
while number < 5:
    print(f"number = {number}")
    number 
print("Работа программы завершена")