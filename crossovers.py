from random import random
from Path import Path


def crossover(path1, path2):
    first_index = int(random() * len(path1))
    last_index = int(random() * len(path2))

    while last_index == first_index:
        last_index = int(random() * len(path2))

    if last_index < first_index:
        first_index, last_index = last_index, first_index

    # pravljenje prvog deteta
    new_path1 = path1[first_index:last_index]
    temp = [p for p in path2 if p not in new_path1]
    new_path1 += temp

    # pravljenje drugog deteta
    temp = path2[first_index:last_index]
    new_path2 = [p for p in path1 if p not in temp]
    new_path2 += temp

    return Path(new_path1), Path(new_path2)
