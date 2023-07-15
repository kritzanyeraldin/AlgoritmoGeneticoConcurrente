class Individuo:
    def __init__(self, x , y):
        self.x = x
        self.y = y
        self.fitness = 0

    def print(self):
        print(self.x)
        print(self.y)