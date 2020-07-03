from validation.type_validation import ValidationType, ValidationTypeError


class FloatTypeValidation(ValidationType):

    def validate_type(self, input_):
        if (not input_.uon_type.startswith("float")):
            raise ValidationTypeError(input_, """The following input {} type
                                           does not correspond to float"""
                                              .format(input_))

    def __repr__(self):
        return "FloatTypeValidation()"
