from func_create_driver import create_driver

#Функия для получения ссылки на видео со страницы передачи:
def get_yt_url(driver, url):

    #Переход по ссылке:
    driver.get(url)

    #Получение элемента:
    i_frame = driver.find_element_by_css_selector("#mmread > div > iframe")

    #Получение ссылки на видео:
    yt_url = i_frame.get_attribute("src")

    #Возвращение ссылки на видео:
    return yt_url

if __name__ == "__main__":

    #Получение драйвера:
    driver = create_driver()

    #Получение ссылки на видео:
    yt_url = get_yt_url(driver, "https://echo.msk.ru/programs/code/2588256-echo/")

    #Вывод результата:
    print("Ссылка на видео: ", yt_url)
