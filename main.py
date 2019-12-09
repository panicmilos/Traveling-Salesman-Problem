from iomanager import read_file
from GeneticAlgorithm import GeneticAlgorithm
from Options import Options
from time import time

def main():
    cities = read_file("data_tsp.txt")

    # for c in cities:
    #    c.print_city()
    o = Options()
    o['PopulationSize'] = 1000

    t = time()
    ga = GeneticAlgorithm(cities, o)
    print(time() - t)
    print("TU SAM")


def test_options():
    o = Options()
    print(o['NumOfGeneration'], "== 100")
    print(o['PopulationSize'], "== 50")
    print(o['FunctionTolerance'], "== 10**-8")

    o['NumOfGeneration'] = 200
    print(o['NumOfGeneration'], "== 200")
    o['PopulationSize'] = 100
    print(o['PopulationSize'], "== 100")
    o['FunctionTolerance'] = 10**-15
    print(o['FunctionTolerance'], "== 10**-15")


if __name__ == "__main__":
    # test_options()
    main()
