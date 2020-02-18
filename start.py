from func_download_waves import download_waves
from func_format_waves import format_waves
from func_download_hand_subs import download_hand_subs
from func_download_auto_subs import download_auto_subs


#Пути, необходимые для работы программы:
yt_dl_path = r"youtube-dl\youtube-dl.exe"
config_path = r"func_download_waves.config"
wav_dir = r"files\wavs\raw"
urls_path = "urls.txt"

download_waves(urls_path, config_path, wav_dir, yt_dl_path)


#Пути, необходимые для работы программы:
wav_dir = r"files\wavs\raw"
f_wav_dir = r"files\wavs\format"
ffmpeg_path = r"ffmpeg\bin\ffmpeg.exe"

format_waves(wav_dir, f_wav_dir, ffmpeg_path)


#Пути, необходимые для работы программы:
yt_dl_path = r"youtube-dl\youtube-dl.exe"
config_path = r"func_download_hand_subs.config"
hand_subs_dir = r"files\subs\hand_subs"

download_hand_subs(hand_subs_dir, config_path, yt_dl_path)


#Пути, необходимые для работы программы:
yt_dl_path = r"youtube-dl\youtube-dl.exe"
config_path = r"func_download_auto_subs.config"
auto_subs_dir = r"files\subs\auto_subs"

download_auto_subs(auto_subs_dir, config_path, yt_dl_path)



