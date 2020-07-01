from validation.type_validator import ValidationType, ValidationTypeError


class FloatTypeValidation(ValidationType):

    def validate_type(self, input):
        if (not input.uon_type.startsWith("float")):
            raise ValidationTypeError(input, """The following input {} type
                                           does not correspond to float"""
                                             .format(input))
