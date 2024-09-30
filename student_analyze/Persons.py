from abc import ABC, abstractmethod  # Not yet sure how to make the class


# GovernmentPerson shortened as GovPerson
class GovPerson:
    __people = dict()
    __last_nationalcode = 1000

    def __init__(self, first_name, last_name, education_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.education_grade = education_grade
        self.educational_organizations = set()
        self.working_organizations = set()
        self.id = self.__class__.get_id
        self.__class__.people.add(self)

    def add_organization(self, organization_type, organization):
        match organization_type:
            case "educational":
                self.educational_organizations.add(organization)
            case "working":
                self.working_organizations.add(organization)
            case _:
                # TODO testing if i could use the wild card (_) to output the organization_type value along with ValueError message
                raise ValueError("non-defined organization type to add for student")

    @classmethod
    def get_by_id(cls, person_id):
        return cls.__people[person_id]

    @property
    @classmethod
    def national_code(cls):
        cls.__last_nationalcode += 1
        return cls.__last_nationalcode


# # OLD STYLE PERSON MODULE ----------------------------------
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
        education_grade,
        student_id,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        # TODO adding some getter and setters to the attributes
        self.parent_school = parent_school
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
