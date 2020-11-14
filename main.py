from dl_waves import download_waves
from f_waves import format_waves
from dl_h_subs import download_hand_subs
from dl_a_subs import download_auto_subs
from get_csv import cut_f_waves_and_create_csv_files

# Скачивание звуковых файлов:
download_waves()

# Форматирование звуковых файлов:
format_waves()

# Скачивание авторских субтитров:
download_hand_subs()

# Скачивание автоматических субтитров:
download_auto_subs()

# Нарезка звуковых файлов на фразы и создание csv-файлов:
cut_f_waves_and_create_csv_files()
