# This is the module which is resposible for all calculations and logics

# Importing
from student_analyze import Validator
from typing import Dict

# region DataObject
# This object containes information about the data that is stored within it
# TODO adding type validations for DataObject
class DataObject:
    cls_name = 'DateObject'

    # Creating a Validator object
    check = Validator()

    def __init__(self, data_name: str, printable_data: Dict[str, int] = None) -> None:
        # Type Validations
        self.check.check_type(
            data_name,
            str,
            'data_name',
            self.cls_name,
        )
        # TODO adding type validation for dict keys and values
        self.check.check_type(
            printable_data,
            (dict, type(None)),
            'printable_data',
            self.cls_name,
            inner_type=str,
        )

        # Initializations
        self.data_name = data_name
        self.item = {}
        self.printable_data = printable_data

    def retrieve(self):
        # Creating a tuple of item values
        items = tuple(self.item.values())
        values_len = tuple(self.printable_data.values())
        attrs = tuple(self.printable_data.keys())
        retrieving_content = []

        # Creating a base-text for formatting
        # the following line creates something like this:
        #   "{!s:<5}  {!s:<20} {!s:<20} {!s:<10} {!s:<25} {!s:<15} {!s:<72}"
        base_formatting_text = " ".join([f"{{!s:<{place_count}}}" for place_count in values_len])

        # iterating through the tuple to create formated string of it
        for item in items:
            # getting attribute values in the form of a tuple
            attr_values = [getattr(item, value) for value in attrs]

            # formatting values
            row = base_formatting_text.format(*attr_values)

            # appending the resaults
            retrieving_content.append(row)
        
        return retrieving_content

    def __str__(self):
        return self.data_name

    def __repr__(self):
        return f'<DataObject: "{self.data_name}">'

# endregion


# region Data Accessor
class RuntimeDataAccessor:
    def __init__(self) -> None:
        self.es = DataObject('Education State')
        self.egd = DataObject('Education Grade')
        self.egp = DataObject('Education Group')
        self.lesson = DataObject('Lesson')
        self.gender = DataObject('Gender')
        self.person = DataObject(
            'Person', 
            {
                'id': 5,
                'first_name': 20,
                'last_name': 20,
                'gender': 10,
                'birth_date': 25,
                'national_code': 15
            }
            )
        self.school = DataObject('School')
        self.croom = DataObject('ClassRoom')
        self.student = DataObject('Student')
        self.teacher = DataObject('Teacher')
        self.cg = DataObject('Class Group')

# TODO creating a decorator to keep record of any instance creation

# endregion

