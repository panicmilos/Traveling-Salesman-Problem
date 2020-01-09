from iomanager import read_file
from GeneticAlgorithm import GeneticAlgorithm
from Options import Options
import GUI


def main():
    cities = read_file("data_tsp.txt")

    o = Options()

    ga = GeneticAlgorithm(cities, o)

    GUI.init(ga)


if __name__ == "__main__":
    main()
