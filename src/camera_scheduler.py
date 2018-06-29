#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import os
import subprocess
import sched
import time

def get_unique_name(date: datetime.datetime):
    """時刻から一意に識別可能な文字列を生成する
    
    Arguments:
        date {datetime.datetime} -- 時刻
    
    Returns:
        [str] -- 一意に識別可能な文字列
    """
    unique_name = date.strftime("%Y%m%d_%H%M%S")
    return unique_name


def make_unique_name_directory():
    """現在時刻に基づいた名前のディレクトリを生成する

    Returns:
        [str] -- ディレクトリ名
    """
    date = datetime.datetime.now()
    dir_name = get_unique_name(date)
    if not os.path.isdir('./' + dir_name):
        os.mkdir(dir_name)
    return dir_name


def print_timestamp(module_name:str):
    """ デバッグ用 タイムスタンプを表示する
    
    Arguments:
        module_name {str} -- 関数名など
    """
    print("===== ", module_name, " =====")
    date = datetime.datetime.now()
    print(date)


def shot_and_download(dir_name: str, file_name: str):
    """ 撮影とダウンロードを実行する
    
    Arguments:
        dir_name {str} -- 保存先ディレクトリ名 (カレントディレクトリ下のディレクトリ)
        file_name {str} -- 画像名
    """
    print_timestamp("shot_and_download")
    
    shot_cmd = ['bash', 'cam_shot.sh', dir_name + '/' + file_name]
    try:
        res = subprocess.check_call(shot_cmd)
    except:
        print("CalledProcessError")
        exit()


def connect_cam():
    """ カメラと接続する
    """
    print_timestamp("shot_and_download")

    connect_cmd = ['bash', 'cam_connect.sh']
    try:
        res = subprocess.check_call(connect_cmd)
    except:
        print("CalledProcessError")
        exit()


def schedule_run():
    """ スケジューラ実行時から指定した時間後に登録した関数を実行する
    """
    print_timestamp("schedule_run")
    s = sched.scheduler(time.time, time.sleep)
    dir_name = make_unique_name_directory()
    print("schedule_run start")
    s.enter(1,  1, connect_cam)
    s.enter(5,  2, shot_and_download, kwargs={'dir_name':dir_name, 'file_name':'pic_01_' + dir_name + '.jpg'})
    s.enter(10, 2, shot_and_download, kwargs={'dir_name':dir_name, 'file_name':'pic_02_' + dir_name + '.jpg'})
    s.enter(15, 2, shot_and_download, kwargs={'dir_name':dir_name, 'file_name':'pic_03_' + dir_name + '.jpg'})
    print_timestamp("run!!")
    s.run()


def main():
    print_timestamp("main")
    schedule_run()

if __name__ == "__main__":
    main()
