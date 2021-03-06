import random


class Ball:

    def __init__(self, boundary):
        self.boundary = boundary  # field size - 1
        self.positionRow = 3
        self.positionCol = 4
        self.moveUp = True
        self.moveRight = True
        # If Pong sleeps 0.01 s then cycle speed of 100 means "move once in a second" (Smaller = faster)
        self.cycleSpeed = 7
        self.randomAngle = 0

    def move(self, cycle):
        if cycle % self.cycleSpeed != 0:
            return

        # horizontal movement
        if self.positionCol == 0:
            self.positionCol = 1
            self.moveRight = True
            self.moveUp = self.get_movement_direction()
        elif self.positionCol == self.boundary:
            self.positionCol = self.boundary - 1
            self.moveRight = False
            self.moveUp = self.get_movement_direction()
        elif self.moveRight:
            self.positionCol += 1
        elif not self.moveRight:
            self.positionCol -= 1

        # vertical movement
        if self.positionRow == 0:
            self.set_random_angle()
            self.positionRow = 1 + self.randomAngle
            self.moveUp = False
        elif self.positionRow == self.boundary:
            self.set_random_angle()
            self.positionRow = self.boundary - 1 - self.randomAngle
            self.moveUp = True
        elif self.moveUp:
            self.positionRow -= (1 + self.get_random_angle())
        elif not self.moveUp:
            self.positionRow += (1 + self.get_random_angle())

    def get_random_angle(self):
        if 1 < self.positionRow < self.boundary-1:
            return self.randomAngle
        return 0

    def set_random_angle(self):
        self.randomAngle = random.randint(0, 1)

    @staticmethod
    def get_movement_direction():
        return True if random.randint(0, 1) == 1 else False
