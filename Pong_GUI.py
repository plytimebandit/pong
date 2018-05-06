#!/usr/bin/env python3

import time
from curses import wrapper

from MatrixField import MatrixField


def start():
    wrapper(main)


def main(stdscr):
    stdscr.nodelay(True)

    key_stroke = -1

    while True:
        draw_screen(stdscr)  # This is exchanged by GPIO control later on

        field.next_cycle(key_stroke)

        time.sleep(0.01)

        key_stroke = stdscr.getch()
        if key_stroke == ord('q'):
            break


def draw_screen(stdscr):
    stdscr.clear()
    counter = 0

    stdscr.addstr("+")
    stdscr.addstr("-" * field.size)
    stdscr.addstr("+")
    stdscr.addstr("\n")

    for led in field.ledList:
        if counter % field.size == 0:
            stdscr.addstr("|")
        if counter >= field.size and counter % field.size == 0:
            stdscr.addstr("\n|")
        stdscr.addstr("*" if led.isActive else " ")
        counter += 1

    stdscr.addstr("|\n")
    stdscr.addstr("+")
    stdscr.addstr("-" * field.size)
    stdscr.addstr("+\n")

    stdscr.refresh()


field = MatrixField(16)

start()


