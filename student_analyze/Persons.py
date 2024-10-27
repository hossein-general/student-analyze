
# region importing
# for abstractmethods
from abc import ABC, abstractmethod

# only for type hints:
from .GlobalAttributes import EducationGrade
from datetime import datetime

# endregion

# region BasePerson


class BasePerson(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

# endregion


# region Gender
# A Gender could be Male or Female
class Gender:
    _genders = []

    def __init__(self, name: str):
        self.name = name
        self.__class__._genders.append(self)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<Gender: "{self.name}">'

# endregion


# region Person
# GovernmentPerson shortened as GovPerson
# This class is a blueprint for person type
# Any organization that needs to validate a persons identification will chek that person's id with this class, and may retreive data about that person. (this connection can be seen in government web apps only gets the person id and filles other fields automatically like name, family, age, etc.)
# Each instance of this class is single person, containing information about that person. There will be a private variable within the class itself that acts as a container for all persons created
# UPDATE: GovPerson has been changed to Person
class Person(BasePerson):
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
        gender: Gender,
        birth_date: datetime,
        education_grade: EducationGrade,
        national_code: int = None,
    ):
        self.id = self.__class__.test
        self.gender = gender
        self.first_name = first_name
        self.last_name = last_name
        # Each person has an education grade as their education state
        # it has to be of type
        self.birth_date = birth_date
        self.education_grade = education_grade
        # setting a national code (this could be done automatically or by user)
        # TODO the current national code generator does not check for duplicate national codes. add a checking function for that in the future
        if national_code is not None:
            self.__national_code = national_code
        else:
            self.__national_code = self.__class__.get_national_code()
        # Adding the newly created person to the
        self.__class__.add_person(self)
        self._workinglog_list = []

    # region @prop
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

    # endregion

    # region @cls
    @classmethod
    def get_by_id(cls, person_id):
        return cls.__people[person_id]

    @classmethod
    def get_national_code(cls):
        cls.__last_nationalcode += 1
        return cls.__last_nationalcode

    # Generating an ip address for new instance
    # (maybe i should remove the class-properties as they are depricated)
    @classmethod
    @property
    def test(cls):
        cls.__id_pool += 1
        return cls.__id_pool

    # Adding a record using the person instance and an id
    @classmethod
    def add_person(cls, person):
        cls.__people[person.id] = person

    # endregion

    # region format

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f'<Person: "{self.fullname}">'

    # endregion
    
    # region nested classes
    # a region containing nested classes
    # these classes should be directly called from Person class
    # these classes are not accessible from base person
    # WorkingLog, EducationLog


    # region Working-L
    # A class that is kind of a table that contains records of places each person have been worked or is working in

    class WorkingLog:
        # Creating a new record for the table
        def __init__(
            self,
            parent_person,
            working_organization,
            contract_id,
        ):
            self.person = parent_person
            self.contract = contract_id
            # The id of that organization
            self.working_organization = working_organization

        # An instance method that will tell whether the record status is active or inactive
        # it will check the organizations contractid and checks if the termination_date of that contract is filled with a value or not
        @property
        def status(self):
            return (
                (True, "active")
                if self.working_organization.getcontract(
                    self.contract_id
                ).termination_date
                == None
                else (False, "inactive")
            )

        # Returns the instance that is representing the current working organization
        # that instance should not have an end_time and there could be multiple instances that will be retruned as a list
        @classmethod
        def current_organization(cls):
            pass

    # endregion

    # region Education-L
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

    def add_workinglog(
        self,
        working_organization,
        contract_id,
    ):
        new_workinglog = self.__class__.WorkingLog(
            self,
            working_organization,
            contract_id,
        )
        self._workinglog_list.append(new_workinglog)


# endregion
