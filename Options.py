class Options:

    def __init__(self):
        self.options = {
            "NumOfGenerations": 1000,
            "PopulationSize": 100,
            "FunctionTolerance": 10**-6,
            "Limit": 200,
            "MutationRate": 0.01,
            "ElitismRate": 20
        }

    def set_value(self, key, value):
        if key not in self.options:
            print(key, "is not a valid option.")
            return

        self.options[key] = value
        print(key, "is successfully set to", value, ".")

    def __setitem__(self, key, value):
        self.set_value(key, value)

    def get_item(self, key):
        if key not in self.options:
            print(key + " is not a valid option.")
            return

        return self.options[key]

    def __getitem__(self, key):
        return self.get_item(key)
