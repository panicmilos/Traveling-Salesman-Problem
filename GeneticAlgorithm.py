from copy import copy
from random import shuffle, random
from Path import Path


class GeneticAlgorithm:
    def __init__(self, cities, options):
        self.cities = cities
        self.options = options
        self.populations = []
        self.fitness_hash = {}

        self.init_population()

    def init_population(self):

        for i in range(self.options['PopulationSize']):
            cities = copy(self.cities)
            shuffle(cities)
            self.populations.append(Path(cities))

    def calculate_fitness(self):
        self.fitness_hash.clear()

        for path in self.populations:
            fitness = path.total_distance()
            self.fitness_hash[path] = fitness

    def select_parents(self):
        roulette_table = []

        for path in self.populations:
            fitness_with_random = self.fitness_hash[path] * random()
            roulette_table.append(fitness_with_random)

        min1 = [0, roulette_table[0]] if roulette_table[0] < roulette_table[1] else [1, roulette_table[1]]
        min2 = [0, roulette_table[0]] if roulette_table[0] > roulette_table[1] else [1, roulette_table[1]]

        for i in range(2, len(self.populations)):
            fitness = roulette_table[i]

            if fitness < min1:
                min2 = min1
                min1 = [i, fitness]
                continue

            if fitness < min2:
                min2 = [i, fitness]

        return min1, min2
