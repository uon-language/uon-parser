from uonTypes.uon_definition import UonBase


class UonPair(UonBase):
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def getKeyname(self):
        return self.key.keyname        
    
    def __str__(self):
        return str(self.key) + " : " + str(self.value)

    def __repr__(self):
        return self.__str__()
