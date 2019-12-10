from copy import copy
from random import shuffle, random
from Path import Path
from crossovers import crossover1
from mutations import mutation1


class GeneticAlgorithm:
    def __init__(self, cities, options):
        self.cities = cities
        self.options = options
        self.populations = []
        self.fitness_hash = {}

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

    def ga_loop(self):
        self.init_population()

        for i in range(self.options['NumOfGeneration']):
            self.selection()

            self.populations.sort(key=lambda x: self.fitness_hash[x])
            self.populations = self.populations[0:self.options['PopulationSize']]

        for path in self.populations:
            print(path.total_distance())

        return

    def selection(self):
        childrens = []

        self.calculate_fitness()
        for i in range(len(self.populations)//2):
            parent1, parent2 = self.select_parents()
            child1, child2 = crossover1(parent1, parent2)

            mutation1(child1, 0.01)
            childrens.append(child1)

            mutation1(child2, 0.01)
            childrens.append(child2)

        self.populations += childrens
        # mozda editovati funkciju da kalkulise samo drugi deo a ne ponovo za roditelje
        self.calculate_fitness()

    def select_parents(self):
        roulette_table = []

        for path in self.populations:
            fitness_with_random = self.fitness_hash[path] * random()
            roulette_table.append(fitness_with_random)

        min1 = [0, roulette_table[0]] if roulette_table[0] < roulette_table[1] else [1, roulette_table[1]]
        min2 = [0, roulette_table[0]] if roulette_table[0] > roulette_table[1] else [1, roulette_table[1]]

        for i in range(2, len(self.populations)):
            fitness = roulette_table[i]

            if fitness < min1[1]:
                min2 = min1
                min1 = [i, fitness]
                continue

            if fitness < min2[1]:
                min2 = [i, fitness]

        return self.populations[min1[0]], self.populations[min1[0]]
