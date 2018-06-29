#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import os
import subprocess

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


def main():
    # カメラと接続する
    connect_cmd = ['bash', 'cam_connect.sh']
    try:
        res = subprocess.check_call(connect_cmd)
    except:
        print("CalledProcessError")
        exit()
    
    # ディレクトリを作って撮影した画像をそこにいれる
    dir_name = make_unique_name_directory()
    shot_cmd = ['bash', 'cam_shot.sh', dir_name + '/test.jpg']
    try:
        res = subprocess.check_call(shot_cmd)
    except:
        print("CalledProcessError")
        exit()

if __name__ == "__main__":
    main()
