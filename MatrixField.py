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

        return self.ledList[self.size * row + col]

    def nextCycle(self, keyStroke):
        cycle = self.cycle

        self.deactivate(self.ball.positionRow, self.ball.positionCol)
        self.ball.move(cycle)
        self.activate(self.ball.positionRow, self.ball.positionCol)

        for pos in self.humanPlayer.positions: self.deactivate(pos, 0)
        self.humanPlayer.move(cycle, keyStroke)
        for pos in self.humanPlayer.positions: self.activate(pos, 0)

        self.cycle += 1
