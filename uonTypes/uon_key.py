class UonKey :
    def __init__(self, keyname, properties):
        self.keyname = keyname
        # or operator to return default value in case property is none or any falsy value
        print("UonKey Constructor: ", keyname, properties)
        self.properties = properties
    
    def __repr__(self):
        return "{}: {{properties: {}}}".format(
            self.keyname, self.properties)

class UonKeyProperties:
    def __init__(self, description, required=False):
        self.description = description
        self.required = required
    
    def __repr__(self):
        return "description: {}, required: {}".format(
            self.description, self.required)


