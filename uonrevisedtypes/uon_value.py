from uon import Uon

import copy


class UonValue(Uon):
    """
    Represents the basic UON value type.

    We provide a getter and a setter for _presentation_properties (we
    prefix it with an underscore to denote that it's a private variable)
    by the means of the built-in @property decorator. That way 
    we can add custom behavior when getting or setting this attribute, 
    while avoiding to have to write boilerplate code like 
    get_presentation_properties() or set_presentation_properties().

    # TODO: When deserializing verify that the keys of the presentation 
    properties dict correspond to the accepted set of properties
    like description or optional.
    """
    PRESENTATION_PROPERTIES_KEYWORDS = ["description", "optional"]

    def __init__(self, value, uon_type, presentation_properties={}):
        self.value = value
        self.uon_type = uon_type
        UonValue.verify_presentation_properties(presentation_properties)
        self._presentation_properties = presentation_properties

    @property
    def presentation_properties(self):
        """ Return a shallow copy of
        the presentation properties of this uon object."""
        return copy.copy(self._presentation_properties)

    @presentation_properties.setter
    def presentation_properties(self, presentation_properties_):
        """ Set the presentation properties of this uon object. """
        UonValue.verify_presentation_properties(presentation_properties_)
        self._presentation_properties = presentation_properties_

    @staticmethod
    def verify_presentation_properties(presentation_properties):
        for k in presentation_properties.keys():
            if k not in UonValue.PRESENTATION_PROPERTIES_KEYWORDS:
                raise ValueError("{} is not a presentation_property".format(k))
