class UonDictionary:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def get(self, key):
        return self.dictionary[key]