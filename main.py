# For cleaner look
from os import system

# For cleaner printing option
from pprint import pprint

# Main imported modules for program
from student_analyze import (
    Student,
    Teacher,
    SchoolType,
    EducationGrade,
    EducationGroup,
    Lesson,
    ClassSession,
    ClassSchedule,
    ClassGroup,
    ClassRoom,
    School,
    getattributes,
)


def main():
    # # Cleaning the screen
    # system("cls")

    # # Running the debugger
    # import ipdb; ipdb.set_trace()

    # -------------------------------------------------
    # General Information Initializing:
    # Creating all excisting SchoolTypes
    school_types = {}
    school_types["ps"] = SchoolType("Primary School")
    school_types["hs1"] = SchoolType("High School 1st Term")
    school_types["hs2"] = SchoolType("High School 2nd Term")
    school_types["u"] = SchoolType("University")

    # Creating EducationGrades for each and all SchoolType
    school_types["ps"].add_grade("1st grade")
    school_types["ps"].add_grade("2nd grade")
    school_types["ps"].add_grade("3rd grade")
    school_types["ps"].add_grade("4th grade")
    school_types["ps"].add_grade("5th grade")
    school_types["ps"].add_grade("6th grade")

    school_types["hs1"].add_grade("7th grade")
    school_types["hs1"].add_grade("8th grade")
    school_types["hs1"].add_grade("9th grade")

    school_types["hs2"].add_grade("10th grade")
    school_types["hs2"].add_grade("11th grade")
    school_types["hs2"].add_grade("12th grade")

    school_types["u"].add_grade("Bachelor")
    school_types["u"].add_grade("Master")
    school_types["u"].add_grade("Ph.D")

    # pprint(getattributes(school_types["u"]))

    # -------------------------------------------------
    # School Information Initializing
    # Creating a School
    test_school = School("Alameh Tabatabai", school_types["ps"])

    # Creating a classroom for the school
    test_school.add_classroom("room 1", "room 2", "room 3")

    # -------------------------------------------------
    # For Testing Purposes:


    import ipdb; ipdb.set_trace()
    pprint(getattributes(test_school))


    # pprint(getattributes(school_types["u"]))

    # pprint(getattributes(school_types["u"]))
    # system("cls")
    # print("=============================")
    # print("test_school.__dict__: \n")
    # pprint(test_school.__dict__)

    # print("=============================")
    # print("vars(test_school): \n")
    # pprint(vars(test_school))

    # print("=============================")
    # print("dir(teat_school): \n")
    # pprint(dir(test_school))

    # print("=============================")

    # pprint(getattributes(test_school))
    # print("End of the program!")
    
    print("end")


if __name__ == "__main__":
    main()
