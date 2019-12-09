from copy import copy
from random import shuffle


class GeneticAlgorithm:
    def __init__(self, cities, options):
        self.cities = cities
        self.options = options
        self.populations = []

        self.init_populations()

    def init_populations(self):

        for i in range(self.options['PopulationSize']):
            cities = copy(self.cities)
            shuffle(cities)
            self.populations.append(cities)
