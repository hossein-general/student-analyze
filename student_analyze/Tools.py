# This module contains tools for debugging

# As a cleaner printing option
from pprint import pprint


# Getting object attributes and classes in format more readable than the dir() function
# This functinon will not work if the class has __sltos__ defined, as it prevents __dict__ creation
# TODO adding some validation for existance of __dict__
def gtattr(clazz):
    attrs = {}
    for name in vars(clazz):
        # Checking if the attribute is not dunder, private or protected
        if name.startswith("__"):
            continue

        # Getting the value of that attribute
        attr = getattr(clazz, name)

        # we dont want to print callable attributes like methods
        if callable(attr):
            continue

        # using the __str__ writing format for each item to return
        # (if it was not an iterable or it was a string)
        if hasattr(attr, "__iter__") and not isinstance(attr, str):
            attr = dict(zip(list(item.__str__() for item in attr), attr))
        elif not isinstance(attr, (str, int, bool, float)):
            attr = {attr.__str__(): attr}
        # (if it was an iterable and not a string)

        # Adding the attribute with its name and value inside the dictionary
        attrs[name] = attr
    pprint(attrs)
