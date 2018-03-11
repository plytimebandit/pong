class Ball:

    def __init__(self, boundary):
        self.boundary = boundary
        self.positionRow = 3
        self.positionCol = 4
        self.moveUp = True
        self.moveRight = True
        self.cycleSpeed = 10

    def move(self, cycle):
        if cycle % self.cycleSpeed != 0:
            return

        if self.positionRow == 0:
            self.positionRow = 1
            self.moveUp = False
        elif self.positionRow == self.boundary:
            self.positionRow = self.boundary - 1
            self.moveUp = True
        elif self.moveUp:
            self.positionRow -= 1
        elif not self.moveUp:
            self.positionRow += 1

        if self.positionCol == 0:
            self.positionCol = 1
            self.moveRight = True
        elif self.positionCol == self.boundary:
            self.positionCol = self.boundary - 1
            self.moveRight = False
        elif self.moveRight:
            self.positionCol += 1
        elif not self.moveRight:
            self.positionCol -= 1
