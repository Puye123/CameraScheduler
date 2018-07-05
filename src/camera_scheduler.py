#!/usr/bin/env python
# -*- coding: utf-8 -*-
import env
import datetime
import os
import subprocess
import sched
import time
import shutil

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


def shot_and_download(dir_name: str, file_prefix: str):
    """ 撮影とダウンロードを実行する
    
    Arguments:
        dir_name {str} -- 保存先ディレクトリ名 (カレントディレクトリ下のディレクトリ)
        file_name {str} -- 画像プレフィックス名
    """
    print_timestamp("shot_and_download")

    pic_name = get_unique_name(datetime.datetime.now())
    
    shot_cmd = ['bash', 'cam_shot.sh', dir_name + '/' + file_prefix + pic_name + '.jpg']
    try:
        res = subprocess.check_call(shot_cmd)
    except:
        print("CalledProcessError")
        connect_cam()


def connect_cam():
    """ カメラと接続する
    """
    print_timestamp("connect_cam")

    connect_cmd = ['bash', 'cam_connect.sh']
    try:
        res = subprocess.check_call(connect_cmd)
    except Exception as ex:
        print(ex)
        #exit()

def move_dir(dir_name: str, dst_path: str):
    """ ディレクトリを移動する
    
    Arguments:
        dir_name {str} -- ディレクトリ名
        dst_path {str} -- 移動先のパス
    """
    print_timestamp("move_dir")
    
    # 所定回数まではコピーが成功するまでretryする
    for i in range(0, env.COPY_RETRY_COUNT):
        try:
            shutil.copytree('./' + dir_name, dst_path + '/' + dir_name)
            break
        except Exception as ex:
            print (ex)
            print("[Warn] Cannot copy: Retry...")
            # コピー先のディレクトリを削除して次のリトライ処理に備える
            if os.path.exists(dst_path + '/' + dir_name):
                try:
                    shutil.rmtree(dst_path + '/' + dir_name)
                except Exception as ex:
                    print (ex)

    try:
        shutil.rmtree('./' + dir_name)
    except Exception as ex:
        print (ex)


def time_adjustment():
    """ 時刻合わせ実行
    """
    print_timestamp("time_adjustment")
    time_adj_cmd = ['sudo', 'ntpdate', '-B', 'ntp.nict.jp']
    try:
        res = subprocess.check_call(time_adj_cmd)
    except:
        print("Time Adjustment Error")
        #exit()


def schedule_run(shot_times):
    """ スケジューラ実行時から指定した時間後に登録した関数を実行する
    
    Arguments:
        shot_times -- 撮影タイミング（秒）
    """
    
    print_timestamp("schedule_run")
    if len(shot_times) == 0:
        print("invalid param: shot_times is empty")
        return

    s = sched.scheduler(time.time, time.sleep)
    dir_name = make_unique_name_directory()
    image_save_dir_path = '../sandbox'

    s.enter(1, 1, connect_cam)

    count = 1
    for shot_time in shot_times:
        s.enter(shot_time,  2, shot_and_download, kwargs={'dir_name':dir_name, 'file_prefix':'pic_' + str(count) + '_'})
        count += 1
    
    move_dir_time = max(shot_times) + env.OFFSET_DIRECTORY_MOVE
    s.enter(move_dir_time, 2, move_dir, kwargs={'dir_name': dir_name, 'dst_path': image_save_dir_path})

    time_adjustment_time = move_dir_time + env.OFFSET_TIME_ADJUST
    s.enter(time_adjustment_time, 3, time_adjustment)
    print_timestamp("run!!")
    s.run()


def main():
    print_timestamp("main")
    schedule_run(env.TEST_SHOT_TIMES)


if __name__ == "__main__":
    main()
