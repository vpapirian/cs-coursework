class Bug:
    def __init__(self, initialPosition):
        self.position = initialPosition
        self.direction = 1  # 1 = right, -1 = left

    def turn(self):
        self.direction *= -1  # switch direction

    def move(self):
        self.position += self.direction  # move 1 step

    def getPosition(self):
        return self.position