from validation.type_validator import ValidationType, ValidationTypeError


class IntegerTypeValidation(ValidationType):

    def validate_type(self, input):
        if (not input.uon_type.startsWith("int")):
            raise ValidationTypeError(input, """The following input {} type
                                           does not correspond to integer"""
                                             .format(input))
