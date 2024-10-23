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
    ClassSession,
    ClassSchedule,
    ClassGroup,
    ClassRoom,
    School,
    gtattr,
    # GovPerson, # Renamed to Person
)

# Program Modules
import faker
from ui import Program

# endregion


# main: Containing functions for users to modify and manage the applicatoin (like adding person, organization, etc.)
def main():
    es = {}
    eg = {}
    genders = {}
    person = {}

    # region initializations and fakers
    es, eg, gender = faker.init_data()
    person_gen = faker.fake_person(eg, gender)
    for person in person_gen:
        pass
    # endregion

    program = Program()
    program.main_menue()

if __name__ == "__main__":
    main()

    # initialization
    # -------------------------------------------------
    # # General Information Initializing:
    # # Creating all excisting EducationStates
    # # a list (as it supports order) containing es
    # # TODO i should add some functions to manage order for the education state
    # es = []

    # es["ps"] = EducationState("Primary School")
    # es["hs1"] = EducationState("High School 1st Term")
    # es["hs2"] = EducationState("High School 2nd Term")
    # es["u"] = EducationState("University")

    # # Creating EducationGrades for each and all EducationState
    # # each education state will create its own education grade instances and stores them within itself
    # es["ps"].add_grade("1st grade")
    # es["ps"].add_grade("2nd grade")
    # es["ps"].add_grade("3rd grade")
    # es["ps"].add_grade("4th grade")
    # es["ps"].add_grade("5th grade")
    # es["ps"].add_grade("6th grade")

    # es["hs1"].add_grade("7th grade")
    # es["hs1"].add_grade("8th grade")
    # es["hs1"].add_grade("9th grade")

    # es["hs2"].add_grade("10th grade")
    # es["hs2"].add_grade("11th grade")
    # es["hs2"].add_grade("12th grade")

    # # in persion: Lisanse
    # es["u"].add_grade("Bachelor")
    # # in persian: foghlisans
    # es["u"].add_grade("Master")
    # #  in persian: doctora
    # es["u"].add_grade("Ph.D")

    # # -------------------------------------------------
    # # School Information Initializing
    # # Creating a School
    # test_school = School("Shahid Abbass Hesaraki", es["ps"])

    # # Creating classrooms for the school
    # test_school.add_classroom("room 1", "room 2", "room 3")

    # # Adding Students
    # test_school.add_student(
    #     "Hossein", "Ramezani", es["ps"], es["ps"][0]
    # )  # a first grade student

    # # Adding Teachers
    # # ...

    # # Person
    # person = {}
    # person_temp = Person("Hossein", "Ramezani", datetime(2020, 5, 17), eg["10th"])
    # person[person_temp.id] = person_temp

    # person_temp = Person("Mohammadmahdi", "Ramezani", datetime(2023, 3, 11), eg["7th"])
    # person[person_temp.id] = person_temp

    # Adding logs to the WorkingLog
