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

from conf import DIR_F_WAV, DIR_FC_WAV, DIR_VTT, DIR_P_CSV, DIR_U_CSV

def cut_f_waves_and_create_csv_files():

    #Получение данных из "paths.json":
    # f = open("paths.json", "r")
    # paths = json.loads(f.read())
    # f.close
    
    f_wav_names = os.listdir(DIR_F_WAV)
    vtt_names = os.listdir(DIR_VTT)
    
    #Создание списка списков [время начала фразы, время конца фразы, фраза]:
    time_list = []
    for vtt_name in vtt_names:
        
        time_list.append(create_time_list(str(DIR_VTT) + r"\\" + vtt_name))

    print("TIME_LIST:")
    print(time_list)

    for i in range(len(time_list)):

        # TODO: Добавить проверки на существование папок prog_csv и user_csv!!!
        # TODO: Добавить проверку на существование папки cut в папке waves!!!

        prog_csv_name = "p" + str(i + 1) + ".csv"
        prog_csv_path = str(DIR_P_CSV) + r"\\" + prog_csv_name
        prog_csv_path = os.path.normpath(prog_csv_path)

        prog_f = open(prog_csv_path, "w", encoding = "utf-8")

        user_csv_name = "u" + str(i + 1) + ".csv"
        user_csv_path = str(DIR_U_CSV) + r"\\" + user_csv_name
        user_csv_path = os.path.normpath(user_csv_path)

        user_f = open(user_csv_path, "w", encoding = "utf-8")

        for j in range(len(time_list[i][0])):
            
            t_point = time_list[i][0][j]
            t_delta = str(time_delta(time_list[i][1][j], time_list[i][0][j]))

            print(f_wav_names[i])

            f_wav_path = str(DIR_F_WAV) + r"\\" + f_wav_names[i]
            
            fc_wav_path = str(DIR_FC_WAV) + r"\\" + \
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
