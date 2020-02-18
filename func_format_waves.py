import os
import json

#Конвертирование аудио в формат wav 16000 Гц, 16 бит, моно:
def format_waves():

    #Получение данных из "paths.json":
    f = open("paths.json", "r")
    paths = json.loads(f.read())
    f.close

    #Запись путей в переменные:
    wav_dir = paths["wav_dir"]
    f_wav_dir = paths["f_wav_dir"]
    ffmpeg_path = paths["ffmpeg_path"]

    for wav_name in os.listdir(wav_dir):
        command = os.path.normpath(ffmpeg_path) + " " + \
                    "-i" + " " + os.path.normpath(wav_dir) + "\\" + wav_name + " " + \
                    "-ar 16000 -ac 1 -ab 256k" + " " + \
                    os.path.normpath(f_wav_dir) + "\\" + "f" + wav_name
        
##    for i in range(audio_name):
##        command = ffmpeg_path + " " + \
##                    "-i" + " " + wav_dir + "\\" + str(i + 1) + ".wav" + " " + \
##                    "-ar 16000 -ac 1 -ab 256k" + " " + \
##                    f_wav_dir + "\\" + "f" + str(i + 1) + ".wav"

        os.system(command)
        print("Создан файл: ", "f" + wav_name)

if __name__ == "__main__":

    format_waves()

    
    
