class UonKey :
    def __init__(self, key, properties):
        self.key = key
        self.properties = properties
    
    def __repr__(self):
        return "{} ({})".format(
            self.key, self.properties)

class UonKeyProperties:
    def __init__(self, description, required=False):
        self.description = description
        self.required = required
    
    def __repr__(self):
        return "description: {}, required: {}".format(
            self.description, self.required)


