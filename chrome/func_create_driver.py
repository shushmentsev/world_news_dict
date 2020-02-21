from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#Путь к драйверу:
driver_path = "D:/Anton Shushmencev/19.02.20/progs/chrome_driver/chromedriver.exe"

#Опции для драйвера:
options = Options()

#Получение драйвера:
def create_driver():
    driver = webdriver.Chrome( \
            options = options, \
            executable_path = driver_path, \
            )

    return driver
