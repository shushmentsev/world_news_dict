import os

#Скачивание аудио по ссылке и в формате wav:
#youutbe-dl.exe --config-location config_file_path -0 wav_file_save_path url"

def download_waves(urls_path, config_path, wav_dir, yt_dl_path):

    urls = open(urls_path, "r")
    
    audio_name = 0
    for url in urls:
        audio_name = audio_name + 1
        command = yt_dl_path + " " + \
                    "--config-location" + " " + config_path + " " + \
                    "-o" + " " + wav_dir + "\\" + str(audio_name) + ".wav" + " " + \
                    url

        os.system(command)
        print("Создан файл: ", str(audio_name) + ".wav")


if __name__ == "__main__":
    
    #Пути, необходимые для работы программы:
    yt_dl_path = r"youtube-dl\youtube-dl.exe"
    config_path = r"func_download_wavs.config"
    wav_dir = r"files\wavs\raw"
    urls_path = "urls.txt"

    download_waves(urls_path, config_path, wav_dir, yt_dl_path)
