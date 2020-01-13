class Path:
    def __init__(self, cities):
        self.cities = cities
        self.total_distance = self._calc_total_distance()

    def _calc_total_distance(self):
        total = 0
        for i in range(-1, len(self.cities) - 1):
            total += self.cities[i].distance(self.cities[i+1])
        return total

    def __len__(self):
        return len(self.cities)

    def __getitem__(self, index):
        return self.cities[index]

    def __setitem__(self, index, city):
        self.cities[index] = city
        self.total_distance = self._calc_total_distance()

    def __str__(self):
        s = ""
        for city in self.cities[0:-1]:
            s = s + str(city.city_id) + " -> "
        s += str(self.cities[-1].city_id)
        return s
