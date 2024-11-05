# This is the module which is resposible for all calculations and logics

# region importing

# Importing
from student_analyze import Validator
from typing import Dict

# endregion


# region DataObject
# This object containes information about the data that is stored within it
# TODO adding type validations for DataObject
class DataObject:
    cls_name = "DateObject"

    # Creating a Validator object
    check = Validator()

    def __init__(self, data_name: str, printable_data: Dict[str, int] = None) -> None:

        # a tuple containing tuples of arguments to be used when passed to type validation
        attr_types = (
            (data_name, str),
            (printable_data, dict, str, int),
        )

        # Type Validations
        self.check.init_check_type(attr_types)

        # Initializations
        self.data_name = data_name
        self.item = {}
        self.printable_data = printable_data

    def retrieve(self):
        # Creating a tuple of item values
        items = tuple(self.item.values())
        attrs = self.printable_data.keys

        return items, attrs
        attrs = tuple(self.printable_data.keys())
        values_len = tuple(self.printable_data.values())

        # this list contains the formatted data, each item is a row as a string
        retrieving_content = []

        # Creating a base-text for formatting
        # the following statement creates something like this:
        #   "{!s:<5}  {!s:<20} {!s:<20} {!s:<10} {!s:<25} {!s:<15} {!s:<72}"
        base_formatting_text = " ".join(
            [f"{{!s:<{place_count}}}" for place_count in values_len]
        )

        # iterating through the tuple to create formated string of it
        for item in items:
            # getting attribute values in the form of a tuple
            attr_values = [getattr(item, value) for value in attrs]

            # formatting values
            row = base_formatting_text.format(*attr_values)

            # appending the resaults
            retrieving_content.append(row)

        col_names = base_formatting_text.format(*attrs)

        return retrieving_content, col_names

    def __str__(self):
        return self.data_name

    def __repr__(self):
        return f'<DataObject: "{self.data_name}">'


# endregion


# region Data Accessor
class RuntimeDataAccessor:
    def __init__(self) -> None:
        self.es = DataObject(
            "Education State",
            {
                "state_name": 5,
            },
        )
        self.egd = DataObject(
            "Education Grade",
            {
                "name": 12,
                "parent_educationstate": 5,
            },
        )
        self.egp = DataObject(
            "Education Group",
            {
                "parent_educationstate": 25,
                "name": 45,
                "direct_use": 15,
                "generic_dependency": 55,
                "lessons": 40,
            },
        )
        self.lesson = DataObject(
            "Lesson",
            {
                "name": 15,
                "parent_educationgroup": 30,
                "educationgrade": 30,
                "grade_base_prerequisite": 50,
            },
        )
        self.gender = DataObject("Gender", {"name": 8, "prefix": 10})
        self.person = DataObject(
            "Person",
            {
                "id": 5,
                "first_name": 20,
                "last_name": 20,
                "gender": 10,
                "birth_date": 25,
                "national_code": 15,
            },
        )
        self.school = DataObject(
            "School", {"name": 33, "education_state": 40, "education_group": 55}
        )
        self.croom = DataObject(
            "ClassRoom",
            {
                "name": 15,
                "parent_school": 33,
                "parent_assigned_id": 25,
            },
        )
        self.student = DataObject(
            "Student",
            {
                "student_id": 13,
                "person": 40,
                "parent_school": 33,
                "education_grade": 25,
                "education_group": 35,
            },
        )
        self.teacher = DataObject(
            "Teacher",
            {
                "teacher_id": 15,
                "person": 30,
                "parent_school": 33,
                "presenting_lessons": 40,
            },
        )
        self.cg = DataObject(
            "Class Group",
            {
                "group_id": 10,
                "parent_school": 33,
                "educationgrade": 22,
                "educationgroup": 30,
                "teacher": 20,
                "lesson": 15,
                "students": 1,
            },
        )


# TODO creating a decorator to keep record of any instance creation

# endregion
