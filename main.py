from iomanager import read_file
from GeneticAlgorithm import GeneticAlgorithm
from Options import Options


def main():

    cities = read_file("data_tsp.txt")

    o = Options()
    o['PopulationSize'] = 100
    o['NumOfGenerations'] = 5000
    o['FunctionTolerance'] = 10 ** -6
    o['Limit'] = float('inf')
    o['MutationRateStart'] = 1
    o['MutationRateFinish'] = 5
    o['ElitismRate'] = 20
    o['Draw'] = True
    ga = GeneticAlgorithm(cities, o)
    ga.run()


if __name__ == "__main__":
    main()
