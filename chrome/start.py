#Создаёт пользователей "Гугл Хрома"
#Заходит в определённый профиль на всех вкладках в каждом окне браузера

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import os

# chromedriver binary
driver_path = os.getcwd() + 'chrome_driver/chromedriver.exe'

options = Options()

#options.binary_location = "D:/Anton Shushmencev/19.02.20/progs/chromium/chrome.exe"

driver = webdriver.Chrome( \
        options = options, \
        executable_path = "D:/Anton Shushmencev/19.02.20/progs/chrome_driver/chromedriver.exe", \
        )

driver.maximize_window()
driver.get("https://echo.msk.ru/programs/code/2588256-echo/")

#Получение кнопки "Присоединиться / Войти":
continue_flag = True
my_list = []
while continue_flag:
    try:
        #Получение текста передачи:
        my_list = driver.find_elements_by_tag_name("p")
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

continue_flag = True
while continue_flag:
    try:
        #Получение текста передачи:
        title = driver.find_element_by_tag_name("title")
        print("Спарсил название вкладки")

    except:
        print("Исключение")

    else:
        print("Else")
        continue_flag = False
        
print(title.text)

