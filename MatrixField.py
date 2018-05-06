import HumanPlayer
from Ball import Ball
from HumanPlayer import HumanPlayer
from Led import Led


class MatrixField:

    def __init__(self, size):
        self.size = size
        self.ledList = []
        self.cycle = 0

        self.ball = Ball(size - 1)
        self.humanPlayer = HumanPlayer(size / 2, size - 1)

        for i in range(0, size * size):
            self.ledList.append(Led())

    def activate(self, row, col):
        self.__get_led(row, col).activate()

    def deactivate(self, row, col):
        self.__get_led(row, col).deactivate()

    def activate_all(self):
        for led in list(filter(lambda l: not l.isActive, self.ledList)):
            led.deactivate()

    def deactivate_all(self):
        for led in list(filter(lambda l: l.isActive, self.ledList)):
            led.deactivate()

    def __get_led(self, row, col):
        if row >= self.size or col >= self.size:
            raise ValueError("'row' {} and 'col' {} must not be bigger or equals 'size' {}.".format(row, col, self.size))
        if row < 0 or col < 0:
            raise ValueError("'row' {} and 'col' {} must be bigger than 0".format(row, col, self.size))

        return self.ledList[self.size * row + col]

    def is_led_active(self, row, col):
        return self.__get_led(row, col).isActive

    def next_cycle(self, key_stroke):
        cycle = self.cycle

        for led in list(filter(lambda led: led.isFlashed, self.ledList)):
            led.deactivate()

        self.deactivate(self.ball.positionRow, self.ball.positionCol)
        self.ball.move(cycle)
        self.activate(self.ball.positionRow, self.ball.positionCol)

        for pos in self.humanPlayer.positions: self.deactivate(pos, 0)
        self.humanPlayer.move(key_stroke)
        for pos in self.humanPlayer.positions: self.activate(pos, 0)

        self.check_result()

        self.cycle += 1

    def check_result(self):
        if self.ball.positionCol != 0:
            return

        if self.ball.positionRow not in self.humanPlayer.positions:
            self.flash_leds()

    def invert_leds(self):
        for led in self.ledList:
            if led.isActive:
                led.deactivate()
            else:
                led.activate()

    def flash_leds(self):
        for led in self.ledList: led.flash()
