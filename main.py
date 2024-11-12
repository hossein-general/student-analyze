# region IMPORTING
# For a cleaner look
from os import system
from pprint import pprint

# Other packages
from datetime import datetime

# Program Modules
import faker
from ui import Program
from bl import RuntimeDataAccessor
from dal import run

# endregion


# main: Containing functions for users to modify and manage the applicatoin (like adding person, organization, etc.)
def main():
    data = RuntimeDataAccessor()

    # region initializations and fakers
    faker.init_data(data)
    person_gen = faker.fake_person(data, 5)
    for new_person in person_gen:
        data.person.item[new_person.id] = new_person

    # endregion
    
    # only for direct dal access
    if input('do you wanna directly connect to dal? (enter empty)')== "":
        run(data)

    # running the ui app
    program = Program(data)
    program.start()

    system("cls")
    print("Good Luck")


if __name__ == "__main__":
    main()
