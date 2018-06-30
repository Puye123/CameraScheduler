#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
import sys
from random import randint

def workA():
    print("workA", time.time())
    # Something to do

def workB():
    print("workB", time.time())
    # Something to do

def workC():
    print("workC", time.time())
    # Something to do

def _callback(future):
    print("done!")

loop = asyncio.get_event_loop()
future = loop.create_future()
future.add_done_callback(_callback)
loop.
loop.call_soon(eternal_hello, loop)  # add
result = loop.run_until_complete(future)
print(result)
loop.close()