# -*- coding: utf-8 -*-

from pathlib import Path

DIR_SRC = Path(__file__).parent.resolve()

DIR_WAV = DIR_SRC / "files" / "waves" / "raw"
DIR_F_WAV = DIR_SRC / "files" / "waves" / "format"

PTH_FFMPEG = DIR_SRC / "ffmpeg" / "bin" / "ffmpeg.exe"