#Модуль для взаимодействия с ОС:
import os

#Конвертирование аудио в формат wav 16000 Гц, 16 бит, моно:
def format_waves(wav_dir, f_wav_dir, ffmpeg_path):
    for i in range(audio_name):
        command = ffmpeg_path + " " + \
                    "-i" + " " + wav_dir + "\\" + str(i + 1) + ".wav" + " " + \
                    "-ar 16000 -ac 1 -ab 256k" + " " + \
                    f_wav_dir + "\\" + "f" + str(i + 1) + ".wav"

        os.system(command)
        print("Создан файл: ", str(audio_name) + ".wav")

if __name__ == "__main__":

    #Пути, необходимые для работы программы:
    wav_dir = r"files\wavs\raw"
    f_wav_dir = r"files\wavs\format"
    ffmpeg_path = r"ffmpeg\bin\ffmpeg.exe"

    format_waves(wav_dir, f_wav_dir, ffmpeg_path)

    
    
