from validation.types.type_validation import (
    ValidationType, ValidationTypeError
)


class StringTypeValidation(ValidationType):

    def validate_type(self, input_):
        if (not isinstance(input_, str)):
            raise ValidationTypeError(input_, "The following input {} type "
                                              "does not correspond to string"
                                              .format(input_))

    def __repr__(self):
        return "StringTypeValidation()"
