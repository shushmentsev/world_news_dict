from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import time

import os

#Путь к драйверу:
driver_path = "D:/Anton Shushmencev/19.02.20/progs/chrome_driver/chromedriver.exe"

#Опции для драйвера:
options = Options()

#Получение драйвера:
driver = webdriver.Chrome( \
        options = options, \
        executable_path = driver_path, \
        )

#Максимальный размер окна браузера:
driver.maximize_window()

#Безголовый режим:

#Переход по ссылке:
driver.get("https://echo.msk.ru/programs/code/2588256-echo/")

#Получение текста передачи:
continue_flag = True
my_list = []
while continue_flag:
    try:
        #Получение текста передачи:
        my_list = driver.find_elements_by_css_selector("#mmread > div > div > p")
        print("Спарсил текст")

    except:
        print("Исключение")

    else:
        continue_flag = False

#Запись текста передачи в файл:
f = open("text.txt", "w", encoding = "utf-8")
for i in range(len(my_list)):
    f.write(my_list[i].text)

f.close()

#Получение ссылки на видео:
i_frame = driver.find_element_by_css_selector("#mmread > div > iframe")
yt_url = i_frame.get_attribute("src")
print("Ссылка на видео: ", yt_url)

