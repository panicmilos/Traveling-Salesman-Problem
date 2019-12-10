from iomanager import read_file
from GeneticAlgorithm import GeneticAlgorithm
from Options import Options
import GUI


def main():
    cities = read_file("data_tsp.txt")
    o = Options()
    o['PopulationSize'] = 10
    o['NumOfGenerations'] = 10000
    o['FunctionTolerance'] = 10 ** -6
    o['Limit'] = float('Inf')
    o['MutationRate'] = 0.5
    ga = GeneticAlgorithm(cities, o)
    GUI.init(ga)


if __name__ == "__main__":
    # test_options()
    main()
