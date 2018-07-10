#!/bin/bash

# PTPCameraプロセスをkillする
ps axuwww | grep "PTPCamera" | grep -v "grep" | awk '{ print "kill -9 ", $2}' | sh

# カメラと接続する
connect_cmd="gphoto2 --auto-detect"
eval $connect_cmd
