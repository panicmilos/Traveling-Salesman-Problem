from iomanager import read_file
from GeneticAlgorithm import GeneticAlgorithm
from Options import Options
import GUI


def main():
    cities = read_file("data_tsp.txt")
    o = Options()
    o['PopulationSize'] = 100
    o['NumOfGenerations'] = 100
    o['FunctionTolerance'] = 10 ** -15
    o['Limit'] = 100
    o['MutationRate'] = 0.01
    ga = GeneticAlgorithm(cities, o)
    ga.calculate_fitness()
    GUI.init(ga)


if __name__ == "__main__":
    # test_options()
    main()
