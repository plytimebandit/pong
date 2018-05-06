class Led:

    def __init__(self):
        self.isActive = False
        self.isFlashed = False

    def activate(self):
        self.isActive = True

    def deactivate(self):
        self.isActive = False
        self.isFlashed = False

    def flash(self):
        self.activate()
        self.isFlashed = True
