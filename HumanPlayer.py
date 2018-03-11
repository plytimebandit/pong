class HumanPlayer:

    def __init__(self, startPosition, boundary):
        self.size = 3
        self.cycleSpeed = 20
        pos = int(startPosition - self.size / 2)
        self.positions = range(pos, pos + self.size)

        self.startPosition = startPosition
        self.boundary = boundary

    def move(self, cycle, key_stroke):
        if cycle % self.cycleSpeed != 0:
            return

        if key_stroke == ord('w'):
            pass
        elif key_stroke == ord('s'):
            pass
