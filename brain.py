import random
import math

class Brain():
    def __init__(self, direction_size=400):
        self.directions_size = direction_size
        self.step = 0
        self.directions = [random.uniform(0, 2 * math.pi) for _ in range(direction_size)]

    def get_acceleration(self):
        if self.step >= self.directions_size:
            return None
        x = math.sin(self.directions[self.step])
        y = math.cos(self.directions[self.step])
        self.step += 1
        return (x, y)