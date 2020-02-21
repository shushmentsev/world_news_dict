from func_create_driver import create_driver

#Функция для получения текста передачи:
def get_text_in_file(driver, file_path, url):

    #Переход по ссылке:
    driver.get(url)

    #Получение текста из параграфов:
    continue_flag = True
    while continue_flag:
        try:
            #Получение текста передачи:
            paragraphs = driver.find_elements_by_css_selector("#mmread > div > div > p")
            print("Спарсил текст")

        except:
            print("Исключение")

        else:
            continue_flag = False

    #Запись текста из параграфов в файл:
    f = open(file_path, "w", encoding = "utf-8")
    for par in paragraphs:
        f.write(par.text)

    f.close()

if __name__ == "__main__":

    #Получение драйвера:
    driver = create_driver()
    
    #Максимальный размер окна браузера:
    driver.maximize_window()

    #Безголовый режим:
    pass

    #Получение текста передачи:
    get_text_in_file(driver, "text.txt", "https://echo.msk.ru/programs/code/2588256-echo/")
