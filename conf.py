# -*- coding: utf-8 -*-

from pathlib import Path

# Корневая папка:
DIR_SRC = Path(__file__).parent.resolve()

# Пути к программам:
PTH_FFMPEG = DIR_SRC / "ffmpeg" / "bin" / "ffmpeg.exe"
PTH_YT_DL = DIR_SRC / "youtube-dl" / "youtube-dl.exe"

# Пути к аудиофайлам:
DIR_WAV = DIR_SRC / "files" / "waves" / "raw"
DIR_F_WAV = DIR_SRC / "files" / "waves" / "format"
DIR_FC_WAV = DIR_SRC / "files" / "waves" / "cut"

# Пути к субтитрам:
DIR_H_SUBS = DIR_SRC / "files" / "subs" / "hand_subs"
DIR_A_SUBS = DIR_SRC / "files" / "subs" / "auto_subs"
DIR_VTT = DIR_SRC / "files" / "subs" / "hand_subs"

# Пути к CSV-файлам:
DIR_P_CSV = DIR_SRC / "files" / "csv" / "prog_csv"
DIR_U_CSV = DIR_SRC / "files" / "csv" / "user_csv"

# Пути к конфигам:
PTH_CONF_DL_WAVES = DIR_SRC / "func_download_waves.config"
PTH_CONF_DL_H_SUBS = DIR_SRC / "func_download_hand_subs.config"
PTH_CONF_DL_A_SUBS = DIR_SRC / "func_download_auto_subs.config"