# region IMPORTING
# For a cleaner look
from os import system
from pprint import pprint

# Other packages
from datetime import datetime

# Modules from the main package
from student_analyze import (
    Person,
    # Student,  # Depricated
    # Teacher,  # Depricated
    EducationState,
    EducationGrade,  # i think its unnecessary (as its automatically created)
    EducationGroup,
    EducationTerm,
    Lesson,
    School,
    gtattr,
    # GovPerson, # Renamed to Person
)

# Program Modules
import faker
from ui import Program
from bl import RuntimeDataAccessor

# endregion


# main: Containing functions for users to modify and manage the applicatoin (like adding person, organization, etc.)
def main():
    data = RuntimeDataAccessor()
    
    # region initializations and fakers
    faker.init_data(data)
    person_gen = faker.fake_person(data, 20)
    for new_person in person_gen:
        data.person.list[new_person.id] = new_person

    # endregion

    program = Program(data)
    program.start()

    system("cls")    
    print("Good Luck")


if __name__ == "__main__":
    main()
