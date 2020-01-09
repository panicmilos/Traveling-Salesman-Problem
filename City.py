import math


class City:
    def __init__(self, city_id, x, y):
        self.city_id = city_id
        self.x = x
        self.y = y

    def distance(self, city):
        return math.sqrt((self.x - city.x)**2 + (self.y - city.y)**2)

    def __str__(self):
        return self.city_id + " (" + str(self.x) + ", " + str(self.y) + ")"
