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
$ python camera_scheduler.py
```

## Install
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
