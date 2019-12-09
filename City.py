class City:
    def __init__(self, city_id, x, y):
        self._id = city_id
        self._x = x
        self._y = y

    def print_city(self):
        print(self._id + " " + self._x + " " + self._y)
