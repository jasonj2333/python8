#!/usr/bin/env python3
from pyfirmata import Arduino, util
from time import sleep

board = Arduino('COM7') # Change to your port
print("Start blinking D13")
while True:
    board.digital[13].write(1)
    sleep(1)
    board.digital[13].write(0)
    sleep(1)
