import os
import json

urls = open("urls.txt", "r")

#Скачивание русских авторских субтитров по ссылке в формате vtt:
#youutbe-dl.exe --config-location config_file_path -0 vtt_file_save_path url"

def download_auto_subs():

    #Получение данных из "paths.json":
    f = open("paths.json", "r")
    paths = json.loads(f.read())
    f.close

    #Запись путей в переменные:
    yt_dl_path = paths["yt_dl_path"]
    config_path = paths["config_download_auto_subs"]
    auto_subs_dir = paths["auto_subs_dir"]
    
    sub_name = 0
    for url in urls:
        sub_name = sub_name + 1
        command = os.path.normpath(yt_dl_path) + " " + \
                    "--config-location" + " " + os.path.normpath(config_path) + " " + \
                    "-o" + " " + os.path.normpath(auto_subs_dir) + "\\" + str(sub_name) + " " + \
                    url

        os.system(command)
        print("Создан файл: ", str(sub_name) + ".ru.vtt")

if __name__ == "__main__":

    download_auto_subs()
