from validation.type_validation import ValidationType, ValidationTypeError


class IntegerTypeValidation(ValidationType):

    # TODO: use is instanceOf
    def validate_type(self, input_):
        if (not input_.uon_type.startswith("int")):
            raise ValidationTypeError(input_, """The following input {} type
                                           does not correspond to integer"""
                                              .format(input_))

    def __repr__(self):
        return "IntegerTypeValidation()"
