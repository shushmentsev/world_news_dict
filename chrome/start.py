#Создаёт пользователей "Гугл Хрома"
#Заходит в определённый профиль на всех вкладках в каждом окне браузера

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import os

# chromedriver binary
driver_path = os.getcwd() + 'chrome_driver/chromedriver.exe'

options = Options()

options.binary_location = "chromium/bin/chrome.exe"

driver = webdriver.Chrome( \
        options = options, \
        executable_path = "chrome_driver/chromedriver.exe", \
        )

driver.maximize_window()
driver.get("https://echo.msk.ru/programs/code/2588256-echo/")

#Получение кнопки "Присоединиться / Войти":
continue_flag = True
while continue_flag:
    try:
        print('Попытка нажатия на кнопку "Присоединиться / Войти"')

        #Нажатие на кнопку "Присоединиться / Войти":
        yt_button = driver.find_element_by_xpath('//*[@id="player_uid_607712792_1"]/div[4]/button')
        yt_button.click()

    except:
        print("Исключение")

##            except NoSuchElementException:
##                print("Исключение: NoSuchElementException")
##
##            except ElementNotInteractableException:
##                print("Исключение: ElementNotInteractableException")

    else:
        print('Нажал на кнопку "Присоединиться / Войти"')
        continue_flag = False






