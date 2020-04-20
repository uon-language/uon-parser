class UonValue:
    def __init__(self, uonType, unit, value):
        self.uonType = uonType
        self.unit = unit
        self.value = value
    
    def __repr__(self):
        return "{{type: {}, unit: {}, content:{}}}".format(
            self.uonType, self.unit, self.value
        )
