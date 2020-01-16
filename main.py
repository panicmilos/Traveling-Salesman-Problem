from iomanager import read_file
from GeneticAlgorithm import GeneticAlgorithm
from Options import Options


def main():
    cities = read_file("new.txt")
    o = Options()
    o['PopulationSize'] = 500
    o['NumOfGenerations'] = 5000
    o['Tolerance'] = 10 ** -6
    o['Limit'] = float('inf')
    o['MutationRateStart'] = 1
    o['MutationRateFinish'] = 5
    o['ElitismRate'] = 10
    o['Draw'] = True
    ga = GeneticAlgorithm(cities, o)
    ga.run()


if __name__ == "__main__":
    main()
