from Led import Led


class MatrixField:

    def __init__(self, size):
        self.size = size
        self.ledList = []

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
            raise ValueError("'row' and 'col' must not exceed 'size'.")

        return self.ledList[self.size * row + col]
