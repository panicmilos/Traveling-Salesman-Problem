class Options:

    def __init__(self):
        self.options = {
            "NumOfGenerations": 1000,
            "PopulationSize": 100,
            "FunctionTolerance": 10**-6,
            "Limit": 200,
            "MutationRateStart": 1,
            "MutationRateFinish": 5,
            "ElitismRate": 20,
            "Draw": False,
        }

    def set_value(self, key, value):
        if key not in self.options:
            print(key, "nije validna opcija.")
            return

        self.options[key] = value
        print(key, "je postavljen na", value, ".")

    def __setitem__(self, key, value):
        self.set_value(key, value)

    def get_item(self, key):
        if key not in self.options:
            print(key, "nije validna opcija.")
            return

        return self.options[key]

    def __getitem__(self, key):
        return self.get_item(key)
