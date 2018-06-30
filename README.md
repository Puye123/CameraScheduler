CameraScheduler
====

カメラの定期撮影を行うスクリプト

## Description
以下の処理を順に行います
* PCに接続されたカメラとconnectします
* 1回目の撮影
* 2回目の撮影
* 3回目の撮影
* 撮影した画像を日付を名前とするディレクトリに格納します

## Demo
camera_scheduler.pyの実行した時のコンソール表示
```
$ python camera_scheduler.py
=====  main  =====
2018-06-30 11:26:17.983791
=====  schedule_run  =====
2018-06-30 11:26:17.983836
=====  run!!  =====
2018-06-30 11:26:17.984114
=====  connect_cam  =====
2018-06-30 11:26:18.989351
Model                          Port
----------------------------------------------------------
Canon EOS 5D Mark IV           usb:020,007
=====  shot_and_download  =====
2018-06-30 11:26:37.990039
New file is in location /capt0000.jpg on the camera
Saving file as ./20180630_112617/pic_01_20180630_112617.jpg
Deleting file /capt0000.jpg on the camera
=====  shot_and_download  =====
2018-06-30 11:27:01.986164
New file is in location /capt0000.jpg on the camera
Saving file as ./20180630_112617/pic_02_20180630_112617.jpg
Deleting file /capt0000.jpg on the camera
=====  shot_and_download  =====
2018-06-30 11:27:54.991042
New file is in location /capt0000.jpg on the camera
Saving file as ./20180630_112617/pic_03_20180630_112617.jpg
Deleting file /capt0000.jpg on the camera
=====  move_dir  =====
2018-06-30 11:28:02.989703
=====  time_adjustment  =====
2018-06-30 11:28:07.989483
30 Jun 11:28:15 ntpdate[2089]: adjust time server 133.243.238.244 offset 0.006618 sec
```

## Requirement
### gphoto2
http://www.gphoto.org  
このスクリプトはgphoto2のコマンドを利用しています

### Equipment
以下の環境で動作を確認しています
#### OS
macOS High Sierra ver. 10.13.5
#### python
3.6.4
#### gphoto2
2.5.17
#### camera
* EOS 5D MarkⅣ
* EOS 8000D(760D)

## Usage
```
$ python3 camera_scheduler.py
```
または
```
$ python camera_scheduler.py
```

## Install
### python
#### mac
ターミナルで以下を実行
```
$ brew install python3
```

```
$ pip install pyserial
```
### gphoto2
#### mac
ターミナルで以下を実行
```
$ brew install gphoto2
```
バージョンを確認
```
$ gphoto2 --version
```
## Contribution

## Licence

[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)

## Author

[Puye123](https://github.com/Puye123)
