from random import random


# drugi roditelj i staljva na kraj
def crossover1(path1, path2):
    first_index = int(random() * len(path1))
    last_index = int(random() * len(path2))
    if last_index < first_index:
        first_index, last_index = last_index, first_index

    new_path1 = path1[first_index:last_index]
    for p in path2:
        if p not in new_path1:
            new_path1.append(p)

    temp = path2[first_index:last_index]
    new_path2 = []
    for p in path1:
        if p not in temp:
            new_path2.append(p)
    new_path2 += temp

    print(path1[first_index:last_index])
    return new_path1, new_path2


# drugi roditelj i staljva na pocetak
def crossover2(path1, path2):
    first_index = int(random() * len(path1))
    last_index = int(random() * len(path2))
    if last_index < first_index:
        first_index, last_index = last_index, first_index

    new_path1 = path1[first_index:last_index]
    for p in path2:
        if p not in new_path1:
            new_path1.append(p)

    new_path2 = path2[first_index:last_index]
    for p in path1:
        if p not in new_path2:
            new_path2.append(p)

    print(path1[first_index:last_index])
    return new_path1, new_path2
