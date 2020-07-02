from validation.type_validation import ValidationType, ValidationTypeError


class StringTypeValidation(ValidationType):

    def validate_type(self, input):
        if (input.uon_type != "str"):
            raise ValidationTypeError(input, """The following input {} type
                                           does not correspond to string"""
                                             .format(input))
