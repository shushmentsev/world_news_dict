import os

urls = open("urls.txt", "r")

#Скачивание русских авторских субтитров по ссылке в формате vtt:
#youutbe-dl.exe --config-location config_file_path -0 vtt_file_save_path url"

def download_auto_subs(auto_subs_dir, config_path, yt_dl_path):

    sub_name = 0
    for url in urls:
        sub_name = sub_name + 1
        command = yt_dl_path + " " + \
                    "--config-location" + " " + config_path + " " + \
                    "-o" + " " + auto_subs_dir + "\\" + str(sub_name) + " " + \
                    url

        os.system(command)
        print("Создан файл: ", str(sub_name) + ".ru.vtt")

if __name__ == "__main__":

    #Пути, необходимые для работы программы:
    yt_dl_path = r"youtube-dl\youtube-dl.exe"
    config_path = r"func_download_auto_subs.config"
    auto_subs_dir = r"files\subs\auto_subs"

    download_auto_subs(auto_subs_dir, config_path, yt_dl_path)
