class Schema:
    '''
    TODO: Need to add UUID
    '''
    def __init__(self, type_, validators):
        """
        A Schema defines a type with a list of
        attributes and properties they have to verify.
        The properties will be stored in dictionary with the corresponding
        attributes serving as keys.

        example: TODO
        """
        self.type_ = type_
        self.validators = validators

    def validateSchema(self, input_):
        """
        Takes a UonCustomType and validates it.
        """
        for k, v in input_.attributes.items():
            self.validators[k].validate(v)
    
    def __repr__(self):
        return "Schema({}, {})".format(
            self.type_, self.validators
        )
