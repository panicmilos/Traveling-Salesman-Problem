from City import City


def read_file(path):
    cities = []

    with open(path, "r") as file:
        for line in file.readlines():
            tokens_from_line = line.strip().split(' ')
            c = City(tokens_from_line[0], float(tokens_from_line[1]), float(tokens_from_line[2]))

            cities.append(c)

    return cities
