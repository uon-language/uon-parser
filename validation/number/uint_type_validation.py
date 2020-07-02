from validation.type_validation import ValidationType, ValidationTypeError


class UintTypeValidation(ValidationType):

    def validate_type(self, input_):
        if (not input_.uon_type.startswith("uint")):
            raise ValidationTypeError(input_, """The following input {} type
                                           does not correspond to unsigned
                                           int""".format(input_))

    def __repr__(self):
        return "UintTypeValidation()"
