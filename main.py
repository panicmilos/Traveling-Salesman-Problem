from iomanager import read_file
from GeneticAlgorithm import GeneticAlgorithm
from Options import Options


def main():
    cities = read_file("data_tsp.txt")

    o = Options()
    o['PopulationSize'] = 100
    ga = GeneticAlgorithm(cities, o)
    ga.ga_loop()


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
