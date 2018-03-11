class Led:

    def __init__(self):
        self.isActive = False

    def activate(self):
        self.isActive = True

    def deactivate(self):
        self.isActive = False