#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 通常コンテンツの撮影タイミング(秒)
NORMAL_CONTENT_SHOT_TIMES = [31, 55, 94]

# ショートコンテンツの撮影タイミング(秒)
SHORT_CONTENT_SHOT_TIMES = [6, 20, 27]

# 最後の１枚の撮影開始時刻からディレクトリ移動開始時刻の時間(秒)
OFFSET_DIRECTORY_MOVE = 5

# ディレクトリ移動開始時刻から時刻合わせ開始時刻の時間(秒)
OFFSET_TIME_ADJUST = 5

# 画像の保存先パス
#IMAGE_SAVE_DIR_PATH = '../sandbox'
IMAGE_SAVE_DIR_PATH = '/home/techlab/repo/ex-techlab-a-ss18-photo/cam_folder'

# USBシリアルポートのパス
#USB_SERIAL_PORT = '/dev/tty.usbserial-FT2GFQB6'
USB_SERIAL_PORT = '/dev/ttyS0'

# シリアル通信のボーレート
SERIAL_BAUD_RATE = 38400

# シリアル通信のタイムアウト時間
SERIAL_TIME_OUT = 0.05

# コピーのリトライ回数
COPY_RETRY_COUNT = 10

# テスト撮影用の撮影タイミング
TEST_SHOT_TIMES = [5, 10, 15]

