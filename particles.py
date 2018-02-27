class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xSpeed = 0
        self.ySpeed = 0

    def move(self, x, y):
        self.x += x
        self.y += y

<<<<<<< Updated upstream
    def xSpeed(self, x):
        self.x += x
=======
    def xAccel(self, x):
        self.xSpeed += x

>>>>>>> Stashed changes
