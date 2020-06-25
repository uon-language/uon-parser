from uonTypes.uon_definition import UonBase


class UonScalar(UonBase):
    def __init__(self, value, uon_type):
        '''
        A Uon scalar takes a value and a string representation
        of its type
        '''
        self.value = value
        self.uon_type = uon_type

    # TODO: Type coercion methods here
