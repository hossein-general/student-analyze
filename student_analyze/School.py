# This module containes School related classes
# These Classes only have meaning in the context of schools
# The School class within this module inharites from the Organizations class within the Organizations module

# region importing
from .Validations import Validator
from .Organization import Organization
from .Persons import Person
from .GlobalAttributes import (
    EducationState,
    EducationGroup,
    EducationGrade,
    Lesson,
)

# for type hints (type annotations)
from typing import Union, List

# endregion

# region School


# School class
# TODO making the schools gender specific (or at least an option for that)
class School(Organization):
    # Validator object
    check = Validator()
    cls_name = "School"

    # region __init__
    def __init__(
        self,
        name: str,
        education_states_list: Union[EducationState, List[EducationState]],
        education_groups_list: Union[EducationGroup, List[EducationGroup]],
    ):
        # region <type valid>
        # Type Validations
        self.check.check_type(
            name,
            str,
            "name",
            self.cls_name,
        )
        self.check.check_type(
            education_states_list,
            (EducationState, list),
            "education_states_list",
            self.cls_name,
            inner_type=EducationState,
        )
        self.check.check_type(
            education_groups_list,
            (EducationGroup, list),
            "educatoin_groups_list",
            self.cls_name,
            inner_type=EducationGroup,
        )
        # endregion

        # region <Init>
        # initializations
        self.name = name
        self.education_state = set()
        self.education_group = set()

        # checking wether the input parameters are iterables or not
        if hasattr(education_states_list, "__iter__"):
            self.education_state.update(education_states_list)
        else:
            self.education_state.add(education_states_list)

        if hasattr(education_groups_list, "__iter__"):
            self.education_group.update(education_groups_list)
        else:
            self.education_group.add(education_groups_list)

        # endregion

        # region <logic valid>
        # Validation
        # - checking if education groups within the school list are compatible with  the education statets
        # - checking for each education groups generic dependency to be included within the school education_group
        # TODO im not sure what would happen to the instance when it raises an error mid-init. i should check on that later
        # TODO creating custom errors for different sitiuations
        # TODO adding validation for not having only generic education groups
        for group in self.education_group:
            if the_state := group.parent_educationstate not in self.education_state:
                raise ValueError(
                    f'the education group {group}\'s education state is not within the given education_states_list: "{the_state}"'
                )

            for dependency in group.generic_dependency:
                if dependency not in self.education_group:
                    raise ValueError(
                        f'the education group {group} has a generic dependency that is not assigned to school: "{dependency}"'
                    )

        # endregion

        # region <data container>
        # Data Containers
        self.classrooms = dict()
        self.students = dict()
        self.teachers = dict()
        self.classgroups = dict()

        # endregion

        # region <generator>
        # ID Generators
        self.classroom_id_pool = self.generate_id("classroom")
        self.student_id_pool = self.generate_id("student")
        self.teacher_id_pool = self.generate_id("teacher")
        self.classgroup_id_pool = self.generate_id("classgroup")

        # endregion

    # endregion
    
    # region c-room
    # Create add adding multiple classrooms to the school

    def add_classrooms(
        self,
        *classroom_names: Union[str, int],
        starting_id: int = None,
    ):
        # NOTE the funcion accepts integer numbers as classroom name and uses the str() to make them string

        # Valiations
        self.check.check_type(
            classroom_names,
            tuple,
            "classroom_names",
            "ClassRoom",
            inner_type=(str, int),
        )
        self.check.check_type(
            starting_id,
            (int, type(None)),
            "starting_id",
            "ClassRoom",
        )

        # a list to be return at the end of the function
        created_crooms = []

        # deciding if i want to use my own id pattern or the default one
        if starting_id is None:
            id_pattern = self.classroom_id_pool
        else:
            id_pattern = self.generate_id("custom", starting_id)

        # stating to crete classrooms (iterating though names and giving each an id)
        for name in classroom_names:
            # Generate an id for the new classroom
            classroom_id = next(id_pattern)
            # Creating an instance of ClassRoom
            new_classroom = self.ClassRoom(self, classroom_id, str(name))
            # Assigning the newly created classroom to classrooms dict and the tempore list
            self.classrooms[classroom_id] = new_classroom
            created_crooms.append(new_classroom)

        return created_crooms

    # endregion

    # region c-group

    # Creating a ClassGroup for the school
    # TODO most of the parameters should be removed and be placed within the function to get
    """I can think of two different ways to get the necessary inputs from user
    one is to get them one by one from user while the add method is open, 
    and the other is to first fill the requirements within a form and at the end sending them to tha add method
    im not sure if there is any risk of problems in first method
    this idea applies to many other parts of my program, and maybe ill change my structure in the future"""

    # TODO adding validation for type hints
    def add_classgroup(
        self,
        educationgrade: EducationGrade,
        educationgroup: EducationGroup,
        teacher: "School.Teacher",
        lesson: Lesson,
        student_list: List["School.Student"] = [],
    ):
        # Validations
        self.check.check_type(
            educationgrade,
            EducationGrade,
            "educationgrade",
            "ClassGroup",
        )
        self.check.check_type(
            educationgroup,
            EducationGroup,
            "educationgroup",
            "ClassGroup",
        )
        self.check.check_type(
            teacher,
            School.Teacher,
            "teacher",
            "ClassGroup",
        )
        self.check.check_type(
            lesson,
            Lesson,
            "lesson",
            "ClassGroup",
        )
        self.check.check_type(
            student_list, list, "stukdent_list", "ClassGroup", inner_type=School.Student
        )

        # Generate an id for the new classgroup
        classgroup_id = next(self.classgroup_id_pool)
        # Creating an instance of ClassGroup
        new_classgroup = self.ClassGroup(
            self,
            classgroup_id,
            educationgrade,
            educationgroup,
            teacher,
            lesson,
            student_list,
        )
        # Assigning the newly created classgroup to the classgroups dict
        self.classgroups[classgroup_id] = new_classgroup
        return new_classgroup

    # endregion

    # region student

    # Creating new students and assigning them to the school
    # TODO adding validation for type hints
    def add_student(
        self,
        person: Person,
        education_grade: EducationGrade,
        education_group: EducationGroup,
    ):
        # Type Validations
        self.check.check_type(
            person,
            Person,
            "person",
            "Student",
        )
        self.check.check_type(
            education_grade,
            EducationGrade,
            "education_grade",
            "Student",
        )
        self.check.check_type(
            education_group,
            EducationGroup,
            "education_group",
            "Student",
        )

        # Logical Validation
        # checking if the students education state and education group is within the school's egp and es list
        if (
            the_es := education_grade.parent_educationstate
        ) not in self.education_state:
            raise ValueError(
                f'the student {person}\'s education state is not within the school education_states list: "{the_es}"'
            )

        # if the assigned education group is not a directly usable group
        if not education_group.direct_use:
            raise ValueError(
                f'the student {person}\'s education group is not directly assignable: "{education_group}"'
            )

        if education_group not in self.education_group:
            raise ValueError(
                f'the student {person}\'s education group is not within the school education_states group: "{education_group}"'
            )

        # Creating and returning the Student instance
        # Generating an id for the student
        student_id = next(self.student_id_pool)
        # Calling the Student class to create an instance of Student
        new_student = self.Student(
            self,
            student_id,
            person,
            education_grade,
            education_group,
        )
        # Adding the newly created student to students dict
        self.students[student_id] = new_student
        return new_student

    # endregion

    # region teacher
    def add_teacher(self, person: Person, *lessons: Lesson):
        # Type Validations
        self.check.check_type(
            person,
            Person,
            "person",
            "Teacher",
        )
        self.check.check_type(
            lessons,
            tuple,
            "lessons",
            "Teacher",
            inner_type=Lesson,
        )

        # Logical Validations
        # validating input lessons
        for lesson in lessons:
            # checking if the lessons are within schools education groups
            if (the_egp := lesson.parent_educationgroup) not in self.education_group:
                raise ValueError(
                    f'the teacher "{person}"\'s lessons\'s education group is not within the school "{self}" education_states group: "{the_egp}" lesson: "{lesson}"'
                )
            # There would not be any need to validate educaiton grade to be within the school list, as
            # if the education group is within the school then the education grade must be too

        # Creating and returning a Teacher instance
        # Generating an id for the teacher
        teacher_id = next(self.teacher_id_pool)
        # Calling the Teacher class to create an instance of Teacher
        new_teacher = self.Teacher(self, teacher_id, person, *lessons)
        self.teachers[teacher_id] = new_teacher
        return new_teacher

    # endregion

    # region ID genrator

    # This class will manage ids for each id-able item in the school
    # e.g. ClassRooms (classroom), Teachers (teacher), Students (student), etc.
    # This management happens by using a counter variable and adding one to it each time an id is assigned
    # each entity has its own id counter
    # This function is used within the class, where ever a new entity creates
    # ID Generator

    def generate_id(self, entity: str, start_id: int = None):
        # Type Validations
        self.check.check_type(
            entity,
            str,
            "entity",
            "id_generator",
        )
        self.check.check_type(
            start_id,
            (int, type(None)),
            "start_id",
            "id_generator",
        )

        # Creating Generator (matching the entity type name to generate desired id pattern)
        # TODO BUG i should find some way to prevent id duplication as data may be storde within the database
        last_id = start_id
        match entity:
            case "classroom":
                if last_id is None:
                    last_id = 100
                while True:
                    yield last_id
                    last_id += 1

            case "student":
                if last_id is None:
                    last_id = 200
                while True:
                    yield last_id
                    last_id += 1

            case "teacher":
                if last_id is None:
                    last_id = 300
                while True:
                    yield last_id
                    last_id += 1

            case "classgroup":
                if last_id is None:
                    last_id = 400
                while True:
                    yield last_id
                    last_id += 1

            case "custom":
                while True:
                    yield last_id
                    last_id += 1

            case _:
                raise ValueError("non-defined entity name for id assignment")

    def __str__(self):
        return self.name

    # endregion

    # region Nested Classes
    # this region containes nested classes
    # any class related to schoo will be defined here
    # classes: ClassRoom, ClassGroup, ClassSchedule, ClassSession

    # region C-Room
    # Classroom class which are called by School class instances. they are used as the place for holding class sessions

    # TODO adding __slot__ for all classes
    # TODO changing id type to str
    class ClassRoom:
        cls_name = "ClassRoom"

        # Creating Validator object
        check = Validator()

        def __init__(
            self,
            parent_school: "School",
            parent_assigned_id: int,
            name: str,
        ):
            # Type Validations
            self.check.check_type(
                parent_school,
                School,
                "parent_school",
                self.cls_name,
            )
            self.check.check_type(
                parent_assigned_id,
                int,
                "parent_assigned_id",
                self.cls_name,
            )
            self.check.check_type(
                name,
                str,
                "name",
                self.cls_name,
            )

            # Initializations
            self.parent_school = parent_school
            self.parent_assigned_id = parent_assigned_id
            self.name = name

        def __str__(self):
            return f"[{self.id}: {self.name}]"

    # endregion

    # Class Group class. its used to bind teachers, students, lessons, classrooms and adding schedule for each
    # region C-Group
    # I dont think if there would ever be a need to name a ClassGroup as its not user readable
    # NOTE There may not be need for education group and grade as they are accessible trhou lesson
    #   but i rather access them directly from classgroup itself rather than through lesson
    # TODO adding validation for type hints
    class ClassGroup:
        cls_name = "ClassGroup"

        # Creating Validator object
        check = Validator()

        def __init__(
            self,
            parent_school: "School",
            group_id: int,
            educationgrade: EducationGrade,
            educationgroup: EducationGroup,
            teacher: "School.Teacher",
            lesson: Lesson,
            student_list: List["School.Student"] = [],
        ):
            # Type Validations
            self.check.check_type(
                parent_school,
                School,
                "parent_school",
                self.cls_name,
            )
            self.check.check_type(
                group_id,
                int,
                "group_id",
                self.cls_name,
            )
            self.check.check_type(
                educationgrade,
                EducationGrade,
                "educationgrade",
                self.cls_name,
            )
            self.check.check_type(
                educationgroup,
                EducationGroup,
                "educationgroup",
                self.cls_name,
            )
            self.check.check_type(
                teacher,
                School.Teacher,
                "teacher",
                self.cls_name,
            )
            self.check.check_type(
                lesson,
                Lesson,
                "lesson",
                self.cls_name,
            )
            self.check.check_type(
                student_list,
                list,
                "student_list",
                self.cls_name,
                inner_type=School.Student,
            )

            # Initializations
            self.parent_school = parent_school
            self.group_id = group_id
            self.educationgrade = educationgrade
            self.educationgroup = educationgroup
            self.teacher = teacher
            self.lesson = lesson
            self.students = student_list

            # Data Containers
            self.classschedules = set()

            # ID Pools
            self.last_classschedule_id = 11000

        # Creating a class schedule

        def add_classschedule(
            self,
            teacher: "School.Teacher",
            lesson: Lesson,
        ):
            # Type Validations
            self.check.check_type(
                teacher,
                School.Teacher,
                "teacher",
                "ClassSchedule",
            )
            self.check.check_type(
                lesson,
                Lesson,
                "lesson",
                "ClassSchedule",
            )

            # Generating an id for the classschedule for new ClassSchedule
            classschedule_id = self.generate_id("cschedule")
            # Calling the ClassSchedule class to create an instance of it
            new_classschedule = self.ClassSchedule(
                self, classschedule_id, teacher, lesson
            )
            self.classschedules.add(new_classschedule)

        # TODO adding validation for type hints
        def generate_id(self, entity: str):
            # Type Validations
            self.check.check_type(
                entity,
                str,
                "entity",
                "id_generator",
            )

            # generating id base on the entity name for desired id pattern
            match entity:
                case "cschadule":
                    self.last_classschedule_id += 1
                    return self.last_classschedule_id
                case _:
                    raise TypeError(
                        f"{entity} is not an entity that would have an id pool in ClassGroup class. pls enter a valid option"
                    )

        def __str__(self):
            return self.id

    # endregion

    # region C-Schedule
    # This class shows which of the ClassGroup teachers is assigend and what lesson is he presenting (as a sible ClassGroup could hold many teachers and lessons at the same time)
    # In most cases the ClassSchedule instances are named by the lesson presenting within them, and sometimes combined with an id
    # e.g. "Riazi-1 20341", "Arabi", ...
    # TODO adding validation for type hints
    class ClassSchedule:
        def __init__(
            self,
            parent_classgroup: "School.ClassGroup",
            id: int,
        ):
            # initializations
            self.id = id
            self.parent_classgroup = parent_classgroup
            # empty data container
            self.classsessions = set()

        def add_classsession(self, start_session, end_session, student_list, teacher):
            # TODO Getting start_session and removing from parameters
            # TODO Getting end_session and removing from parameters
            # TODO Inhariting teacher
            # TODO Inhariting student_list
            # TODO Inhariting lesson
            new_classsession = self.ClassSession(
                self, start_session, end_session, student_list, teacher
            )
            self.classsessions.add(new_classsession)

        def __str__(self):
            return f"{self.lesson}-{self.id}"

    # endregion

    # region C-Sessions
    # TODO The ClassSession class should be inherited from the ClassSchedule class so it will be containing infrmations like students list, teacher, lesson and etc by default
    # ClassSessions are instances that contain classSchedule information plus date & time information and is used for a single session
    # This class can be used for checking presence and absence of each studing within each session
    # Each ClassSession should only have one teacher

    # TODO adding type validations
    class ClassSession:
        def __init__(
            self,
            parent_classsession,
            start_time,
            end_time,
            student_list,
            teacher,
            lesson,
        ):
            self.parent_classsession = parent_classsession
            self.start_time = start_time
            self.end_time = end_time
            self.student_list = student_list
            self.teacher = teacher
            self.lesson = lesson

        def __str__(self):
            return f"{self.lesson} {self.start_time}-{self.end_time}"

    # endregion

    # region Student
    # Student
    # TODO adding validation for type hints
    class Student:
        cls_name = "Student"

        # Creating Validator object
        check = Validator()

        def __init__(
            self,
            parent_school: "School",
            student_id: int,
            person: Person,
            education_grade: EducationGrade,
            education_group: EducationGroup,
        ):
            # Type Validations
            self.check.check_type(
                parent_school,
                School,
                "parent_school",
                self.cls_name,
            )
            self.check.check_type(
                student_id,
                int,
                "student_id",
                self.cls_name,
            )
            self.check.check_type(
                person,
                Person,
                "person",
                self.cls_name,
            )
            self.check.check_type(
                education_grade,
                EducationGrade,
                "education_grade",
                self.cls_name,
            )
            self.check.check_type(
                education_group,
                EducationGroup,
                "education_group",
                self.cls_name,
            )

            # Initializations
            self.parent_school = parent_school
            self.student_id = student_id
            self.person = person
            self.education_grade = education_grade
            self.education_group = education_group
        
        def __str__(self):
            return f'{self.person.first_name} {self.person.last_name}'

    # endregion

    # region Teacher
    # Teacher
    # TODO adding validation for type hints
    class Teacher:
        cls_name = "Teacher"

        # Creating Validator object
        check = Validator()

        def __init__(
            self,
            parent_school: "School",
            teacher_id: int,
            person: Person,
            *presenting_lessons: Lesson,
        ):
            # Type Validations
            self.check.check_type(
                parent_school,
                School,
                "parent_school",
                self.cls_name,
            )
            self.check.check_type(
                teacher_id,
                int,
                "teacher_id",
                self.cls_name,
            )
            self.check.check_type(
                person,
                Person,
                "person",
                self.cls_name,
            )
            self.check.check_type(
                presenting_lessons,
                tuple,
                "presenting_lessons",
                self.cls_name,
                inner_type=Lesson,
            )

            # Initializations
            self.parent_school = parent_school
            self.teacher_id = teacher_id
            self.person = person
            self.presenting_lessons = [lesson for lesson in presenting_lessons]

        def __str__(self):
            return f'{self.person.gender.prefix} {self.person.last_name}'

    # endregion


# endregion
