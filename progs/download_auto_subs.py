import os

urls = open("urls.txt", "r")

#Пути, необходимые для работы программы:
yt_dl_path = r"youtube-dl\youtube-dl.exe"
config_path = r"config_download_auto_subs.txt"
auto_subs_path = r"files\subs\auto_subs"

#Скачивание русских авторских субтитров по ссылке в формате vtt:
#youutbe-dl.exe --config-location config_file_path -0 vtt_file_save_path url"

sub_name = 0
for url in urls:
    sub_name = sub_name + 1
    command = yt_dl_path + " " + \
                "--config-location" + " " + config_path + " " + \
                "-o" + " " + auto_subs_path + "\\" + str(sub_name) + " " + \
                url

    os.system(command)
    #print("command: ", command)
    print("Создан файл: ", str(sub_name) + ".ru.vtt")
