
# SchoolTypes will define type of schools
# e.g. Primary School, High School 1st Term, High School 2nd Term, University
class SchoolType:
    __slots__ = ["tpe_name"]
    def __init__(self, type_name):
        self.type_name = type_name
        # TODO Creating variables that will be initialized when an instance is created, and will manage School realations



class EducationGrade:
    def __init__(self, name):
        self.name = name
        

# EducationGroups are created to define different grous in differen school types
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




