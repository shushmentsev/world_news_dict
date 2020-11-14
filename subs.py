#Дописывать "\n\n" в файл субтитров!!! ?

#Библиотека для взаимодействия с ОС:
import os
import json

# import io

 #Функция для нарезки звуковых файлов:
from cut_f_wav import cut_f_wav

# Функция для вычисления разницы двух времён:
from func_time_delta import time_delta

# Функция для создания списков: [время начала фразы, время конца фразы, фраза]
from func_create_time_list import create_time_list

from conf import DIR_F_WAV, DIR_FC_WAV, DIR_H_SUBS, DIR_A_SUBS, DIR_P_CSV, DIR_U_CSV

def cut_f_waves_and_create_csv_files():

    # Получение данных из "paths.json":
    # f = open("paths.json", "r")
    # paths = json.loads(f.read())
    # f.close
    
    f_wav_names = os.listdir(DIR_F_WAV)
    h_subs_names = os.listdir(DIR_H_SUBS)
    a_subs_names = os.listdir(DIR_A_SUBS)

    print(DIR_F_WAV)
    print(f_wav_names)

    # Функция:
    def my_func(name, time_list_h_subs):

        # TODO: Добавить проверки на существование папок prog_csv и user_csv!!!
        # TODO: Добавить проверку на существование папки cut в папке waves!!!

        csv_path = str(DIR_P_CSV) + r"\\" + name + ".csv"
        csv_path = os.path.normpath(csv_path)

        csv_f = open(csv_path, "w", encoding="utf-8")

        #
        for i in range(len(time_list_h_subs[0])):
            t_point = time_list_h_subs[0][i]
            t_delta = str(time_delta(time_list_h_subs[1][i], time_list_h_subs[0][i]))

            #

            f_wav_path = str(DIR_F_WAV) + r"\\" + name + ".wav"

            fc_wav_path = str(DIR_FC_WAV) + r"\\" + \
                          name + "c" + str(i + 1) + ".wav"

            cut_f_wav(t_point, t_delta, f_wav_path, fc_wav_path)

            # Запись в файл "name.csv":

            csv_s = fc_wav_path + ";" + str(os.path.getsize(fc_wav_path)) + ";" + time_list_h_subs[2][i] + "\n"
            csv_f.write(csv_s)

        # Закрытие файла:
        csv_f.close()
    
    # Ручные субтитры:
    time_list_h_subs = []
    for h_sub_name in h_subs_names:

        # Создание списка [время начала фразы, время конца фразы, фраза]:
        time_list_h_subs = create_time_list(str(DIR_H_SUBS) + r"\\" + h_sub_name)

        my_func("f1", time_list_h_subs)

    # Автоматические субтитры:
    # time_list_a_subs = []
    # for a_sub_name in a_subs_names:
    #
    #     time_list_a_subs = create_time_list(str(DIR_H_SUBS) + r"\\" + a_sub_name)

    print("TIME_LISTS:")
    print(time_list_h_subs)
    # print(time_list_a_subs)
    # print(time_list_h_subs[0][0])
    # print(time_list_h_subs[0][1])
    # print(time_list_h_subs[0][2])

    # for i in range(len(time_list_h_subs[0])):
    #
    #     # # TODO: Добавить проверки на существование папок prog_csv и user_csv!!!
    #     # # TODO: Добавить проверку на существование папки cut в папке waves!!!
    #     #
    #     # prog_csv_name = "p" + str(i + 1) + ".csv"
    #     # prog_csv_path = str(DIR_P_CSV) + r"\\" + prog_csv_name
    #     # prog_csv_path = os.path.normpath(prog_csv_path)
    #     #
    #     # prog_f = open(prog_csv_path, "w", encoding = "utf-8")
    #     #
    #     # user_csv_name = "u" + str(i + 1) + ".csv"
    #     # user_csv_path = str(DIR_U_CSV) + r"\\" + user_csv_name
    #     # user_csv_path = os.path.normpath(user_csv_path)
    #     #
    #     # user_f = open(user_csv_path, "w", encoding = "utf-8")
    #
    #     # Нарезка файлов:
    #     for j in range(len(time_list_h_subs[0])):
    #
    #         t_point = time_list_h_subs[0][j]
    #         t_delta = str(time_delta(time_list_h_subs[1][j], time_list_h_subs[0][j]))
    #
    #         print(f_wav_names[i])
    #
    #         f_wav_path = str(DIR_F_WAV) + r"\\" + f_wav_names[i]
    #
    #         fc_wav_path = str(DIR_FC_WAV) + r"\\" + \
    #                       f_wav_names[i].replace(".wav", "") + \
    #                       "c" + str(j + 1) + ".wav"
    #
    #         cut_f_wav(t_point, t_delta, f_wav_path, fc_wav_path)
    #
    #         #Запись в файл "name.csv":
    #
    #         prog_s = fc_wav_path + ";" + str(os.path.getsize(fc_wav_path)) + ";" + time_list_h_subs[i][2][j] + "\n"
    #         prog_f.write(prog_s)
    #
    #         user_s = fc_wav_path + ";" + t_delta + ";" + time_list_h_subs[i][2][j] + "\n"
    #         user_f.write(user_s)
    #
    #     prog_f.close()
    #     user_f.close()

if __name__ == "__main__":
    
    cut_f_waves_and_create_csv_files()
