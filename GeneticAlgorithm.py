from copy import copy
from random import shuffle, random
from Path import Path
from crossovers import crossover
from mutations import mutation
import GUI
from time import time


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
        self._init_population()
        self.status_index = 1

    def _init_population(self):
        self.population.clear()
        for i in range(self.options['PopulationSize']):
            cities = copy(self.cities)
            shuffle(cities)
            self.population.append(Path(cities))

        self.best_path = self.population[0]

    def _calculate_fitness(self, population, clear=1):
        if clear:
            self.fitness_hash.clear()

        for path in population:
            fitness = path.total_distance
            self.fitness_hash[path] = fitness

    def next_iter(self):
        if self.current_iter >= self.options['NumOfGenerations'] * self.status_index / 10:
            print(">> " + str(self.status_index * 10) + "%")
            self.status_index += 1
        if self.current_iter < self.options['NumOfGenerations'] and self.limit < self.options['Limit']:
            children = self._selection()

            self.population.sort(key=lambda x: self.fitness_hash[x])
            children.sort(key=lambda x: self.fitness_hash[x])

            num_of_parents = int(self.options['ElitismRate'] * self.options['PopulationSize'] / 100)
            self.population = [self.population[i] for i in range(num_of_parents)]
            self.population += [children[i] for i in range(self.options['PopulationSize'] - num_of_parents)]

            self.current_iter += 1
            # ako nema napretka options['Limit'] puta, prekini petlju
            if abs(self.current_best - self.population[0].total_distance) < self.options['Tolerance']:
                self.limit += 1
            else:
                self.limit = 0
            self.current_best = self.population[0].total_distance
            self.best_path = self.population[0]

            return True
        else:
            if self.limit >= self.options['Limit']:
                print("Limit dostignut. Algoritam prekinut\n")
        return False

    def _selection(self):
        children = []

        self._calculate_fitness(self.population)
        # promenljiva mutacija
        mr = (self.options["MutationRateStart"] + self.current_iter / self.options["NumOfGenerations"] * (
                self.options["MutationRateFinish"] - self.options["MutationRateStart"])) / 100

        for i in range(len(self.population) // 2):
            parent1, parent2 = self._select_parents()
            child1, child2 = crossover(parent1, parent2)

            mutation(child1, mr)
            children.append(child1)

            mutation(child2, mr)
            children.append(child2)

        self._calculate_fitness(children, 0)

        return children

    def _select_parents(self):
        sortirane_putanje = sorted(self.fitness_hash.items(), key=lambda kv: kv[1], reverse=True)

        sp = 1.8  # skaliranje indeksa 1<=sp<=2

        n = self.options["PopulationSize"]

        roulette_table = [(2 - sp + (2 * (sp - 1) * i / (n - 1))) * random() for i in range(n)]

        max1 = [0, roulette_table[0]] if roulette_table[0] < roulette_table[1] else [1, roulette_table[1]]
        max2 = [0, roulette_table[0]] if roulette_table[0] > roulette_table[1] else [1, roulette_table[1]]

        for i in range(2, len(self.population)):
            fitness = roulette_table[i]

            if fitness > max1[1]:
                max2 = max1
                max1 = [i, fitness]
                continue

            if fitness > max2[1]:
                max2 = [i, fitness]

        return sortirane_putanje[max1[0]][0], sortirane_putanje[max2[0]][0]

    def run(self):
        print("Running...")
        t = time()
        if self.options['Draw']:
            GUI.init(self)
        else:
            while self.next_iter():
                pass
            print("Predjeni put >> ", self.current_best)
            print("Redosled gradova >> ", self.best_path)
            print("Ukupno vreme", time() - t)
