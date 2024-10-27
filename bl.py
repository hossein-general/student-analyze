# This is the module which is resposible for all calculations and logics


# This object containes information about the data that is stored within it
class DataObject:
    def __init__(self, data_name, print_format=None) -> None:
        self.data_name = data_name
        self.item = {}
        self.print_format = print_format

    def retrieve(self):
        return self.item


class RuntimeDataAccessor:
    def __init__(self) -> None:
        self.es = DataObject('Education State')
        self.egd = DataObject('Education Grade')
        self.egp = DataObject('Education Group')
        self.lesson = DataObject('Lesson')
        self.gender = DataObject('Gender')
        self.person = DataObject('Person')
        self.school = DataObject('School')
        self.croom = DataObject('ClassRoom')
