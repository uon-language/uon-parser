from validation.types.type_validation import (
    ValidationType, ValidationTypeError
)
from uonrevisedtypes.scalars.uon_bool import UonBoolean


class BooleanTypeValidation(ValidationType):

    def validate_type(self, input_):
        if (not isinstance(input_, UonBoolean)):
            raise ValidationTypeError(input_, "The following input {} type "
                                              "does not correspond to boolean"
                                              .format(input_))

    def __repr__(self):
        return "BooleanTypeValidation()"