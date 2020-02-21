from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#Путь к драйверу:
driver_path = "D:/Anton Shushmencev/world_news_dict/progs/chrome_driver/chromedriver.exe"

#Опции для драйвера:
options = Options()

#Отключение загрузки изображений:
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)

#Максимальный размер окна:
options.add_argument("--start-maximized")

#Безголовый режим:
options.add_argument("headless")



#Получение драйвера:
def create_driver():
    driver = webdriver.Chrome( \
            options = options, \
            executable_path = driver_path, \
            )

    return driver

if __name__ == "__main__":

    #Получение драйвера:
    driver = create_driver()

    #Переход на сайт:
    driver.get("https://www.google.com/")
