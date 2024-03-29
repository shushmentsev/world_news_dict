#Дописывать "\n\n" в файл субтитров!!! ?

#Библиотека для взаимодействия с ОС:
import os
import json

#import io

#Функция для нарезки звуковых файлов:
from func_cut_f_wav import cut_f_wav

#Функция для вычисления разницы двух времён:
from func_time_delta import time_delta

#Функция для создания списков: [время начала фразы, время конца фразы, фраза]
from func_create_time_list import create_time_list



def cut_f_waves_and_create_csv_files():

    #Получение данных из "paths.json":
    f = open("paths.json", "r")
    paths = json.loads(f.read())
    f.close

    #Запись путей в переменные:
    f_wav_dir = paths["f_wav_dir"]
    fc_wav_dir = paths["fc_wav_dir"]
    vtt_dir = paths["vtt_dir"]
    prog_csv_dir = paths["prog_csv_dir"]
    user_csv_dir = paths["user_csv_dir"]
    
    f_wav_names = os.listdir(f_wav_dir)
    vtt_names = os.listdir(vtt_dir)
    
    #Создание списка списков [время начала фразы, время конца фразы, фраза]:
    time_list = []
    for vtt_name in vtt_names:
        
        time_list.append(create_time_list(vtt_dir + r"\\" + vtt_name))

    for i in range(len(time_list)):

        prog_csv_name = "p" + str(i + 1) + ".csv"
        prog_csv_path = prog_csv_dir + r"\\" + prog_csv_name

        prog_f = open(prog_csv_path, "w", encoding = "utf-8")

        user_csv_name = "u" + str(i + 1) + ".csv"
        user_csv_path = user_csv_dir + r"\\" + user_csv_name

        user_f = open(user_csv_path, "w", encoding = "utf-8")
        

        for j in range(len(time_list[i][0])):
            
            t_point = time_list[i][0][j]
            t_delta = str(time_delta(time_list[i][1][j], time_list[i][0][j]))

            print(f_wav_names[i])

            f_wav_path = f_wav_dir + r"\\" + f_wav_names[i]
            
            fc_wav_path = fc_wav_dir + r"\\" + \
                          f_wav_names[i].replace(".wav", "") + \
                          "c" + str(j + 1) + ".wav"
            
            cut_f_wav(t_point, t_delta, f_wav_path, fc_wav_path)

            #Запись в файл "name.csv":

            prog_s = fc_wav_path + ";" + str(os.path.getsize(fc_wav_path)) + ";" + time_list[i][2][j] + "\n"
            prog_f.write(prog_s)

            user_s = fc_wav_path + ";" + t_delta + ";" + time_list[i][2][j] + "\n"
            user_f.write(user_s)

    prog_f.close()
    user_f.close()

if __name__ == "__main__":
    
    cut_f_waves_and_create_csv_files()
