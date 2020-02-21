from func_create_driver import create_driver

#Функция для получения текста передачи:
def get_text(driver, file_path, url):

    #Переход по ссылке:
    driver.get(url)

    #Получение текста из параграфов:
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
    f = open(file_path, "w", encoding = "utf-8")
    for i in range(len(my_list)):
        f.write(my_list[i].text)

    f.close()

if __name__ == "__main__":

    driver = create_driver()
    
    #Максимальный размер окна браузера:
    driver.maximize_window()

    #Безголовый режим:

    #Получение текста передачи:
    get_text(driver, "text.txt", "https://echo.msk.ru/programs/code/2588256-echo/")
