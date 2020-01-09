from random import random


def mutation(path, probability):
    if random() <= probability:
        city1 = int(random() * len(path))
        city2 = int(random() * len(path))

        while city2 == city1:
            city2 = int(random() * len(path))

        path[city1], path[city2] = path[city2], path[city1]
