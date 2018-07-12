#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial
import env
from camera_scheduler import schedule_run, print_timestamp
from pysyslog import make_logger

make_logger("cam_serial")
def main():

  print_timestamp("START")
  #_serial_device_port = '/dev/tty.usbserial-FT2J6I04' #使用製品が確定したら書き直す
  _serial_device_port = env.USB_SERIAL_PORT

  with serial.Serial(_serial_device_port,env.SERIAL_BAUD_RATE,timeout=env.SERIAL_TIME_OUT) as ser:
    _evt = {
        'original':{  # 制御装置から送られてくる電文
          b'R00\r':"stop",
          b'R01\r':"normal start",
          b'R02\r':"normal start",
          b'R03\r':"short version",
          b'R09\r':"Black screen",
          },
        'judge':{  # 動作判定用の文言
          b'R00':"stop",
          b'R01':"normal start",
          b'R02':"normal start",
          b'R03':"short version",
          b'R09':"Black screen",
          }
        }

    cur_cmd  = b''
    _SHOOT_FLG = b'R01'

    while True:
      line = ser.readline()
      cur_cmd = line
      go_cmd = cur_cmd.rstrip()

      if go_cmd  in _evt['judge']:
        print_timestamp(_evt['judge' ][ go_cmd ])
        # do something
        if _evt['judge'][go_cmd] == "normal start":
          ser.close()
          schedule_run(env.NORMAL_CONTENT_SHOT_TIMES)
          ser = serial.Serial(_serial_device_port,env.SERIAL_BAUD_RATE,timeout=env.SERIAL_TIME_OUT)
          logger.info("start serial : %s"%(go_cmd))
        elif _evt['judge'][go_cmd] == "short version":
          ser.close()
          schedule_run(env.SHORT_CONTENT_SHOT_TIMES)
          ser = serial.Serial(_serial_device_port,env.SERIAL_BAUD_RATE,timeout=env.SERIAL_TIME_OUT)
          logger.info("start serial : %s"%(go_cmd))
      else:
        pass
 


if __name__ == "__main__":
    main()

