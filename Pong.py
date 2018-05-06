#!/usr/bin/env python3

import time
import RPi.GPIO as GPIO

from LEDControl import LEDControl
from MatrixField import MatrixField


GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def start():
    led_control = LEDControl()

    while True:
        for n in range(len(field.ledList)):
            # TODO very hard coded ...
            row = int(n / 16)
            col = int(n % 16)

            field_col = col
            field_row = row
            if col < 8 and row >= 8:
                field_col = col + 8
                field_row = row - 8
            if row < 8 and col >= 8:
                field_col = col - 8
                field_row = row + 8

            led_control.set_led(row + 1,
                                col + 1,
                                led_control.SWITCH_ON if field.is_led_active(field_row, field_col) else led_control.SWITCH_OFF)
        led_control.repaint()

        key_stroke = -1
        if not GPIO.input(17):
            key_stroke = ord('w')
        if not GPIO.input(22):
            key_stroke = ord('s')

        field.next_cycle(key_stroke)

        time.sleep(0.01)


field = MatrixField(16)

try:
    start()
except KeyboardInterrupt:
    print("Game quit.")
