# This module contains tools for debugging


# Getting object attributes and classes in format more readable than the dir() function
def getattributes(clazz):
    attrs = {}
    for name in vars(clazz):
        if name.startswith("__"):
            continue
        attr = getattr(clazz, name)
        if callable(attr):
            continue
        print(f"name is {name}, and attrs are:", attr, sep="\n")

        attrs[name] = attr
    return attrs
