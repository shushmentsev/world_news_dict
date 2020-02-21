#Функция для получения драйвера:
from func_create_driver import create_driver

#Функция для получения текста со страницы и записи его в файл:
from func_get_text_in_file import get_text_in file

#Функция для получения ссылки на видео со страницы сайта:
from func_get_yt_url import get_yt_url

#Получение списка страниц из файла:
urls = []
f = open("echo_msk_urls.txt", "r", encoding = "utf-8")
for url in f:
    urls.append(url)
f.close()

#\n

#Получение драйвера:

#Получение текста со страницы и запись его в файл:
get_text_in_file(driver, "1.txt", "https://echo.msk.ru/programs/code/2588256-echo/")



