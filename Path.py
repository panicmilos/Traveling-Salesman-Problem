class Path:
    def __init__(self, cities):
        self.cities = cities

    def total_distance(self):
        total = 0
        for i in range(len(self.cities) - 1):
            total += self.cities[i].distance(self.cities[i+1])
        return total
