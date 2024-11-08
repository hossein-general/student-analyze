# This module contains user interface functions that will commmunicate with user and has access to bl (business logic) module functions

# region Importing
# for type hinting
from typing import Callable, Union, Any
from bl import DataObject

# for cleaner look
from os import system

# for validation
from student_analyze import Validator

# Development tools
import ipdb

# endregion


# region UserIn
# the UserIn class is used to store previous user inputs and maybe some more functionality in the future
class UserIn:
    def __init__(self) -> None:
        self.catch = ""

    # getting the user input and returning it
    def user_option(self, show):

        # formatting the self.catch in a way that it doesnt take so much space when is used as a placeholder
        placeholder = self.catch if len(self.catch) <= 6 else (self.catch[:3] + "...")

        # getting input and printing the 'show' value, as well as the last entered value as a placeholder
        new_inp = input(f"{show} <{placeholder}> " if placeholder else f"{show} ")

        if not new_inp:
            return self.catch

        self.catch = new_inp
        return new_inp

    # clearing the previous choices
    def clear_catch(self):
        self.catch = ""


# region MenueOption
class MenueOption:
    cls_name = "MenueOption"

    # Creating Validator object
    check = Validator()

    def __init__(
        self,
        name: str,
        trigger: Union["Menue", None, str, tuple],
    ) -> None:
        # a tuple containing tuples of arguments to be used when passed to type validation
        attr_types = (
            (name, str),
            (trigger, (Menue, Callable, type(None), str)),
        )

        # Type Validations
        self.check.init_check_type(attr_types)

        # Initialization
        self.name = name
        self.trigger = trigger

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f'<MenueOption: "{self.name}">'


# endregion


# region Menue
# TODO adding type validations
class Menue:
    def __init__(self, name: str, *menue_options: MenueOption, data_object=None):
        self.name = name
        # menue options list
        self.molist = menue_options
        self.data_object = data_object


# endregion


# region Program
class Program:
    def __init__(self, data) -> None:
        system("cls")

        self.get = UserIn()
        self.data = data

        # management menue options that will be used for manage base Menues
        manage_mo = (
            MenueOption("Show all", self.show_all),
            MenueOption("Add", None),
            MenueOption("Edit", None),
            MenueOption("Remove", None),
        )

        # region Creating Menues
        # Creating Menues
        # ClassGroup management menue
        self.mo_cg_manage = Menue(
            "Class Group management", *manage_mo, data_object=self.data.cg
        )
        # Teacher management menue
        self.mo_teacher_manage = Menue(
            "Teacher management", *manage_mo, data_object=self.data.teacher
        )
        # Student management menue
        self.mo_student_manage = Menue(
            "Student management", *manage_mo, data_object=self.data.student
        )
        # ClassRoom management menue
        self.mo_croom_manage = Menue(
            "Classroom management", *manage_mo, data_object=self.data.croom
        )
        # School management menue
        self.mo_school_manage = Menue(
            "School management", *manage_mo, data_object=self.data.school
        )
        # Gender management menue
        self.mo_gender_manage = Menue(
            "Gender management", *manage_mo, data_object=self.data.gender
        )
        # Lesson management menue
        self.mo_lesson_manage = Menue(
            "Lesson management", *manage_mo, data_object=self.data.lesson
        )
        # Education Group management menue
        self.mo_egp_manage = Menue(
            "Education Group management", *manage_mo, data_object=self.data.egp
        )
        # Education Grade management menue
        self.mo_egd_manage = Menue(
            "Education Grade management", *manage_mo, data_object=self.data.egd
        )
        # Education State management menue
        self.mo_es_manage = Menue(
            "Education State management", *manage_mo, data_object=self.data.es
        )
        # Person management menue
        self.mo_person_manage = Menue(
            "Person management", *manage_mo, data_object=self.data.person
        )

        # Main Menues Management
        # School Base Direct managements
        self.mo_school_base_direct_manage = Menue(
            "School Base Direct manage",
            MenueOption("School", self.mo_school_manage),
            MenueOption("Classroom", self.mo_croom_manage),
            MenueOption("Student", self.mo_student_manage),
            MenueOption("Teacher", self.mo_teacher_manage),
            MenueOption("Class Group", self.mo_cg_manage),
        )
        # Person realated managements
        self.mo_person_related_manage = Menue(
            "Person realted management",
            MenueOption("Person", self.mo_person_manage),
            MenueOption("Gender", self.mo_gender_manage),
        )
        # School related managements menue & menue options
        self.mo_school_related_manage = Menue(
            "School related managements",
            MenueOption(
                "Direct Class Managements <dev>", self.mo_school_base_direct_manage
            ),
            MenueOption("Schools", None),
        )
        # Global attribute management menue & menue options
        self.mo_glob_attr_manage = Menue(
            "Global Attributes management",
            MenueOption("Education States", self.mo_es_manage),
            MenueOption("Education Grade", self.mo_egd_manage),
            MenueOption("Education Group", self.mo_egp_manage),
            MenueOption("Lesson", self.mo_lesson_manage),
        )
        # Main Menue menue & menue options
        self.mo_main_menue = Menue(
            "Main Menue",
            MenueOption("Global Attribute management", self.mo_glob_attr_manage),
            MenueOption("Person realated management", self.mo_person_related_manage),
            MenueOption("School related managements", self.mo_school_related_manage),
        )
        # Exit/Back menue & menue option
        self.exit_option = MenueOption("Exit", "Exit")
        # ipdb menue option
        self.ipdb_option = MenueOption("ipdb", "ipdb")
        # endregion

    # region Menues
    # TODO adding type validations
    def menue(self, menue_options: Menue):
        # bottom message is a list containing errors that program have encountered that user has to fix when inputting data
        bottom_message = []

        while True:
            # cleaning the cli screen
            system("cls")
            print(menue_options.name)

            # refactoring the menue so it would contain the "exit" option and having the method stored only (instead of the MenueOption class instance)
            ref_menue = self.option_print_refactor(menue_options)

            # Cheking if there are any error
            if bottom_message:
                for _ in range(len(bottom_message)):
                    print("-", bottom_message.pop(0))

            # Getting the user input
            inp = self.get.user_option("pls enter your choice: ")

            try:
                # Checking if the user input refers to a method that should be called
                # NOTE previously i was making the ref_menue[inp] able to have any type of value
                #   aside from MenueOption instancers, ive been using string and None types too and
                #   match cased them within the else block. but now its forced to use only MenueOption instances
                if callable(ref_menue[inp].trigger):
                    system("cls")
                    # Calling that method
                    # this will also send the data_object (e.g. es, eg, gender, etc.)
                    ref_menue[inp].trigger(menue_options.data_object)
                    continue
                    # To know if the ref_menue option has been run and excecuted, so there will be no need for match-case (in the exception else statement)
                elif isinstance(ref_menue[inp].trigger, Menue):
                    self.menue(ref_menue[inp].trigger)
                    continue

            except TypeError as err:
                bottom_message.append(f"pls enter a valid choice")
                continue

            except KeyError as err:
                # If the key was not defined in the refactor-print list
                # If the inp value was not empty
                if inp:
                    bottom_message.append(f"menue item out of range")
                continue

            except BaseException as err:
                bottom_message.append(f"unexpected error: {type(err)}, {err}")
                continue

            else:
                # defining a match case to handle multiple types of actions
                match ref_menue[inp].trigger:
                    # for exiting the current menue
                    case "Exit":
                        break

                    case "ipdb":
                        ipdb.set_trace()

                    case None:
                        bottom_message.append(
                            f"the selected menue is not implemented yet, pls excuse the programmer! :)"
                        )

                    case _:
                        bottom_message.append(
                            f"there was a problem with menue options, pls contact admin: \n{ref_menue[inp]}, type: {type(ref_menue[inp])}"
                        )

    # endrgion

    # region Refactors
    # this method will print menue options and adds some extra options to it, while adding indexes to them
    def option_print_refactor(self, menue_option_original: Menue):
        # initializations
        refactored_menue = {}
        temp_menue_options = [
            (option, option.name) for option in menue_option_original.molist
        ]

        # printing options
        for index_id, option in enumerate(temp_menue_options):
            refactored_menue[str(index_id + 1)] = option[0]
            print(f"{index_id + 1}- {option[1]}")

        # for an empty line
        print()

        # this part of code desides if the back option should be displayed as "Exit" or not
        # in other words, are we in the main menue or not?
        if menue_option_original.name == "Main Menue":
            exit_label = "Exit"
        else:
            exit_label = "Back"

        # adding additional options to the menue
        # Exit/Back option
        refactored_menue["i"] = self.ipdb_option
        print(f"(i)- ipdb")

        # adding additional options to the menue
        # Exit/Back option
        refactored_menue["q"] = self.exit_option
        print(f"(q)- {exit_label}")

        # for an empty line
        print()

        return refactored_menue

    # endregion

    # region triger funcs
    # Triger functions are methods that are used to interact with users
    # they can connect to bl and retrieve data to show, edit, delete, serach and do other things

    # region show_all
    # TODO moving all calculation from the DataObject class here to make customizations possible
    def show_all(self, data_object):
        # to clear previous user inputs
        self.get.clear_catch()
        # import ipdb; ipdb.set_trace()
        # cleaning the screen
        system("cls")

        items, attrs = data_object.retrieve()
        








        # retrieving the list of data from data object
        ret = data_object.retrieve()
        lst = ret[0]
        col_names = ret[1]

        # a variable that defines the current page we are in
        # each page contains 10 rows of data
        page = 1
        # the count of showing rows
        row_count = 10
        # the end page defines the last page for the content
        # (the main use is to define where the last page is so i could prevent any further page forward navigation)

        while True:
            # calculating the page count (considering the number of )
            end_page = (
                len(lst) // row_count
                if len(lst) % row_count == 0
                else len(lst) // row_count + 1
            )
            # cleaning the screen
            system("cls")

            # Initializations
            max_row = 99
            min_row = 5
            starting_row = (page - 1) * row_count + 1
            ending_row = page * row_count

            # The header for the list
            # (also checking if the endrow doesnt exit length of the data list)
            print(
                data_object,
                f": (page: {page}/{end_page}) (rows: {starting_row}-{(ending_row if ending_row <= len(lst) else len(lst))})",
                sep="",
            )

            # Printing list of data (10 items)
            try:
                print()
                print("{:<8}".format("rows"), col_names)
                for i in range(starting_row, ending_row + 1):
                    print("{:<8}".format(f"{i})"), lst[i - 1])

            except IndexError:
                print("end")
                end_page = page

            except BaseException as err:
                print("unexpected error:")
                print(err)

            # Getting user input
            inp = self.get.user_option(
                f"\nq: quit / n: next page / p: previous page / row number ({min_row}-{max_row}): "
            )

            # Checking the user input
            # checking the first index of the string to make it easyier for user (in case of miss hitting other keys)
            match inp[0]:
                case "n":
                    # preventing user from going further than the last page
                    if page < end_page:
                        page += 1

                case "p":
                    if page > 1:
                        page -= 1

                case "q":
                    break

            if inp.isdigit():
                inp = int(inp)
                if inp >= min_row and inp <= max_row:
                    row_count = inp
                    page = 1

    # endregion

    # endregion

    # region start
    # this function is created just because i dont want to call the "menu(main)" directly from main module
    #   (because i have to pass the self.main_menue_options from there and that would look ugly in the main module)
    def start(self):
        self.menue(self.mo_main_menue)


# endregion


# region main (test)
def main():
    # --Only for testing purposes--
    input('Running The "Program" module')
    program = Program()
    program.start()


if __name__ == "__main__":
    main()

# endregion
