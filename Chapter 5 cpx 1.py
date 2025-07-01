# Chapter 5 cpx lab-1
# Functions

from adafruit_circuitplayground import cp
import time

WHITE = (20, 20, 20)
OFF = (0, 0, 0)
MAX = 300
TIME = .1

def scale(light):
    maxIndex = 9
    index = int(light / MAX * maxIndex)
    return index


def led_pix_on(pixel_on):
    cp.pixels[pixel_on] = WHITE


def led_pix_off(pixel_off):
        cp.pixels[pixel_off] = OFF


def main():
    while True:
        light = cp.light
        print((light,))
        time.sleep(TIME)
        index = scale(light)
        led_pix_on(index)
        time.sleep(TIME)
        led_pix_off(index)
main()
