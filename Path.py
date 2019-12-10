class Path:
    def __init__(self, cities):
        self.cities = cities

    def total_distance(self):
        total = 0
        for i in range(-1, len(self.cities) - 1):
            total += self.cities[i].distance(self.cities[i+1])
        return total

    def __len__(self):
        return len(self.cities)

    def __getitem__(self, index):
        # dodati proveru za opseg
        return self.cities[index]

    def __setitem__(self, index, city):
        # dodati proveru za opseg
        self.cities[index] = city

