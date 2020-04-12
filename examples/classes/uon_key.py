class UonKey :
    def __init__(self, key, properties):
        self.key = key
        # or operator to return default value in case property is none or any falsy value
        print("UonKey COnstructor: ", key, properties, end='\n')
        self.description =  properties.get('description', '')
        self.required = properties.get('required', False)

    
    def __repr__(self):
        return "{} (description={}, required={})".format(
            self.key, self.description, self.required)

class UonKeyProperties:
    def __init__(self, description, required=False):
        self.description = description
        self.required = required
    
    def __repr__(self):
        return "description: {}, required: {}".format(
            self.description, self.required)


