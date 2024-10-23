# This is the module which is resposible for all calculations and logics


# This object containes information about the data that is stored within it
class DataObject:
    def __init__(self, order=None) -> None:
        self.list = {}
        self.order = order

    def retrieve(self):
        return self.list


class RuntimeDataAccessor:
    def __init__(self) -> None:
        self.es = DataObject()
        self.eg = DataObject()
        self.gender = DataObject()
        self.person = DataObject()
