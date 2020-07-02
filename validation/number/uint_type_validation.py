from validation.type_validation import ValidationType, ValidationTypeError


class UintTypeValidation(ValidationType):

    def validate_type(self, input):
        if (not input.uon_type.startsWith("uint")):
            raise ValidationTypeError(input, """The following input {} type
                                           does not correspond to unsigned
                                           int""".format(input))

    def __repr__(self):
        return "UintTypeValidation()"
