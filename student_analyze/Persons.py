from abc import ABC, abstractmethod  # Not yet sure how to make the class


class BasePerson(ABC):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        print("the main")

    @abstractmethod
    def __str__(self):
        pass


class Student(BasePerson):
    def __init__(
        self,
        parent_school,
        education_state,
        education_grade,
        student_id,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        # TODO adding some getter and setters to the attributes
        self.parent_school = parent_school
        self.education_state = education_state
        self.education_grade = education_grade
        self.id = student_id

    def __str__(self):
        return " ".join((self.first_name, self.last_name))


class Teacher(BasePerson):
    def __init__(self, parent_school, name_prefix, teacher_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name_prefix = name_prefix
        self.parent_school = parent_school
        self.id = teacher_id

    def __str__(self):
        return f"{self.name_prefix} {self.first_name} {self.last_name}"
