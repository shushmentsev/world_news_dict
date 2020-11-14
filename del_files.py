# Библиотека для взаимодействия с ОС:
import os

from conf import DIR_WAV, DIR_F_WAV, DIR_FC_WAV, DIR_H_SUBS, DIR_A_SUBS, DIR_P_CSV, DIR_U_CSV


# Функция для удаления файлов:
def del_files(dirs):
    for this_dir in dirs:
        files = os.listdir(str(this_dir))
        # print(files)
        for file in files:
            os.remove(str(this_dir) + "/" + file)


if __name__ == "__main__":

    # Список папок, в которых будут удалены файлы:
    dirs = [
        DIR_WAV, DIR_F_WAV, DIR_FC_WAV,
        DIR_H_SUBS, DIR_A_SUBS,
        DIR_P_CSV, DIR_U_CSV
    ]

    del_files(dirs)
