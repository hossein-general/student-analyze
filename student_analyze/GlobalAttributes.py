# SchoolType will define type of schools
# e.g. Primary School, High School 1st Term, High School 2nd Term, University
class SchoolType:
    __slots__ = ["type_name", "educationgrades"]

    def __init__(self, type_name):
        self.type_name = type_name
        self.educationgrades = set()
        # TODO Creating variables that will be initialized when an instance is created, and will manage School realations

    def add_grade(self, educationgrade_name):
        new_educationgrade = EducationGrade(self, educationgrade_name)
        self.educationgrades.add(new_educationgrade)


# EducationGrades are stages within each SchoolType that are defining the path for each student
# e.g. the primary school has 6 grades from 1st to 6th grade
#   then high school 1st term has 3, starting with 7th and ending with 9th grade
#   high school 2nd term continues like this till 12th grade
#   and at the end, universities having 3 main stages: Bachelor's degree, Master's degree, and Ph.D
# EducationGrade and SchoolTyeps are different from EducationGroups
#   The first two are used to define where is an student in life time of education and the other defines the field of study
class EducationGrade:
    def __init__(self, parent_schooltype, name):
        self.name = name

    
# EducationGroups are created to define different fields of study in differen SchoolTypes
# e.g. General, Tajrobi, Riazi, Mohandesi mechanic, ...
class EducationGroup:
    def __init__(self, educationgrade, name):
        self.educationgrade = educationgrade
        self.name = name
        self.lessons = set()

    # Adding an already created lesson to lessons list inside the education group
    def add_lesson(self, lesson_name):
        new_lesson = Lesson(self, lesson_name)
        self.lessons.add(new_lesson)


class Lesson:
    def __init__(self, parent_educationgroup, name):
        self.parent_educationgroup = parent_educationgroup
        self.name = name
