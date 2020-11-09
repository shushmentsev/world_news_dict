# -*- coding: utf-8 -*-

import os
import json

from pathlib import Path

from conf import DIR_WAV, DIR_F_WAV, PTH_FFMPEG

#Конвертирование аудио в формат wav 16000 Гц, 16 бит, моно:
def format_waves():

    # #Получение данных из "paths.json":
    # f = open("paths.json", "r")
    # paths = json.loads(f.read())
    # f.close
    #
    # #Запись путей в переменные:
    # wav_dir = paths["wav_dir"]

    # f_wav_dir = paths["f_wav_dir"]
    # ffmpeg_path = paths["ffmpeg_path"]

    # if DIR_F_WAV.is__dir():
    #     print("file exist!")
    # else:
    #     print("no such file!")

    # TODO: Сделать проверку на суцествование папки "format"!!!

    for path_wav in DIR_WAV.iterdir():
        wav_name = Path(path_wav).stem

        command = str(PTH_FFMPEG) + " " + \
            "-i" + " " + str(DIR_WAV) + "\\" + str(wav_name) + ".wav" + " " + \
            "-ar 16000 -ac 1 -ab 256k" + " " + \
            str(DIR_F_WAV) + "\\" + "f" + str(wav_name) + ".wav"

        print(command)

        try:
            os.system(command)
            print("Создан файл: ", "f" + wav_name)

        except:

            print("Исключение")

##    for i in range(audio_name):
##        command = ffmpeg_path + " " + \
##                    "-i" + " " + wav_dir + "\\" + str(i + 1) + ".wav" + " " + \
##                    "-ar 16000 -ac 1 -ab 256k" + " " + \
##                    f_wav_dir + "\\" + "f" + str(i + 1) + ".wav"

if __name__ == "__main__":

    format_waves()
    input("Нажми клавишу для завершения программы...")
