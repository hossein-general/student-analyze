# This is the module which is resposible for all calculations and logics


# This object containes information about the data that is stored within it
class DataObject:
    def __init__(self, data_name, order=None) -> None:
        self.data_name = data_name
        self.list = {}
        self.order = order

    def retrieve(self):
        return self.list


class RuntimeDataAccessor:
    def __init__(self) -> None:
        self.es = DataObject('Education State')
        self.egd = DataObject('Education Grade')
        self.egp = DataObject('Education Group')
        self.gender = DataObject('Gender')
        self.person = DataObject('Person')
