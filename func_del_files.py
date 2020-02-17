#Библиотека для взаимодействия с ОС:
import os

#Функция для удаления файлов:
def del_files(dirs):

        for this_dir in dirs:
                files = os.listdir(this_dir)
                print(files)
                for file in files:
                        os.remove(this_dir + "/" + file)

if __name__ == "__main__":
        
        #Пути, необходимые для работы программы:
        
        #Звуковые файлы:
        wav_dir = r"files\wavs\raw"
        f_wav_dir = r"files\wavs\format"
        fc_wav_dir = r"files\wavs\cut"

        #Субтитры:
        hand_subs_dir = r"files\subs\hand_subs"
        auto_subs_dir = r"files\subs\auto_subs"

        #csv-файлы:
        prog_csv_dir = r"files\csv\prog_csv"
        user_csv_dir = r"files\csv\user_csv"

        #Список путей:
        dirs = [
                wav_dir, f_wav_dir, fc_wav_dir,
                hand_subs_dir, auto_subs_dir,
                prog_csv_dir, user_csv_dir
                ]
        
        del_files(dirs)
