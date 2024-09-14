# School class
class School:

    # Im not sure if i should add __shlots__ in School class, as it has many temporarily variables
    # __sltos__ = ["school_stage", "classrooms", "new_classroom", "classrooms"]
    def __init__(self, name, school_stage):
        self.name = name
        self.school_stage = school_stage
        self.classrooms = set()
        self.classgroups = set()
        self.last_classroom_id = 0

    # Create and adding ClassRooms to the school
    def add_classroom(self, *classroom_names):
        # TODO Getting classroom_name
        for item in classroom_names
            id = School.last_classroom
            new_classroom = ClassRoom(self, id, item)
            self.classrooms.add(new_classroom)

    def get_id(self, entity: str = "cr"):
        match entity:
            case "cr":
                self.last_classroom_id += 1
                return self.last_classroom_id
            case _:
                # TODO At this point there should be an error raise
                return None

    # Creating a ClassGroup for the school
    # most of the parameters should be removed and be placed within the function to get
    """I can think of two different ways to get the necessary inputs from user
    one is to get them one by one from user while the add method is open, 
    and the other is to first fill the requirements within a form and at the end sending them to tha add method
    im not sure if there is any risk of problems in first method
    this idea applies to many other parts of my program, and maybe ill change my structure in the future"""

    def add_classgroup(self, educationgrade, student_list, teacher_list):
        # TODO Getting educationgrade
        # TODO Getting student_list
        # TODO Getting teacher_list
        new_classgroup = ClassGroup(self, educationgrade, student_list, teacher_list)
        self.classgroups.add(new_classgroup)

    def __str__():
        return "no info"


# Classroom class which are called by School class instances. they are used as the place for holding class sessions
class ClassRoom:
    __slots__ = ["parent_school", "id", "name"]

    def __init__(self, parent_school, id, name):
        self.id = id
        self.parent_school = parent_school
        self.name = name


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
    ):
        self.parent_school = parent_school
        self.educationgrade = educationgrade
        self.students = student_list
        self.teacher_list = teacher_list
        self.lessons_list = lessons_list
        self.classschedules = set()
        self.default_classroom = default_classroom

    # Creating a class schedule
    def add_classschedule(self, classschedule_name, student_list, teacher, lesson):
        # TODO Getting classschedule_name and removing from parameters
        # TODO Getting students_list and removing from parameters
        # TODO Getting teacher and removing from parameters
        # TODO Getting lesson and removing from parameters
        new_classschedule = ClassSchedule(
            self, classschedule_name, student_list, teacher, lesson
        )
        self.classschedules.add(new_classschedule)


# This class shows which of the ClassGroup teachers is assigend and what lesson is he presenting (as a sible ClassGroup could hold many teachers and lessons at the same time)
# In most cases the ClassSchedule instances are named by the lesson presenting within them, and sometimes combined with and an id
# e.g. "Riazi-1 20341", "Arabi", ...
class ClassSchedule:
    def __init__(self, parent_classgroup, name, student_list, teacher, lesson):
        self.parent_classgroup = parent_classgroup
        self.name = name
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


# TODO The ClassSession class should be inherited from the ClassSchedule class so it will be containing infrmations like students list, teacher, lesson and etc by default
# ClassSessions are instances that contain classSchedule information plus date & time information and is used for a single session
# This class can be used for checking presence and absence of each studing within each session
# Each ClassSession should only have one teacher
class ClassSession:
    def __init__(
        self,
        parent_classsession,
        start_session,
        end_session,
        student_list,
        teacher,
        lesson,
    ):
        self.parent_classsession = parent_classsession
        self.start_session = start_session
        self.end_session = end_session
        self.student_list = student_list
        self.teacher = teacher
        self.lesson = lesson
