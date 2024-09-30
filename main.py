# For a cleaner look
from os import system

# As a cleaner printing option
from pprint import pprint

# Main modules for program
from student_analyze import (
    Student,
    Teacher,
    EducationState,
    EducationGrade,
    EducationGroup,
    EducationTerm,
    Lesson,
    ClassSession,
    ClassSchedule,
    ClassGroup,
    ClassRoom,
    School,
    gtattr,
    GovPerson,
)


def main():
    # # Cleaning the screen
    # system("cls")

    # # Running the debugger
    # import ipdb; ipdb.set_trace()

    # -------------------------------------------------
    # General Information Initializing:
    # Creating all excisting EducationStates
    education_states = {}
    education_states["ps"] = EducationState("Primary School")
    education_states["hs1"] = EducationState("High School 1st Term")
    education_states["hs2"] = EducationState("High School 2nd Term")
    education_states["u"] = EducationState("University")

    # Creating EducationGrades for each and all EducationState
    education_states["ps"].add_grade("1st grade")
    education_states["ps"].add_grade("2nd grade")
    education_states["ps"].add_grade("3rd grade")
    education_states["ps"].add_grade("4th grade")
    education_states["ps"].add_grade("5th grade")
    education_states["ps"].add_grade("6th grade")

    education_states["hs1"].add_grade("7th grade")
    education_states["hs1"].add_grade("8th grade")
    education_states["hs1"].add_grade("9th grade")

    education_states["hs2"].add_grade("10th grade")
    education_states["hs2"].add_grade("11th grade")
    education_states["hs2"].add_grade("12th grade")

    education_states["u"].add_grade("Bachelor")
    education_states["u"].add_grade("Master")
    education_states["u"].add_grade("Ph.D")

    # -------------------------------------------------
    # Creating the government
    gov = GovPerson()

    # -------------------------------------------------
    # School Information Initializing
    # Creating a School
    test_school = School("Shahid Abbass Hesaraki", education_states["ps"])

    # Creating classrooms for the school
    test_school.add_classroom("room 1", "room 2", "room 3")

    # Adding Students
    test_school.add_student(
        "Hossein", "Ramezani", education_states["ps"], education_states["ps"][0]
    )  # a first grade student

    # Adding Teachers

    # -------------------------------------------------
    # For Testing Purposes:

    import ipdb; ipdb.set_trace()

    pprint(gtattr(test_school))

    print("end")


if __name__ == "__main__":
    main()
