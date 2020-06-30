class Schema:
    def __init__(self, properties):
        """
        A Schema defines a type with a list of 
        attributes and properties they have to verify.
        The properties will be stored in dictionary with the corresponding
        attributes serving as keys.
        """
        self.properties = properties
