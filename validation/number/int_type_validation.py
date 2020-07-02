from validation.type_validation import ValidationType, ValidationTypeError


class IntegerTypeValidation(ValidationType):

    def validate_type(self, input_):
        if (not input_.uon_type.startsWith("int")):
            raise ValidationTypeError(input_, """The following input {} type
                                           does not correspond to integer"""
                                              .format(input_))

    def __repr__(self):
        return "IntegerTypeValidation()"
