# Student Management and Analyzing Tool

this program will manage and analyze students data within a school

it containes information about the school and each classroom and teachers

There will be 3 different types of student managements:
1- Primary School (for age 7 - 12)
2- High School (for age 13 - 18)
3- University (+18)

this program backs all of them, but each school must have one of them
There is no defference in object creation for schools in each category. The structures are the same but they have different accesses in managing object attributes that will be explained below



(Exceptions are included with -- under each rule)
Primary School: PS
High School 1st Term: HS1
High School 2nd Term: HS2
University: U


** ClassGroups are directly bined with teachers. Each ClassGroup could contain multiple teachers by default
    -- PS ClassGroups could only have one teacher

** ClassGroups are Contained of multiple students. ther ralation between ClassGroups and students are many-to-many
    -- PS and HS1 ClassGroups

** ClassGroups have an attribute called EducationGroup. that helps defining classes fro each group

** GroupLessons are included within EducationGroups. GroupLessons are used when defining ClassSchedules with Teachers and Students which are then used as blueprints for ClassSessions.

\* (ClassGroups have no connection with ClassRooms)

** ClassGroups can be managed and have a lifespan and it will change by the change of education state

** ClassSessions are objects that have timings (start/end) and are created by ClassGroups, containing their attributes (Students, Teacher, )

** The EducationState will show how long the education durations are and how many of them should or could be passed for each student. its just a blue print that is accessed by ClassGroups (or maybe other classes in the future if necessary)

** The EducationGrade is a blueprint containing information about grades of study that is not used by itself but by ClassGroups and Students to define the stage

** The EducationGroup is also another blue print containing different study fields like Mohandesi shimi, Mohandesi computer, Oloom compouter, etc. its used to help ClassGroup and Students to define the subject of learning. 

** The EducationGroup also containes the lessons provided with each ClassGroup.

** GroupLessons are stored within EducationGrous. then they are used by ClassSchedules (which are created by ClassGroups) and define the schedule of that lesson (this blueprint will be used to create instances of ClassSession, which are containing date and time assigned to each instance session)

** ClassSessions are the class schedule containing date and time, students, teacher, etc. these are created using ClassSchedules

** SchoolStage is an object that defines what type is the school (PS, HS1, HS2, U). this will be used to apply properties to other objects. e.g. policies like objects relation types (one-to-one, one-to-many, etc.).

** ClassGroups in University have a lifespam of 6 months, that is a term long. in ps, hs1, and hs2 this is also related to the term length that is about a year long

** I think it could be a good idea to seperate EducationState and CurrentSchoolState. The EducationState is for students and shows where they are in the path of their education. but the CurrentSchoolState is actually a counter that increases by each term passing and shows the current state/term.



ClassRoom - ClassGroup - Teacher
                |
            Students


Primary School:
    EducationState: the-term
    EducationGrade: 1st grade, 2nd grade, ...
    EducationGroup: General
            GroupLessons: Riazi, Oloom, ...
    ClassGroup: kharazmi-1, 1-2, 1-3, 2-a, 2-b, 2-c, ...
        ClassSchedules
        ClassSession: 
    ClassRoom: 
    Teacher
    Student
* \* ClassRoom and ClassGroup have 1 to 1 relation in Primary School
* \* Students could only be assigned to one ClassGroup (unlike high school and univercity) 


High School 1st term:
    Student
*   \* The following attributes are assigned to students
        EducationState: the-term
        EducationGrade: 7th grade, 8th grade, ...
        EducationGroup: General
            GroupLesson: HedieHa, Ghoran, Riazi, Shimi, ...
    ClassGroup: 
        ClassSchedules
        ClassSession: 
    ClassRoom
    Teacher


High School 2nd term:
    Student
*   \* The following attributes are assigned to students
        EducationState: the-term
        EducationGrade: 7th grade, 8th grade, ...
        EducationGroup: Tajrobi, Riazi, Ensani, ...
            GroupLessons: Shimi, Physic, ...
    ClassGroup: 
        ClassSchedules
        ClassSession: 
    ClassRoom
    Teacher
* \* ClassGroups are like sets of students, they could have intersections and Teachers are bineded with these objects


University:
    Student
*    \* The following attributes are assigned to students
        EducationState: 1st term, 2nd term, 3rd term, ...
        EducationGrade: license, pro-license, doctery
        EducationGroup: Mohandesi shimi, Mohandesi computer, Oloom compouter, ...
            GroupLessons: Riazi-1, Adabiat, ...
    ClassGroup:
        ClassSchedules
        ClassSession: 
    ClassRoom
    Teacher
* \* ClassGroups in University are bined with only one GroupLesson


** Creation of EducationGroups could be available when running the program, as it should be possible to add Units of study to University EducationLessons.



