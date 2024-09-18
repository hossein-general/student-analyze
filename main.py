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
)


def main():
    # Running the debugger
    import ipdb; ipdb.set_trace() 

    # General Information Initializing:
    # Creating all excisting SchoolTypes
    st_ps = SchoolType("Primary School")
    st_hs1 = SchoolType("High School 1st Term")
    st_hs2 = SchoolType("High School 2nd Term")
    st_u = SchoolType("University")

    # -------------------------------------------------

    # School Information Initializing
    # Creating a School
    test_school = School("Alameh Tabatabai", st_ps)

    # Creating a classroom for the school
    test_school.add_classroom("room 1", "room 2", "room 3")


if __name__ == "__main__":
    main()
