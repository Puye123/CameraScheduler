#!/usr/bin/env python
# -*- coding: utf-8 -*-

# schedを試す

import sched
import time

s = sched.scheduler(time.time, time.sleep)

def workA():
    print("workA", time.time())
    # Something to do

def workB():
    print("workB", time.time())
    # Something to do

def workC():
    print("workC", time.time())
    # Something to do


def schedule_run():
    print("schedule_run start")
    s.enter(5, 1, workA)
    s.enter(10, 1, workB)
    s.enter(15, 1, workC)
    s.run()


if __name__ == "__main__":
    schedule_run()

    # 以下のprint函数が呼ばれるのは全てのスケジュールが実行されたあと
    print ("aaa")
