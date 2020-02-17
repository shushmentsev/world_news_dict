import os

#Пути, необходимые для работы программы:
wav_path = r"files\wavs\raw"
f_wav_path = r"files\wavs\format"
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
