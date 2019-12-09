import City

def read_file(path):
    cities = []

    with open(path, "r") as file:
        for line in file.readlines():
            tokens_from_line = line.split(' ')
            c = City(tokens_from_line[0], tokens_from_line[1], tokens_from_line[2])

            cities.append(c)

    return cities

