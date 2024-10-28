# This module is used to store functions that are sued to:
#   initialize data within the application
#   generate fake data fpr classes/tables

from datetime import datetime
import random

from student_analyze import (
    EducationState,
    Person,
    Gender,
    School,
)


# region Init
def init_data(data):
    # region ES
    # EducationStates
    data.es.item["ps"] = EducationState("Primary School")
    data.es.item["hs1"] = EducationState("High School 1st")
    data.es.item["hs2"] = EducationState("High School 2nd")
    data.es.item["u"] = EducationState("University")
    # endregion

    # region EGd
    # EducationGrades
    data.egd.item["1st"] = data.es.item["ps"].add_grade("1st grade")
    data.egd.item["2nd"] = data.es.item["ps"].add_grade("2nd grade")
    data.egd.item["3rd"] = data.es.item["ps"].add_grade("3rd grade")
    data.egd.item["4th"] = data.es.item["ps"].add_grade("4th grade")
    data.egd.item["5th"] = data.es.item["ps"].add_grade("5th grade")
    data.egd.item["6th"] = data.es.item["ps"].add_grade("6th grade")

    data.egd.item["7th"] = data.es.item["hs1"].add_grade("7th grade")
    data.egd.item["8th"] = data.es.item["hs1"].add_grade("8th grade")
    data.egd.item["9th"] = data.es.item["hs1"].add_grade("9th grade")

    data.egd.item["10th"] = data.es.item["hs2"].add_grade("10th grade")
    data.egd.item["11th"] = data.es.item["hs2"].add_grade("11th grade")
    data.egd.item["12th"] = data.es.item["hs2"].add_grade("12th grade")

    data.egd.item["bachelor"] = data.es.item["u"].add_grade("Bachelor")
    data.egd.item["master"] = data.es.item["u"].add_grade("Master")
    data.egd.item["phd"] = data.es.item["u"].add_grade("Ph.D")
    # endregion

    # region EGp
    # EducationGroups
    # Primary School Gropus (1)
    data.egp.item["ps-general"] = data.es.item["ps"].add_group(
        "Primary School - General"
    )

    # High School 1st Groups (1)
    data.egp.item["hs1-general"] = data.es.item["hs1"].add_group(
        "High School 1st - General"
    )

    # High School 2nd Gropus (7)
    data.egp.item["hs2-general"] = data.es.item["hs2"].add_group(
        "High School 2st - General", False
    )
    data.egp.item["hs2-riazi"] = data.es.item["hs2"].add_group(
        "High School 2st - Riazi Fizik", data.egp.item["hs2-general"]
    )
    data.egp.item["hs2-tajrobi"] = data.es.item["hs2"].add_group(
        "High School 2st - Oloom Tajrobi", data.egp.item["hs2-general"]
    )
    data.egp.item["hs2-ensani"] = data.es.item["hs2"].add_group(
        "High School 2st - Oloom Ensani", data.egp.item["hs2-general"]
    )
    data.egp.item["hs2-zaban"] = data.es.item["hs2"].add_group(
        "High School 2st - Zaban haye Khareje", data.egp.item["hs2-general"]
    )
    data.egp.item["hs2-honar"] = data.es.item["hs2"].add_group(
        "High School 2st - Honar", data.egp.item["hs2-general"]
    )
    data.egp.item["hs2-fani"] = data.es.item["hs2"].add_group(
        "High School 2st - Fani Herfei", data.egp.item["hs2-general"]
    )

    # University Groups (??)
    data.egp.item["u-general"] = data.es.item["u"].add_group(
        "University - General", False
    )
    data.egp.item["u-mohandesi-computer"] = data.es.item["u"].add_group(
        "University - Mohandesi Computer", data.egp.item["u-general"]
    )
    data.egp.item["u-oloom-computer"] = data.es.item["u"].add_group(
        "University - Oloom Computer", data.egp.item["u-general"]
    )
    data.egp.item["u-mohandesi-bargh"] = data.es.item["u"].add_group(
        "University - Mohandesi Bargh", data.egp.item["u-general"]
    )
    # endregion

    # region Lessons
    # Lessons
    data.lesson.item["ps-farsi-aval"] = data.egp.item["ps-general"].add_lesson(
        "Farsi Aval",
        data.egd.item["1st"],
    )

    data.lesson.item["ps-riazi-dovom"] = data.egp.item["ps-general"].add_lesson(
        "Riazi Dovom",
        data.egd.item["1st"],
    )

    data.lesson.item["hs1-hendese-1"] = data.egp.item["hs1-general"].add_lesson(
        "Hendese 1",
        data.egd.item["7th"],
    )

    data.lesson.item["hs1-riazi-2"] = data.egp.item["hs1-general"].add_lesson(
        "Riazi Hashtom",
        data.egd.item["8th"],
    )

    # endregion

    # region Gender
    # Genders
    data.gender.item["male"] = Gender("male")
    data.gender.item["female"] = Gender("female")
    # endregion

    # region School
    data.school.item["hesaraki"] = School(
        "Dabestan Shahid Abas Hesaraki", data.es.item["ps"], data.egp.item["ps-general"]
    )

    data.school.item["alameh"] = School(
        "Dabirestan Alameh Tabatabai",
        [data.es.item["hs1"], data.es.item["hs2"]],
        [
            data.egp.item["hs1-general"],
            data.egp.item["hs2-general"],
            data.egp.item["hs2-riazi"],
            data.egp.item["hs2-tajrobi"],
        ],
    )

    data.school.item["payamenoor"] = School(
        "Daneshgah Payame Noor",
        data.es.item["u"],
        [
            data.egp.item["u-general"],
            data.egp.item["u-mohandesi-computer"],
            data.egp.item["u-oloom-computer"],
            data.egp.item["u-mohandesi-bargh"],
        ],
    )

    # endregion

    # region C-Room

    data.croom.item["1-1"] = data.school.item["hesaraki"].add_classrooms("Aval 1-1")[0]
    data.croom.item["1-2"] = data.school.item["hesaraki"].add_classrooms("Aval 1-2")[0]
    data.croom.item["1-3"] = data.school.item["hesaraki"].add_classrooms("Aval 1-3")[0]
    data.croom.item["2-1"] = data.school.item["hesaraki"].add_classrooms("Dovom 2-1")[0]
    data.croom.item["2-2"] = data.school.item["hesaraki"].add_classrooms("Dovom 2-2")[0]
    data.croom.item["2-3"] = data.school.item["hesaraki"].add_classrooms("Dovom 2-3")[0]
    data.croom.item["3-1"] = data.school.item["hesaraki"].add_classrooms("Sevom 3-1")[0]
    data.croom.item["3-2"] = data.school.item["hesaraki"].add_classrooms("Sevom 3-2")[0]
    data.croom.item["3-3"] = data.school.item["hesaraki"].add_classrooms("Sevom 3-3")[0]
    data.croom.item["4-1"] = data.school.item["hesaraki"].add_classrooms(
        "Chaharom 4-1"
    )[0]
    data.croom.item["4-2"] = data.school.item["hesaraki"].add_classrooms(
        "Chaharom 4-2"
    )[0]
    data.croom.item["4-3"] = data.school.item["hesaraki"].add_classrooms(
        "Chaharom 4-3"
    )[0]
    data.croom.item["5-1"] = data.school.item["hesaraki"].add_classrooms("Panjom 5-1")[
        0
    ]
    data.croom.item["5-2"] = data.school.item["hesaraki"].add_classrooms("Panjom 5-2")[
        0
    ]
    data.croom.item["5-3"] = data.school.item["hesaraki"].add_classrooms("Panjom 5-3")[
        0
    ]
    data.croom.item["6-1"] = data.school.item["hesaraki"].add_classrooms("Shishom 6-1")[
        0
    ]
    data.croom.item["6-2"] = data.school.item["hesaraki"].add_classrooms("Shishom 6-2")[
        0
    ]
    data.croom.item["6-3"] = data.school.item["hesaraki"].add_classrooms("Shishom 6-3")[
        0
    ]

    data.croom.item["kharazmi 1"] = data.school.item["alameh"].add_classrooms(
        "Haftom Kharazmi 1"
    )[0]
    data.croom.item["kharazmi 2"] = data.school.item["alameh"].add_classrooms(
        "Haftom Kharazmi 2"
    )[0]
    data.croom.item["kharazmi 3"] = data.school.item["alameh"].add_classrooms(
        "Haftom Kharazmi 3"
    )[0]

    rng = range(200, 210)
    temp_croom_names = map(lambda i: str(i), rng)
    temp_croom_objects = data.school.item["payamenoor"].add_classrooms(
        *rng, starting_id=200
    )
    data.croom.item.update(zip(temp_croom_names, temp_croom_objects))

    # endregion

    # Adding Persons
    person_gen = fake_person(data, 20)
    for new_person in person_gen:
        data.person.item[new_person.id] = new_person

    # region Student
    # Students
    data.student.item["ps-1"] = data.school.item["hesaraki"].add_student(
        data.person.item[1], data.egd.item["1st"], data.egp.item["ps-general"]
    )

    data.student.item["ps-2"] = data.school.item["hesaraki"].add_student(
        data.person.item[2], data.egd.item["5th"], data.egp.item["ps-general"]
    )

    data.student.item["hs1-1"] = data.school.item["alameh"].add_student(
        data.person.item[3], data.egd.item["7th"], data.egp.item["hs1-general"]
    )

    data.student.item["hs1-2"] = data.school.item["alameh"].add_student(
        data.person.item[4], data.egd.item["9th"], data.egp.item["hs1-general"]
    )

    data.student.item["hs2-1"] = data.school.item["alameh"].add_student(
        data.person.item[5], data.egd.item["11th"], data.egp.item["hs2-riazi"]
    )

    data.student.item["hs2-2"] = data.school.item["alameh"].add_student(
        data.person.item[6], data.egd.item["12th"], data.egp.item["hs2-tajrobi"]
    )

    data.student.item["u-1"] = data.school.item["payamenoor"].add_student(
        data.person.item[7],
        data.egd.item["bachelor"],
        data.egp.item["u-mohandesi-computer"],
    )

    data.student.item["u-2"] = data.school.item["payamenoor"].add_student(
        data.person.item[8],
        data.egd.item["phd"],
        data.egp.item["u-oloom-computer"],
    )

    # endregion

    # region Teacher
    # Teachers
    data.teacher.item["1"] = data.school.item["hesaraki"].add_teacher(
        data.person.item[11],
        data.lesson.item["ps-farsi-aval"],
        data.lesson.item["ps-riazi-dovom"],
    )

    data.teacher.item["1"] = data.school.item["alameh"].add_teacher(
        data.person.item[12],
        data.lesson.item["hs1-riazi-2"],
    )

    # endregion


# endregion


# region Person Faker
def fake_person(data, count):
    for count in range(count):
        # TODO i should refactor this and create Names class and assign the gender attribute to it (i dont have enough time)
        fname_gender_list = (
            ("hossein", data.gender.item["male"]),
            ("mohammad mahdi", data.gender.item["male"]),
            ("reza", data.gender.item["male"]),
            ("maryam", data.gender.item["female"]),
            ("samira", data.gender.item["female"]),
            ("fereshteh", data.gender.item["female"]),
            ("eisa", data.gender.item["female"]),
            ("peyman", data.gender.item["male"]),
            ("mansore", data.gender.item["female"]),
            ("elham", data.gender.item["female"]),
            ("hasan", data.gender.item["male"]),
            ("ali", data.gender.item["male"]),
            ("Saeed", data.gender.item["male"]),
            ("arash", data.gender.item["male"]),
            ("hoorieh", data.gender.item["female"]),
        )
        lname_list = (
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

        # Capitalizing the name parts
        fname_gender_list = tuple(
            (name[0].capitalize(), name[1]) for name in fname_gender_list
        )
        lname_list = tuple(name.capitalize() for name in lname_list)

        temp_fname_gender = random.choice(fname_gender_list)
        temp_first_name = temp_fname_gender[0]
        temp_last_name = random.choice(lname_list)
        temp_gender = temp_fname_gender[1]
        # TODO making the birth_date attribute a random date within a range
        temp_birth_date = datetime(2001, 9, 11)
        temp_education_grade = random.choice(tuple(data.egd.item.values()))

        yield Person(
            temp_first_name,
            temp_last_name,
            temp_gender,
            temp_birth_date,
            temp_education_grade,
        )


# endregion


# region  Main
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
            person.birth_date,
            person.education_grade.name,
            person.national_code,
        )
        print(
            # "{0:^10} {1:<10} {2:>10} \n".format('test', 'test2', 'test3'),
            "{:<5}{:<20}{:<20}{:<10}{!s:<25}{:<15}{:<72}".format(*order)
            # "{:^10}{:^10}".format(person.id, person)
        )


# endregion


if __name__ == "__main__":
    main()
