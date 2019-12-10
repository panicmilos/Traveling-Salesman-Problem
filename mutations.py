from random import random


def mutation1(path, probability):
    if random() <= probability:
        city1 = int(random() * len(path))
        city2 = int(random() * len(path))
        path[city1], path[city2] = path[city2], path[city1]