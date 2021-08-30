import random
import math

class Brain():
    def __init__(self, max_steps):
        self.directions_size = max_steps
        self.step = 0
        self.directions = [random.uniform(0, 2 * math.pi) for _ in range(max_steps)]

    def get_acceleration(self):
        if self.step >= self.directions_size:
            return None
        x = math.sin(self.directions[self.step])
        y = math.cos(self.directions[self.step])
        self.step += 1
        return (x, y)
    
    def mutate(self, mutation_rate=0.01):
        for i in range(self.directions_size):
            if random.random() < mutation_rate:
                self.directions[i] = random.uniform(0, 2 * math.pi)
                # TODO maybe just tweak instead of redoing
