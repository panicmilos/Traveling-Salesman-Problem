from copy import copy
from random import shuffle, random
from Path import Path
from crossovers import crossover
from mutations import mutation

class GeneticAlgorithm:
    def __init__(self, cities, options):
        self.cities = cities
        self.options = options
        self.population = []
        self.fitness_hash = {}
        self.current_iter = 0
        self.limit = 0
        self.current_best = float('Inf')
        self.best_path = None
        self.init_population()

    def init_population(self):
        for i in range(self.options['PopulationSize']):
            cities = copy(self.cities)
            shuffle(cities)
            self.population.append(Path(cities))

        self.best_path = self.population[0]

    def calculate_fitness(self, population, clear=1):
        if clear:
            self.fitness_hash.clear()

        for path in population:
            fitness = path.total_distance
            self.fitness_hash[path] = fitness

    def next_iter(self):
        if self.current_iter < self.options['NumOfGenerations'] and self.limit < self.options['Limit']:
            childrens = self.selection()

            self.population.sort(key=lambda x: self.fitness_hash[x])
            childrens.sort(key=lambda x: self.fitness_hash[x])

            num_of_parents = int(self.options['ElitismRate'] * self.options['PopulationSize'] / 100)
            self.population = [self.population[i] for i in range(num_of_parents)]
            self.population += [childrens[i] for i in range(self.options['PopulationSize'] - num_of_parents)]

            self.current_iter += 1
            # ako nema napretka options['Limit'] puta, prekini petlju
            if abs(self.current_best - self.population[0].total_distance) < self.options['FunctionTolerance']:
                self.limit += 1
            else:
                self.limit = 0
            self.current_best = self.population[0].total_distance
            self.best_path = self.population[0]

            return True

        return False

    def selection(self):
        childrens = []

        self.calculate_fitness(self.population)
        for i in range(len(self.population) // 2):
            parent1, parent2 = self.select_parents()
            child1, child2 = crossover(parent1, parent2)

            mutation(child1, self.options['MutationRate'])
            childrens.append(child1)

            mutation(child2, self.options['MutationRate'])
            childrens.append(child2)

        self.calculate_fitness(childrens, 0)

        return childrens

    def select_parents(self):
        roulette_table = [self.fitness_hash[path] * random() for path in self.population]

        min1 = [0, roulette_table[0]] if roulette_table[0] < roulette_table[1] else [1, roulette_table[1]]
        min2 = [0, roulette_table[0]] if roulette_table[0] > roulette_table[1] else [1, roulette_table[1]]

        for i in range(2, len(self.population)):
            fitness = roulette_table[i]

            if fitness < min1[1]:
                min2 = min1
                min1 = [i, fitness]
                continue

            if fitness < min2[1]:
                min2 = [i, fitness]

        return self.population[min1[0]], self.population[min2[0]]
