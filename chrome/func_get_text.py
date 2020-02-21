from func_create_driver import create_driver

#Функция для получения текста передачи:
def get_text(driver, url):

    #Переход по ссылке:
    driver.get(url)

    #Получение текста из параграфов:
    continue_flag = True
    while continue_flag:
        try:
            #Получение текста передачи:
            elements = driver.find_elements_by_css_selector("#mmread > div > div > p")
            print("Спарсил текст")

        except:
            print("Исключение")

        else:
            continue_flag = False

    #Получение списка параграфов:
    paragraphs = []
    for elem in elements:
        paragraphs.append(elem.text)

    return paragraphs

if __name__ == "__main__":

    #Получение драйвера:
    driver = create_driver()
    
    #Максимальный размер окна браузера:
    driver.maximize_window()

    #Безголовый режим:
    pass

    #Получение текста передачи:
    paragraphs = get_text(driver, "https://echo.msk.ru/programs/code/2588256-echo/")

    #print(text)

    #Запись текста передачи в файл:
    f = open("text.txt", "w", encoding = "utf-8")
    for i in range(len(paragraphs)):
        f.write(paragraphs[i])

    f.close()
