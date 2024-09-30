# EducationState will define type of education states wich affects different school types 
# e.g. Primary School, High School 1st Term, High School 2nd Term, University
class EducationState:
    def __init__(self, state_name):
        self.state_name = state_name
        self.educationgrades = list()
        # TODO Creating variables that will be initialized when an instance is created, and will manage School realations

    def add_grade(self, educationgrade_name):
        new_educationgrade = EducationGrade(self, educationgrade_name)
        self.educationgrades.append(new_educationgrade)

    def __str__(self):
        return self.state_name


# EducationGrades are stages within each EducationState that are defining the path for each student
# e.g. the primary school has 6 grades from 1st to 6th grade
#   then high school 1st term has 3, starting with 7th and ending with 9th grade
#   high school 2nd term continues like this till 12th grade
#   and at the end, universities having 3 main stages: Bachelor's degree, Master's degree, and Ph.D
# EducationGrade and SchoolTyeps are different from EducationGroups
#   The first two are used to define where is an student in life time of education and the other defines the field of study
class EducationGrade:
    def __init__(self, parent_educationstate, name):
        self.parent_educationstate = parent_educationstate
        self.name = name

    def __str__(self):
        return self.name


# EducationGroups are created to define different fields of study in differen EducationStates
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

    def __str__(self):
        return self.name


class Lesson:
    def __init__(self, parent_educationgroup, name):
        self.parent_educationgroup = parent_educationgroup
        self.name = name

    def __str__(self):
        return self.name


class EducationTerm:
    def __init__(self, parent_educationstate, name, order):
        self.parent_educationstate = parent_educationstate
        self.name = name
        self.order = order

    def __str__(self):
        return self.name
