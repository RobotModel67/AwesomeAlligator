from machine import Pin
import time

p = Pin(2, Pin.OUT)

def toogle(max):
    lap = 0

    while(lap < max):
        p.value(1)
        time.sleep(0.5)
        p.value(0)
        time.sleep(0.5)
        lap += 1

toogle(20)