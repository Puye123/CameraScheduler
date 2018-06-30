#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial
from camera_scheduler import schedule_run

def main():

  _serial_device_port = '/dev/tty.usbserial-FT2J6I04' #使用製品が確定したら書き直す

  with serial.Serial(_serial_device_port,38400,timeout=0.05) as ser:
    _evt = {
        'original':{  # 制御装置から送られてくる電文
          b'R00\r':"stop",
          b'R01\r':"normal start",
          b'R02\r':"event no 2",
          b'R03\r':"event no 3",
          b'R09\r':"Black screen",
          },
        'judge':{  # 動作判定用の文言
          b'R00':"stop",
          b'R01':"normal start",
          b'R02':"event no 2",
          b'R03':"event no 3",
          b'R09':"Black screen",
          }
        }

    cur_cmd  = b''

    while True:
      line = ser.readline()
      cur_cmd += line

      if b'\r' in cur_cmd:
        go_cmd = cur_cmd.split('\r')[0]
        cur_cmd = cur_cmd.split('\r')[1]
      else:
        continue

      if go_cmd in _evt['judge']:
        print( _evt['judge' ][ go_cmd ] )
        # do something
        if _evt['judge'][go_cmd] == "normal start":
          schedule_run()

      else:
        print( 'unknown command' )

if __name__ == "__main__":
    main()

