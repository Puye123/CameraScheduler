#!/bin/bash

# PTPCameraプロセスをkillする
ps axuwww | grep "gvfs-gphoto2-volume-monitor" | grep -v "grep" | awk '{ print "kill -9 ", $2}' | sh
ps axuwww | grep "gvfsd-gphoto2" | grep -v "grep" | awk '{ print "kill -9 ", $2}' | sh


# カメラと接続する
connect_cmd="gphoto2 --auto-detect"
eval $connect_cmd
