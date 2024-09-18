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
    # Running the debugger
    import ipdb

    ipdb.set_trace()

    # General Information Initializing:
    # Creating all excisting SchoolTypes
    school_types = {}
    school_types["ps"] = SchoolType("Primary School")
    school_types["hs1"] = SchoolType("High School 1st Term")
    school_types["hs2"] = SchoolType("High School 2nd Term")
    school_types["u"] = SchoolType("University")

    # -------------------------------------------------

    # School Information Initializing
    # Creating a School
    test_school = School("Alameh Tabatabai", school_types["ps"])

    # Creating a classroom for the school
    test_school.add_classroom("room 1", "room 2", "room 3")


if __name__ == "__main__":
    main()
