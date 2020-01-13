from iomanager import read_file
from GeneticAlgorithm import GeneticAlgorithm
from Options import Options


def main():
    cities = read_file("data_tsp.txt")

    o = Options()
    o['NumOfGenerations'] = 5000
    o['Limit'] = float('inf')
    o['Draw'] = False

    ga = GeneticAlgorithm(cities, o)
    ga.run()


if __name__ == "__main__":
    main()
