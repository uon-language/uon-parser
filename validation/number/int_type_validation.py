from validation.type_validation import ValidationType, ValidationTypeError


class IntegerTypeValidation(ValidationType):

    def validate_type(self, input):
        if (not input.uon_type.startsWith("int")):
            raise ValidationTypeError(input, """The following input {} type
                                           does not correspond to integer"""
                                             .format(input))

    def __repr__(self):
        return "IntegerTypeValidation()"
