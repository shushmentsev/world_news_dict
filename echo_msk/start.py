#Функция для получения драйвера:
from func_create_driver import create_driver

#Функция для получения текста со страницы и записи его в файл:
from func_get_text_in_file import get_text_in_file

#Функция для получения ссылки на видео со страницы сайта:
from func_get_yt_url import get_yt_url

#Получение списка страниц из файла:
urls = []
f = open("echo_msk_urls.txt", "r", encoding = "utf-8")
for url in f:
    urls.append(url.replace("\n", ""))
f.close()

#Получение драйвера:
driver = create_driver()

for i in range(len(urls)):

    #Получение текста со страницы и запись его в файл:
    get_text_in_file(driver, str(i + 1) + ".txt", urls[i])

    #Получение ссылки на видео:
    yt_url = get_yt_url(driver, urls[i])

    #Запись ссылки на видео в файл:
    f = open("url_" + str(i + 1) + ".txt", "w", encoding = "utf-8")
    f.write(yt_url)
    f.close()
