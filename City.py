import math


class City:
    def __init__(self, city_id, x, y):
        self.city_id = city_id
        self.x = x
        self.y = y

    def print_city(self):
        print(self.id + " " + self.x + " " + self.y)

    def distance(self, city):
        return math.sqrt((self.x - city.x)**2 + (self.y - city.y)**2)