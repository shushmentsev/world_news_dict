from func_download_waves import download_waves
from func_format_waves import format_waves
from func_download_hand_subs import download_hand_subs
from func_download_auto_subs import download_auto_subs
from subs import cut_f_waves_and_create_csv_files

#Загрузка звуковых файлов:
download_waves()

#Скачивание авторских субтитров:
download_hand_subs()

#Скачивание автоматических субтитров:
download_auto_subs()

#Форматирование звуковых файлов:
format_waves()

#Нарезка звуковых файлов на фразы и создание csv-файлов:
cut_f_waves_and_create_csv_files()
