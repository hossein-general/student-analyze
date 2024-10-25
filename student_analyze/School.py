# This module containes School related classes
# These Classes only have meaning in the context of schools
# The School class within this module inharites from the Organizations class within the Organizations module

from .Organization import Organization

# region School
# School class
class School(Organization):
    # last_classroom
    def __init__(self, name, education_state):
        self.name = name
        self.education_state = education_state
        self.classrooms = dict()
        self.students = dict()
        self.teachers = dict()
        self.classgroups = dict()
        self.last_classroom_id = 100
        self.last_student_id = 200
        self.last_teacher_id = 300
        self.last_classgroup_id = 400

    # Create and adding ClassRooms to the school
    def add_classroom(self, *classroom_names):
        # TODO Getting classroom_name
        for item in classroom_names:
            # Getting an id for the new classroom
            classroom_id = self.get_id("classroom")
            # Creating an instance of ClassRoom
            new_classroom = ClassRoom(self, classroom_id, item)
            # Assigning the newly created classroom to classrooms dict
            self.classrooms[classroom_id] = new_classroom

    # Creating a ClassGroup for the school
    # most of the parameters should be removed and be placed within the function to get
    """I can think of two different ways to get the necessary inputs from user
    one is to get them one by one from user while the add method is open, 
    and the other is to first fill the requirements within a form and at the end sending them to tha add method
    im not sure if there is any risk of problems in first method
    this idea applies to many other parts of my program, and maybe ill change my structure in the future"""

    def add_classgroup(
        self,
        educationgrade,
        student_ids_list,
        teacher_ids_list,
        lessons_ids_list,
        default_classroom_id,
    ):
        # TODO Getting educationgrade
        # TODO Getting student_list
        # TODO Getting teacher_list
        # Getting an id for the new classgroup
        classgroup_id = self.get_id("classgroup")
        # Creating an instance of ClassGroup
        new_classgroup = ClassGroup(
            self,
            educationgrade,
            student_ids_list,
            teacher_ids_list,
            lessons_ids_list,
            default_classroom_id,
            classgroup_id,
        )
        # Assigning the newly created classgroup to the classgroups dict
        self.classgroups[classgroup_id] = new_classgroup

    # Creating new students and assigning them to the school
    def add_student(
        self,
        student_first_name,
        student_last_name,
        education_grade,
    ):
        # Getting an id for the student from get_id
        student_id = self.get_id("student")
        # Calling the Student class to create an instance of Student
        new_student = Student(
            self,
            first_name=student_first_name,
            last_name=student_last_name,
            education_grade=education_grade,
            id=student_id,
        )
        # Adding the newly created student to students dict
        self.students[student_id] = new_student

    # This class will manage ids for each id-able item in the school
    # e.g. ClassRooms (classroom), Teachers (teacher), Students (student), etc.
    # This management happens by using a counter variable and adding one to it each time an id is assigned
    # each entity has its own id counter
    # This function is used within the class, where ever a new entity creates
    def get_id(self, entity: str):
        match entity:
            case "classroom":
                self.last_classroom_id += 1
                return self.last_classroom_id

            case "student":
                self.last_student_id += 1
                return self.last_student_id

            case "classgroup":
                self.last_classgroup_id += 1
                return self.last_classgroup_id

            case _:
                raise ValueError("non-defined entity name for id assignment")

    def __str__(self):
        return self.name

# endregion


# region C-Room
# Classroom class which are called by School class instances. they are used as the place for holding class sessions
class ClassRoom:
    __slots__ = ["parent_school", "id", "name"]

    def __init__(self, parent_school, id, name):
        self.id = id
        self.parent_school = parent_school
        self.name = name

    def __str__(self):
        return f"[{self.id}: {self.name}]"

# endregion


# region C-Group
# Class Group class. its used to bind teachers, students, lessons, classrooms and adding schedule for each
# I dont think if there would ever be a need to name a ClassGroup as its not user readable
class ClassGroup:
    def __init__(
        self,
        parent_school,
        educationgrade,
        student_list: set,
        teacher_list: set,
        lessons_list: set,
        default_classroom,
        id,
    ):
        self.parent_school = parent_school
        self.educationgrade = educationgrade
        self.students = student_list
        self.teacher_list = teacher_list
        self.lessons_list = lessons_list
        self.classschedules = set()
        self.default_classroom = default_classroom

    # Creating a class schedule
    def add_classschedule(self, classschedule_id, student_list, teacher, lesson):
        # TODO Getting classschedule_name and removing from parameters
        # TODO Getting students_list and removing from parameters
        # TODO Getting teacher and removing from parameters
        # TODO Getting lesson and removing from parameters
        new_classschedule = ClassSchedule(
            self, classschedule_id, student_list, teacher, lesson
        )
        self.classschedules.add(new_classschedule)

    def __str__(self):
        return self.id

# endregion

# region C-Schedule
# This class shows which of the ClassGroup teachers is assigend and what lesson is he presenting (as a sible ClassGroup could hold many teachers and lessons at the same time)
# In most cases the ClassSchedule instances are named by the lesson presenting within them, and sometimes combined with an id
# e.g. "Riazi-1 20341", "Arabi", ...
class ClassSchedule:
    def __init__(self, parent_classgroup, id, student_list, teacher, lesson):
        self.id = id
        self.student_list = student_list
        self.teacher = teacher
        self.lesson = lesson
        self.classsessions = set()

    def add_classsession(self, start_session, end_session, student_list, teacher):
        # TODO Getting start_session and removing from parameters
        # TODO Getting end_session and removing from parameters
        # TODO Inhariting teacher
        # TODO Inhariting student_list
        # TODO Inhariting lesson
        new_classsession = ClassSession(
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