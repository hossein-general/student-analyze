# region Module Documention
# This module containes classes that are globaly used for education related stuff


# endregion


# region E-State
# EducationState will define type of education states wich affects different school types
# e.g. Primary School, High School 1st Term, High School 2nd Term, University
class EducationState:
    __es_list = []

    # The insert_to parameter is used to manage the order of stages
    def __init__(self, state_name, insert_to: int = None):
        self.state_name = state_name
        # instead of creating id's for each educationgrade, im using a list that supports order, so i could now which grade comes after another in its order
        self.__educationgrades = list()
        self.__educationgroup = set()
        # TODO Creating variables that will be initialized when an instance is created, and will manage School realations
        if insert_to is None:
            self.__class__.__es_list.append(self)
        else:
            self.__class__.__es_list.insert(insert_to, self)

    # this method is used to create a new educationGrade though an educationState instance, which is the main way of doing so.
    def add_grade(self, educationgrade_name):
        new_educationgrade = EducationGrade(self, educationgrade_name)
        self.__educationgrades.append(new_educationgrade)
        return new_educationgrade

    def add_group(self, educationgroup_name):
        new_educationgroup = EducationGroup(self, educationgroup_name)
        self.__educationgroup.add(new_educationgroup)
        return new_educationgroup

    def educationgrades(self):
        return self.__educationgrades

    def __str__(self):
        return self.state_name

    def __repr__(self):
        return f'<EducationState: "{self.state_name}">'

    # Returning the list of education states by order
    @classmethod
    def list(cls):
        return cls.__es_list


# endregion


# region E-Grade
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

    def __repr__(self):
        return f'<EducationGrade: "{self.name}">'


# endregion


# region E-Group
# EducationGroups are created to define different fields of study in differen EducationStates
# Each person could be assigned to multiple groups (e.g. both 'Dedicated lessons' and 'generic lessons')
# e.g. General, Tajrobi, Riazi, Mohandesi mechanic, ...
class EducationGroup:
    def __init__(self, parent_educationstate, name):
        self.parent_educationstate = parent_educationstate
        self.name = name
        self.lessons = set()

    # Adding an already created lesson to lessons list inside the education group
    def add_lesson(self, lesson_name, education_grade, prerequisite):
        new_lesson = Lesson(self, lesson_name, education_grade, prerequisite = None)
        self.lessons.add(new_lesson)
        return new_lesson

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<EducationGroup: "{self.name}">'


# endregion


# region Lesson
class Lesson:
    def __init__(self, parent_educationgroup: EducationGroup, name: str, educationgrade: EducationGrade, prerequisite: 'Lesson' = None):
        # The EducationGroup that this lesson belongs to
        self.parent_educationgroup = parent_educationgroup
        # The grade that this lesson is presenting in
        self.educationgrade = educationgrade
        # The name of that lesson
        self.name = name
        # The lessons that are necessary to be learned before starting this lesson (e.g. math-1 should be learned before math-2)
        self.prerequisite = prerequisite

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<Lesson: "{self.name}">'

# endregion


# region E-Term
# EducationTerms are not yet defined, but will manage the date system for learnings
# Something like "1 year for each grade of highschool state, 4 month for each term of university, etc..."
# TODO complete the EducationTerm class
class EducationTerm:
    def __init__(self, parent_educationstate, name, order):
        self.parent_educationstate = parent_educationstate
        self.name = name
        self.order = order

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<EducationTerm: "{self.name}">'

# endregion
