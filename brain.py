import random
import math

class Brain():
    def __init__(self, max_steps:int) -> None:
        self.directions_size = max_steps
        self.step = 0
        self.directions = [random.uniform(0, 2 * math.pi) for _ in range(max_steps)]

    def get_acceleration(self) -> None:
        if self.step >= self.directions_size:
            return None
        x = math.sin(self.directions[self.step])
        y = math.cos(self.directions[self.step])
        self.step += 1
        return (x, y)
    
    def mutate(self, mutation_rate: float=0.01) -> None:
        for i in range(self.directions_size):
            if random.random() < mutation_rate:
                eps = 0.1 * random.uniform(-2 * math.pi, 2 * math.pi)
                self.directions[i] = max(min(2 * math.pi, self.directions[i] + eps), 0)
                # self.directions[i] = random.uniform(0, 2*math.pi)