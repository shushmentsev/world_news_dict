import os
import json

#Скачивание аудио по ссылке и в формате wav:
#youutbe-dl.exe --config-location config_file_path -0 wav_file_save_path url"

def download_waves():

    #Получение данных из "paths.json":
    f = open("paths.json", "r")
    paths = json.loads(f.read())
    f.close

    #Запись путей в переменные:
    urls_path = paths["urls_path"]
    wav_dir = paths["wav_dir"]
    yt_dl_path = paths["yt_dl_path"]
    config_path = paths["config_download_waves"]
    
    urls = open(urls_path, "r")
    
    audio_name = 0
    for url in urls:
        audio_name = audio_name + 1
        command = os.path.normpath(yt_dl_path) + " " + \
                    "--config-location" + " " + os.path.normpath(config_path) + " " + \
                    "-o" + " " + os.path.normpath(wav_dir) + "\\" + str(audio_name) + ".wav" + " " + \
                    url

        os.system(command)
        print("Создан файл: ", str(audio_name) + ".wav")


if __name__ == "__main__":
    
    download_waves()
