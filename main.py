# For a cleaner look
from os import system

# As a cleaner printing option
from pprint import pprint

# Main modules for program
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
from datetime import datetime


def main():
    # # Cleaning the screen
    # system("cls")

    # # Running the debugger
    # import ipdb; ipdb.set_trace()

    # region old style educationstate/educationgrade/school/classroom initialization
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

    # endregion

    # region new style eudcationstate
    # Creating EducationState's
    es = {}
    es['ps'] = EducationState('Primary School')
    es['hs1'] = EducationState('High School 1st')
    es['hs2'] = EducationState('High School 2nd')
    es['u'] = EducationState('University')

    # Creating
    eg = {}
    eg['1st'] = es["ps"].add_grade("1st grade")
    eg['2nd'] = es["ps"].add_grade("2nd grade")
    eg['3rd'] = es["ps"].add_grade("3rd grade")
    eg['4th'] = es["ps"].add_grade("4th grade")
    eg['5th'] = es["ps"].add_grade("5th grade")
    eg['6th'] = es["ps"].add_grade("6th grade")

    eg['7th'] = es["hs1"].add_grade("7th grade")
    eg['8th'] = es["hs1"].add_grade("8th grade")
    eg['9th'] = es["hs1"].add_grade("9th grade")

    eg['10th'] = es["hs2"].add_grade("10th grade")
    eg['11th'] = es["hs2"].add_grade("11th grade")
    eg['12th'] = es["hs2"].add_grade("12th grade")

    # in persion: Lisanse
    eg['bachelor'] = es["u"].add_grade("Bachelor")
    # in persian: foghlisans
    eg['master'] = es["u"].add_grade("Master")
    #  in persian: doctora
    eg['phd'] = es["u"].add_grade("Ph.D")
    # endregion

    # region new style person
    # Creating a Person
    person1 = Person("Hossein", "Ramezani", datetime(2020, 5, 17), eg['10th'])
    person2 = Person("Mohammadmahdi", "Ramezani", datetime(2023, 3, 11), eg['7th'])
    # Adding logs to the WorkingLog
    

    # endregion

    # ===================================================================
    # For Testing Purposes:
    import ipdb
    ipdb.set_trace()
    print("end")


if __name__ == "__main__":
    main()
