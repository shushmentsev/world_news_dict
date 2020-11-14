import os

#Скачивание русских авторских субтитров по ссылке в формате vtt:
#youutbe-dl.exe --config-location config_file_path -0 vtt_file_save_path url"

from conf import PTH_YT_DL, PTH_CONF_DL_H_SUBS, DIR_H_SUBS

def download_hand_subs():

    urls = open("urls.txt", "r")
    
    sub_name = 0
    for url in urls:
        sub_name = sub_name + 1
        command = os.path.normpath(PTH_YT_DL) + " " + \
                    "--config-location" + " " + os.path.normpath(PTH_CONF_DL_H_SUBS) + " " + \
                    "-o" + " " + os.path.normpath(DIR_H_SUBS) + "\\" + str(sub_name) + " " + \
                    url

        os.system(command)
        print("Создан файл: ", str(sub_name) + ".ru.vtt")

if __name__ == "__main__":

    download_hand_subs()
