import os

urls = open("urls.txt", "r")

#Пути, необходимые для работы программы:
yt_dl_path = r"youtube-dl\youtube-dl.exe"
config_path = r"config_download_wavs.txt"
wav_path = r"files\wavs\raw"
f_wav_path = r"files\wavs\format"

#Скачивание аудио по ссылке и в формате wav:
#youutbe-dl.exe --config-location config_file_path -0 wav_file_save_path url"

audio_name = 0
for url in urls:
    audio_name = audio_name + 1
    command = yt_dl_path + " " + \
                "--config-location" + " " + config_path + " " + \
                "-o" + " " + wav_path + "\\" + str(audio_name) + ".wav" + " " + \
                url

    os.system(command)
    #print("command: ", command)
    print("Создан файл: ", str(audio_name) + ".wav")

#Пути, необходимые для работы программы:
ffmpeg_path = r"ffmpeg\bin\ffmpeg.exe"

#Конвертирование аудио в формат wav 16000 Гц, 16 бит, моно:
for i in range(audio_name):
    command = ffmpeg_path + " " + \
                "-i" + " " + wav_path + "\\" + str(i + 1) + ".wav" + " " + \
                "-ar 16000 -ac 1 -ab 256k" + " " + \
                f_wav_path + "\\" + "f" + str(i + 1) + ".wav"

    os.system(command)
    #print("command: ", command)
    print("Создан файл: ", str(audio_name) + ".wav")
