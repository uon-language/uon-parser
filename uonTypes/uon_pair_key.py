class UonPairKey:
    """
    A class for representing the key in a UON pair key-value
    which also hold its properties
    """
    def __init__(self, keyname, properties):
        self.keyname = keyname
        self.properties = properties

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        if (self.properties is None):
            return self.keyname
        else:
            return "{} ({})".format(self.keyname, self.properties)


class UonPairKeyProperties:
    """ A class for representing the properties of a UON pair key-value """
    def __init__(self, description, optional=False):
        self.description = description
        self.optional = optional

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        properties_list = []
        description_repr = None
        optional_repr = None
        if self.description is not None:
            description_repr = "description= {}".format(self.description)
            properties_list.append(description_repr)
        if self.optional is not None:
            optional_repr = "optional= {}".format(self.optional)
            properties_list.append(optional_repr)
        return ", ".join(properties_list)
