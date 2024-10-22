# This module is used to store functions that are sued to:
#   initialize data within the application
#   generate fake data fpr classes/tables

from datetime import datetime
import random

from student_analyze import (
    EducationState,
    Person,
)


def init_educationstates():
    pass


def init_data():
    # EducationStates
    es = {}
    es["ps"] = EducationState("Primary School")
    es["hs1"] = EducationState("High School 1st")
    es["hs2"] = EducationState("High School 2nd")
    es["u"] = EducationState("University")

    # EducationGrades
    eg = {}
    eg["1st"] = es["ps"].add_grade("1st grade")
    eg["2nd"] = es["ps"].add_grade("2nd grade")
    eg["3rd"] = es["ps"].add_grade("3rd grade")
    eg["4th"] = es["ps"].add_grade("4th grade")
    eg["5th"] = es["ps"].add_grade("5th grade")
    eg["6th"] = es["ps"].add_grade("6th grade")

    eg["7th"] = es["hs1"].add_grade("7th grade")
    eg["8th"] = es["hs1"].add_grade("8th grade")
    eg["9th"] = es["hs1"].add_grade("9th grade")

    eg["10th"] = es["hs2"].add_grade("10th grade")
    eg["11th"] = es["hs2"].add_grade("11th grade")
    eg["12th"] = es["hs2"].add_grade("12th grade")

    eg["bachelor"] = es["u"].add_grade("Bachelor")
    eg["master"] = es["u"].add_grade("Master")
    eg["phd"] = es["u"].add_grade("Ph.D")

    # Genders
    gender = {}
    gender["male"] = Person.Gender("male")
    gender["female"] = Person.Gender("female")

    return es, eg, gender


# TODO adding the ability to access eg, es, person, gender and etc through the class
def fake_person(eg, gender, count):
    # person_temp = Person("Hossein", "Ramezani", datetime(2020, 5, 17), eg["10th"])

    # person_temp = Person("Mohammadmahdi", "Ramezani", datetime(2023, 3, 11), eg["7th"])

    for count in range(count):
        first_name_list = (
            "hossein",
            "mohammad mahdi",
            "reza",
            "maryam",
            "samira",
            "fereshteh",
            "eisa",
            "peyman",
            "mansore",
            "elham",
            "hasan",
            "ali",
            "said",
            "arash",
            "hoorieh",
        )
        last_name_list = (
            "mohammadi",
            "ramezani",
            "mamani",
            "bonab",
            "chakaneh",
            "rajabalian",
            "eisapoor",
            "nobakht",
            "zareiian_zadeh",
            "seyedrazi",
            "dalvand",
            "mohammadian",
            "mohammadian far",
            "mohammad zadeh",
            "pirhadi",
            "enayati",
            "nikravesh",
        )

        first_name_list = tuple(name.capitalize() for name in first_name_list)
        last_name_list = tuple(name.capitalize() for name in last_name_list)

        temp_first_name = random.choice(first_name_list)
        temp_last_name = random.choice(last_name_list)
        temp_gender = random.choice(tuple(gender.values()))
        # TODO making the birth_date attribute a random date within a range
        temp_birth_date = datetime(2001, 9, 11)
        temp_education_grade = random.choice(tuple(eg.values()))

        yield Person(
            temp_first_name,
            temp_last_name,
            temp_gender,
            temp_birth_date,
            temp_education_grade,
        )


def main():
    # --Only for testing purposes--
    es, eg, gender = init_data()
    person_gen = fake_person(eg, gender, 3)
    for person in person_gen:
        # print(Person.get_id)
        order = (
            person.id,
            person.first_name,
            person.last_name,
            person.gender.name,
            # person.birth_date,
            person.education_grade.name,
            person.national_code,
        )
        print(
            # "{0:^10} {1:<10} {2:>10} \n".format('test', 'test2', 'test3'),
            "{:<5}{:^16}{:^16}{:^10}{:^15}{:^7}".format(*order)
            # "{:^10}{:^10}".format(person.id, person)
        )


if __name__ == "__main__":
    main()
