import re


class RegexValidation():
    def __init__(self, regex):
        self.regex = regex
    
    def validate_property(self, input_):
        self.regex.validate(input_)

    def __repr__(self):
        return "RegexValidation({!r})".format(self.regex)

print(re.compile(r"(.)*").match("123"))
