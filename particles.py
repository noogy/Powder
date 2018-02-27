class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xSpeed = 0
        self.ySpeed = 0

    def move(self, x, y):
        self.x += x
        self.y += y

    def accel(self, x, y):
        self.xSpeed += x
        self.ySpeed += y