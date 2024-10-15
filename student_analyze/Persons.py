from abc import ABC, abstractmethod  # Not yet sure how to make the class


# GovernmentPerson shortened as GovPerson
# This class is a blueprint for person type
# Any organization that needs to validate a persons identification will chek that person's id with this class, and may retreive data about that person. (this connection can be seen in government web apps only gets the person id and filles other fields automatically like name, family, age, etc.)
# Each instance of this class is single person, containing information about that person. There will be a private variable within the class itself that acts as a container for all persons created
class GovPerson:
    __people = dict()
    __id_pool = 0
    __last_nationalcode = 1000

    # TODO making the national_code a string (right now its an integer to prevent complecation)
    def __init__(self, first_name, last_name, education_grade, national_code: int = None):
        self.first_name = first_name
        self.last_name = last_name
        # Each person has an education grade as their education state
        self.education_grade = education_grade
        # setting a national code (this could be done automatically or by user)
        if national_code is not None:
            self.national_code = national_code
        else:
            self.national_code = self.__class__.national_code
        # setting this instance's WorkingLog.person so i can use it to know whose WorkingLog is this class for
        self.WorkingLog._person = self
        self.__class__.add_person(self)

    # A class that is kind of a table that contains records of places each person have been worked or is working in
    class WorkingLog:
        _person = None
        _history_list = []

        # Creating a new record for the table
        def __init__(self, start_contract_datetime, original_end_contract_datetime, working_organization, position, base_salary):
            self.start_contract_datetime = start_contract_datetime
            # an end_time would not be empty as each contract has an end_time by default
            self.original_end_contract_datetime = start_contract_datetime
            # in case the person leaves his work or fired by organization
            self.end_contract_datetime = original_end_contract_datetime
            # like beeing fired or leaving the work or etc.
            self.end_contract_reason = None
            # The id of that organization
            self.working_organization = working_organization
            self.position = position
            self.base_salary = base_salary
            # adding the newly created working instance to the working history (which is a list of where the person worked in his life)
            self.__class__._history_list.append(self)

        # An instance method that could be called to set end_time for that instance. (This is an emergency method for cases like "being fired" as each instance would usually end by the deadline time)
        def set_end(self, end_datetime, reason):
            self.end_contract_datetime = end_datetime
            self.end_contract_reason = reason

        # An instance method that will tell whether the record status is active or inactive
        @property
        def status(self):
            pass

        # Returns the instance that is representing the current working organization
        # that instance should not have an end_time and there could be multiple instances that will be retruned as a list
        @classmethod
        def current_organization(cls):
            pass
        
        # returns a list containing the history of where ever that person have been working in
        @property
        @classmethod
        def history_list(cls):
            return cls._history_list

    # A class that is kind of a table that contains records of places each person have been educated or is currently educating in
    class EducationLog:
        # Creating a new record for the table
        def __init__(self):
            self.term
            self.education_grade = None
            self.education_organization

        @classmethod
        def current_organization(cls):
            pass

    @classmethod
    def get_by_id(cls, person_id):
        return cls.__people[person_id]

    @property
    @classmethod
    def national_code(cls):
        cls.__last_nationalcode += 1
        return cls.__last_nationalcode

    @property
    @classmethod
    def id(cls):
        cls.__id_pool += 1
        return cls.__id_pool

    # adding a record using the person instance and an id
    def add_person(cls, person):
        cls.__people[cls.id] = person


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
