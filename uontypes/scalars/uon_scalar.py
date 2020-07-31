from uontypes.uon_value import UonValue


class UonScalar(UonValue):
    def __init__(self, value, uon_type, presentation_properties={}):
        '''
        A Uon scalar takes a value and a string representation
        of its type
        '''
        super().__init__(value, uon_type, presentation_properties)

    # TODO: Type coercion methods here
