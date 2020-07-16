from validation.types.type_validation import (
    ValidationType, ValidationTypeError
)
from uonrevisedtypes.scalars.uon_uint import UonUint


class UintTypeValidation(ValidationType):

    def validate_type(self, input_):
        if (not isinstance(input_, UonUint)):
            raise ValidationTypeError(input_, "The following input {} type "
                                              "does not correspond to "
                                              "unsigned int".format(input_))

    def __repr__(self):
        return "UintTypeValidation()"
