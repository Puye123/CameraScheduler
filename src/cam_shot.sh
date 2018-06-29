#!/bin/bash

# 撮影とダウンロード
shot_cmd="gphoto2 --capture-image-and-download --filename=./$1"
eval $shot_cmd
