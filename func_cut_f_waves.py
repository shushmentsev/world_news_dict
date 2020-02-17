#Библиотека для взаимодействия с ОС:
import os

#Путь до файла "ffmpeg.exe":
ffmpeg_path = r"ffmpeg\bin\ffmpeg.exe"

#Время откуда резать звуковой файл:
#time_point

#Продолжительность звукового файла:
#time_delta

i = 0

def cut_f_wav(time_point, time_delta, f_wav_path, fc_wav_path):
        command = ffmpeg_path + " " + \
                  "-ss" + " " + time_point + " " \
                  "-t" + " " + time_delta + " " + \
                  "-i" + " " + f_wav_path + " " + \
                  fc_wav_path

        print(command)
        os.system(command)
