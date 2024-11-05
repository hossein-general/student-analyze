# region  Documention
# This module containes classes that are globaly used for education related stuff

# endregion

# imports
from .Validations import Validator

# for type hints (type annotations)
from typing import Union, List


# region E-State <13>
# EducationState will define type of education states wich affects different school types
# e.g. Primary School, High School 1st Term, High School 2nd Term, University
# TODO adding a decorator to store all created instances
class EducationState(Validator):
    __es_list = []
    cls_name = "EducationState"

    # The insert_to parameter is used to manage the order of stages
    def __init__(self, state_name: str, insert_to: int = None):
        # a dictionary containing parameter values and the desired type for each
        attr_types = (
            (state_name, str),
            (insert_to, (int, type(None))),
        )

        # Type Validations
        self.init_check_type(attr_types)

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
    def add_grade(
        self,
        educationgrade_name: str,
    ):
        # Validations
        self.check_type(educationgrade_name, str)

        new_educationgrade = EducationGrade(self, educationgrade_name)
        self.__educationgrades.append(new_educationgrade)
        return new_educationgrade

    def add_group(
        self,
        educationgroup_name: str,
        generic_dependency: Union["EducationGroup", List["EducationGroup"]] = [],
        direct_use: bool = True,
    ):
        # a dictionary containing parameter values and the desired type for each
        attr_types = (
            (educationgroup_name, str),
            (generic_dependency, (EducationGroup, list), EducationGroup),
            (direct_use, bool),
        )

        # Type Validations
        self.init_check_type(attr_types)

        # Creating and adding the instance
        new_educationgroup = EducationGroup(
            self, educationgroup_name, direct_use, generic_dependency
        )
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


# region E-Grade <90>
# EducationGrades are stages within each EducationState that are defining the path for each student
# e.g. the primary school has 6 grades from 1st to 6th grade
#   then high school 1st term has 3, starting with 7th and ending with 9th grade
#   high school 2nd term continues like this till 12th grade
#   and at the end, universities having 3 main stages: Bachelor's degree, Master's degree, and Ph.D
# EducationGrade and SchoolTyeps are different from EducationGroups
#   The first two are used to define where is an student in life time of education and the other defines the field of study
class EducationGrade(Validator):
    cls_name = "EducationGrade"

    def __init__(
        self,
        parent_educationstate: EducationState,
        name: str,
    ):
        # a dictionary containing parameter values and the desired type for each
        attr_types = (
            (parent_educationstate, EducationState),
            (name, str),
        )

        # Type Validations
        self.init_check_type(attr_types)

        # Initialization
        self.parent_educationstate = parent_educationstate
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<EducationGrade: "{self.name}">'


# endregion


# region E-Group <135>
# EducationGroups are created to define different fields of study in differen EducationStates
# Each person could be assigned to multiple groups (e.g. both 'Dedicated lessons' and 'generic lessons')
# e.g. General, Tajrobi, Riazi, Mohandesi mechanic, ...
# Dedicated education groups like riazi and mohandesi shimi do have generic dependencies
#   e.g. General group lessons that are the same for every dedicated group like dini, ghoran, etc.
class EducationGroup(Validator):
    cls_name = "EducationGroup"

    def __init__(
        self,
        parent_educationstate: EducationState,
        name: str,
        direct_use: bool = True,
        generic_dependency: Union["EducationGroup", List["EducationGroup"]] = [],
    ):
        # a dictionary containing parameter values and the desired type for each
        attr_types = (
            (parent_educationstate, EducationState),
            (name, str),
            (direct_use, bool),
            (generic_dependency, (list, EducationGroup), EducationGroup),
        )

        # Type Validations
        self.init_check_type(attr_types)

        # Initializations
        self.parent_educationstate = parent_educationstate
        self.name = name
        self.direct_use = direct_use

        # checking wether the input parameters are iterables or not
        # TODO adding further validation to check if the input values actually match the type hints
        if hasattr(generic_dependency, "__iter__"):
            self.generic_dependency = set(generic_dependency)
        else:
            self.generic_dependency = {generic_dependency}

        # Data Containers
        self.lessons = set()

    # Adding an already created lesson to lessons list inside the education group
    def add_lesson(
        self,
        lesson_name: str,
        education_grade: EducationGrade,
        grade_base_prerequisite: List["Lesson"] = [],
    ):
        # a dictionary containing parameter values and the desired type for each
        attr_types = (
            (lesson_name, str),
            (education_grade, EducationGrade),
            (grade_base_prerequisite, list, Lesson),
        )

        # Type Validations
        self.init_check_type(attr_types)

        # Creating and adding the instance
        new_lesson = Lesson(
            self,
            lesson_name,
            education_grade,
            grade_base_prerequisite,
        )
        self.lessons.add(new_lesson)
        return new_lesson

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<EducationGroup: "{self.name}">'


# endregion


# BUG if user creates a Lesson instance directly, and does not compliance validation rules, the instace will be created any ways, and validations may not prevent that
# NOTE the validations within Lesson class are only used to inform user about the incoming bugs and would not prevent them from doing anythin (as it sis direct access)
# region Lesson <231>
class Lesson(Validator):
    cls_name = "Lesson"

    Validator.msg["lesson-prerequisites"] = (
        'the lesson: "{caller_instane}" and its prerequisite: "{content_1}" are not of the same education grade: "{content_2}"'
    )

    def __init__(
        self,
        parent_educationgroup: EducationGroup,
        name: str,
        educationgrade: EducationGrade,
        grade_base_prerequisite: List["Lesson"] = [],
    ):
        # Parameter formatting
        # to handle not supported format of arguments and make the function easier to use
        # TODO modifying __str__ and __repr__ to handle not having first name and last name defined and removing this part
        if not hasattr(grade_base_prerequisite, "__iter__"):
            grade_base_prerequisite = [grade_base_prerequisite]
        # a dictionary containing parameter values and the desired type for each
        attr_types = (
            (parent_educationgroup, EducationGroup),
            (name, str),
            (educationgrade, EducationGrade),
            (grade_base_prerequisite, list, Lesson),
        )

        # Type Validations
        self.init_check_type(attr_types)

        # NOTE It was necessary to puth attribute initialization before validation
        # (to prevent some errors like "Lesson object has no attribute 'name'" when calling its str)
        # The EducationGroup that this lesson belongs to
        self.parent_educationgroup = parent_educationgroup
        # The grade that this lesson is presenting in
        self.educationgrade = educationgrade
        # The name of that lesson
        self.name = name
        # The lessons that are necessary to be learned before starting this lesson (e.g. math-1 should be learned before math-2)
        self.grade_base_prerequisite = grade_base_prerequisite

        # Logical Validations
        # Checking if the lesson and the prerequisites of it are of a same education_grade
        self.is_same_as(
            self,
            grade_base_prerequisite,
            educationgrade,
            "educationgrade",
            "lesson-prerequisites",
        )
        # NOTE There is no need for validating education grops of them, as there could be prerequisites from differen classgroups to each other

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<Lesson: "{self.name}">'


# endregion


# region E-Term <302>
# EducationTerms are not yet defined, but will manage the date system for learnings
# Something like "1 year for each grade of highschool state, 4 month for each term of university, etc..."
# TODO complete the EducationTerm class and adding validations
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
