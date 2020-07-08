from uonrevisedtypes.scalars.uon_scalar import UonScalar

# TODO: maybe inherit from string also?
class UonString(UonScalar):
    def __init__(self, value, presentation_properties={}):
        super().__init__(value, "str", presentation_properties)

    def __repr__(self):
        return "UonString({})".format(self.value)
