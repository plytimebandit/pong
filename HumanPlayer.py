class HumanPlayer:

    def __init__(self, startPosition, boundary):
        self.size = 3
        self.cycleSpeed = 10
        self.cycleInterval = 0
        pos = int(startPosition - self.size / 2)
        self.set_positions(pos)

        self.startPosition = startPosition
        self.boundary = boundary

    def move(self, key_stroke):
        self.cycleInterval += 1
        if self.cycleInterval <= self.cycleSpeed:
            return

        if key_stroke == ord('w'):
            self.move_up()
            self.cycleInterval = 0
        elif key_stroke == ord('s'):
            self.move_down()
            self.cycleInterval = 0

    def set_positions(self, pos):
        self.positions = range(pos, pos + self.size)

    def move_up(self):
        if self.positions[0] == 0:
            return
        self.positions = list(map(lambda e: e-1, self.positions))

    def move_down(self):
        if self.positions[-1] == self.boundary:
            return
        self.positions = list(map(lambda e: e+1, self.positions))
