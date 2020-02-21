from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import time

import os

import json

from func_create_driver import create_driver

def get_urls(url):
    driver.get(url)

    #Задержка, чтобы страница успела прогрузиться:
    time.sleep(5)

    #Получение ссылок на статьи:
    my_list = driver.find_elements_by_css_selector("#archive > div.rel > div > div > div.mediamenu > a.watch.iblock")

    page_urls = []
    #Вывод полученных ссылок:
    for i in range(len(my_list)):
        page_urls.append(my_list[i].get_attribute("href"))

    return page_urls

#Получение ссылки на видео:
def get_yt_url():
    i_frame = driver.find_element_by_css_selector("#mmread > div > iframe")
    yt_url = i_frame.get_attribute("src")
    print("Ссылка на видео: ", yt_url)

if __name__ == "__main__":
    driver = create_driver()
    
    #Максимальный размер окна браузера:
    driver.maximize_window()

    #Безголовый режим:
    
    #Получение ссылок на страницы:
    pages = []

    #Открытие файла "urls.txt":
    f = open("urls.txt", "w", encoding = "utf-8")
    
    for i in range(40):
        url = "https://echo.msk.ru/programs/code/archive/" + str(i + 1) + "/"
        print("Код доступа. Страница " + str(i + 1) + ":")
        urls = get_urls(url)

        #Запись текста передачи в файл:
        for i in range(len(urls)):
            f.write(urls[i] + "\n")
        
        
        #Вывод ссылок на страницы:
        for i in range(len(urls)):
            print(urls[i])

        print("\n")

    #Закрытие файла "urls.txt":
    f.close()
        
