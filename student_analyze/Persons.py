from abc import ABC, abstractmethod  # Not yet sure how to make the class
from .GlobalAttributes import EducationGrade
from datetime import datetime


# GovernmentPerson shortened as GovPerson
# This class is a blueprint for person type
# Any organization that needs to validate a persons identification will chek that person's id with this class, and may retreive data about that person. (this connection can be seen in government web apps only gets the person id and filles other fields automatically like name, family, age, etc.)
# Each instance of this class is single person, containing information about that person. There will be a private variable within the class itself that acts as a container for all persons created
# UPDATE: GovPerson has been changed to Person
class Person:
    # A dictionary containing all people
    __people = dict()
    __id_pool = 0
    __last_nationalcode = 1000

    # TODO making the national_code a string (right now its an integer to prevent complecation)
    # TODO write typing for each parameter (e.g. parameter: str)
    def __init__(
        self,
        first_name: str,
        last_name: str,
        birth_date: datetime,
        education_grade: EducationGrade,
        national_code: int = None,
    ):
        self.first_name = first_name
        self.last_name = last_name
        # Each person has an education grade as their education state
        # it has to be of type
        self.birth_date = birth_date
        self.education_grade = education_grade
        # setting a national code (this could be done automatically or by user)
        if national_code is not None:
            self.__national_code = national_code
        else:
            self.__national_code = self.__class__.get_national_code()
        # setting this instance's WorkingLog.person so i can use it to know whose WorkingLog is this class for
        self.WorkingLog._person = self
        self.__class__.add_person(self)
        self._workinglog_list = []

    # region WorkingLog Class
    # A class that is kind of a table that contains records of places each person have been worked or is working in
    class Contract:
        def __init__(self) -> None:
            # the execuation date of contract
            self.conclusion_date
            # when the contract ends by reaching its deadline
            # expiration_date and termination_date are Usually(!) the same
            # It referes to the "initial" date, and it could be not the same as termination_date in two cases:
            #   Automatic Renewal: If a contract has an automatic renewal clause, the expiration date might refer to the end of the initial term, while the termination date would be the actual date when the contract is formally terminated (which could be after a renewal period)
            #   Early Termination: If a contract allows for early termination under certain conditions, the termination date would be the date when one party officially notifies the other of their intent to terminate, while the expiration date might still refer to the end of the original term.
            self.expiration_date
            # when the contract ends
            self.termination_date

    class WorkingLog:
        # Creating a new record for the table
        def __init__(
            self,
            parent_person,
            start_contract_date,
            original_end_contract_date,
            working_organization,
            job_position,
            base_salary,
        ):
            self.person = parent_person
            self.start_contract_date = start_contract_date
            # an end_time would not be empty as each contract has an end_time by default
            self.original_end_contract_date = start_contract_date
            # in case the person leaves his work or fired by organization
            self.contract_expiration = original_end_contract_date
            # like beeing fired or leaving the work or etc.
            # could be {Expiration, Termination, or Resignation}
            self.end_of_employment_relationship_reason = None
            # The id of that organization
            self.working_organization = working_organization
            self.job_position = job_position
            self.base_salary = base_salary
            # adding the newly created working instance to the working history (which is a list of where the person worked in his life)
            self.__class__._history_list.append(self)

        # region Instance Method/Properties
        # An instance method that could be called to set end_time for that instance. (This is an emergency method for cases like "being fired" as each instance would usually end by the deadline time)
        def set_end(self, end_datetime, reason):
            self.end_contract_datetime = end_datetime
            self.end_contract_reason = reason

        # An instance method that will tell whether the record status is active or inactive
        @property
        def status(self):
            pass

        # endregion

        # region Class Method/Properties
        # Returns the instance that is representing the current working organization
        # that instance should not have an end_time and there could be multiple instances that will be retruned as a list
        @classmethod
        def current_organization(cls):
            pass

        # endregion

    # endregion

    # region EducationLog Class
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

    # endregion

    # region Instancemethods/Properties
    def add_workinglog(
        self,
        start_contract_date,
        original_end_contract_date,
        working_organization,
        job_position,
        base_salary,
    ):
        new_workinglog = self.WorkingLog(
            self,
            start_contract_date,
            original_end_contract_date,
            working_organization,
            job_position,
            base_salary,
        )
        self._workinglog_list.append(new_workinglog)

    @property
    def age(self):
        # TODO calculating age
        pass

    # Returning national code for that person
    @property
    def national_code(self):
        return self.__national_code

    # Returning full name
    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

    # endregion

    # region Classmethods/Properties
    @classmethod
    def get_by_id(cls, person_id):
        return cls.__people[person_id]

    @classmethod
    def get_national_code(cls):
        cls.__last_nationalcode += 1
        return cls.__last_nationalcode

    # Generating an ip address for new instance
    # (maybe i should remove the class-properties as they are depricated)
    @property
    @classmethod
    def id(cls):
        cls.__id_pool += 1
        return cls.__id_pool

    # Adding a record using the person instance and an id
    @classmethod
    def add_person(cls, person):
        cls.__people[cls.id] = person

    # endregion


# # OLD STYLE PERSON MODULE ----------------------------------
# # OLD STYLE STUDENT/TEACHER CLASSES
# class BasePerson(ABC):
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         print("the main")

#     @abstractmethod
#     def __str__(self):
#         pass

# class Student(BasePerson):
#     def __init__(
#         self,
#         parent_school,
#         education_grade,
#         student_id,
#         *args,
#         **kwargs,
#     ):
#         super().__init__(*args, **kwargs)
#         # TODO adding some getter and setters to the attributes
#         self.parent_school = parent_school
#         self.education_grade = education_grade
#         self.id = student_id

#     def __str__(self):
#         return " ".join((self.first_name, self.last_name))


# class Teacher(BasePerson):
#     def __init__(self, parent_school, name_prefix, teacher_id, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.name_prefix = name_prefix
#         self.parent_school = parent_school
#         self.id = teacher_id

#     def __str__(self):
#         return f"{self.name_prefix} {self.first_name} {self.last_name}"
