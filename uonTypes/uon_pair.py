class UonPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def getKeyname(self):
        return self.key.keyname

    def __repr__(self):
        return str(self.key) + " : " + str(self.value)
