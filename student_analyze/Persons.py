
# region importing
# for abstractmethods
from abc import ABC, abstractmethod

# for validations 
from .Validations import Validator

# only for type hints:
from datetime import datetime
from .GlobalAttributes import (
    EducationGrade,
    EducationGroup
)

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
    cls_name = 'Gender'

    # Validator object
    check = Validator()

    def __init__(self, name: str):
        # Validations
        self.check.check_type(
            name,
            str,
            "name",
            creating_class=self.cls_name,
        )

        # Initializations
        self.name = name
        self.__class__._genders.append(self)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<Gender: "{self.name}">'

# endregion

# region id_generator
# The generator function at this point is somuch like a range() generator
# the reason of using a different generator is to customize it in the future


def id_generator(start_id):
    current_id = start_id
    while True:
        yield current_id
        current_id += 1

# endregion


# region Person
# GovernmentPerson shortened as GovPerson
# This class is a blueprint for person type
# Any organization that needs to validate a persons identification will chek that person's id with this class, and may retreive data about that person. (this connection can be seen in government web apps only gets the person id and filles other fields automatically like name, family, age, etc.)
# Each instance of this class is single person, containing information about that person. There will be a private variable within the class itself that acts as a container for all persons created
# UPDATE: GovPerson has been changed to Person
# TODO adding super().__init__() and moving some attributes to the BasePerson class
class Person(BasePerson):
    # A dictionary containing all people
    __people = dict()
    __id = id_generator(1)
    __national_code = id_generator(1001)
    cls_name = 'Person'

    # Validator object
    check = Validator()

    # TODO making the national_code a string (right now its an integer to prevent complecation)
    # TODO write typing for each parameter (e.g. parameter: str)
    def __init__(
        self,
        first_name: str,
        last_name: str,
        gender: Gender,
        birth_date: datetime,
        national_code: int = None,
    ):
        # Validations
        self.check.check_type(
            first_name,
            str,
            "first_name",
            creating_class=self.cls_name,
        )
        self.check.check_type(
            last_name,
            str,
            "last_name",
            creating_class=self.cls_name,
        )
        self.check.check_type(
            gender,
            Gender,
            "gender",
            creating_class=self.cls_name,
        )
        self.check.check_type(
            birth_date,
            datetime,
            "birth_date",
            creating_class=self.cls_name,
        )
        self.check.check_type(
            national_code,
            (int, type(None)),
            "national_code",
            creating_class=self.cls_name,
        )

        # Initializations
        self.id = next(self.__class__.__id)
        self.gender = gender
        self.first_name = first_name
        self.last_name = last_name
        # Each person has an education grade as their education state
        # it has to be of type
        self.birth_date = birth_date
        # setting a national code (this could be done automatically or by user)
        # TODO the current national code generator does not check for duplicate national codes. add a checking function for that in the future
        if national_code is not None:
            self.__national_code = national_code
        else:
            self.__national_code = next(self.__class__.__national_code)
        # Adding the newly created person to the
        self.__class__.add_person(self)
        self._professional_record_list = []

    # region methods
    
    # TODO adding Validations
    def add_professional_record(
        self,
        working_organization,
        contract_id,
    ):
        new_professional_record = self.__class__.ProfessionalRecords(
            self,
            working_organization,
            contract_id,
        )
        self._professional_record_list.append(new_professional_record)

    # endregion

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
    # ProfessionalRecords, EducationLog

    # region Professional-R
    # A class that is kind of a table that contains records of places each person have been worked or is working in

    # TODO adding validations
    class ProfessionalRecords:
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

    # region Academic-R
    # A class that is kind of a table that contains records of places each person have been educated or is currently educating in

    # TODO adding validations
    class AcademicRecords:
        # Creating a new record for the table
        def __init__(self):
            self.term
            self.education_grade = None
            self.education_organization

        @classmethod
        def current_organization(cls):
            pass


# endregion
