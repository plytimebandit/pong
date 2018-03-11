#!/usr/local/bin/python3

import random
import time
from curses import wrapper

from MatrixField import MatrixField


def start():
    wrapper(main)


def main(stdscr):
    stdscr.nodelay(True)

    while True:
        # row = random.randint(0, field.size - 1)
        # col = random.randint(0, field.size - 1)
        #
        # field.deactivate_all()
        # field.activate(row, col)

        draw_screen(stdscr)

        field.nextCycle()

        time.sleep(0.1)

        if stdscr.getch() == ord('q'):
            break


def draw_screen(stdscr):
    stdscr.clear()
    counter = 0
    for led in field.ledList:
        if counter % field.size == 0:
            stdscr.addstr("\n")
        stdscr.addstr("*" if led.isActive else " ")
        counter += 1
    stdscr.refresh()


field = MatrixField(16)

start()


