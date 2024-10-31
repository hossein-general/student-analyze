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


# region MenueOption
class MenueOption:
    cls_name = "MenueOption"

    # Creating Validator object
    check = Validator()

    def __init__(
        self,
        name: str,
        trigger: Union[Callable, None, str],
        data_object: DataObject = None,
    ) -> None:
        # Type Validation
        self.check.check_type(
            name,
            str,
            "name",
            self.cls_name,
        )
        self.check.check_type(
            trigger,
            (Callable, type(None), str),
            "trigger",
            self.cls_name,
        )
        self.check.check_type(
            data_object,
            (DataObject, type(None)),
            "data_object",
            self.cls_name,
        )

        # Initialization
        self.name = name
        self.trigger = trigger
        self.data_object = data_object

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f'<MenueOption: "{self.name}">'


# endregion


# region Program
class Program:
    def __init__(self, data) -> None:
        system("cls")

        self.data = data

        # Main Menue menue options
        self.main_menue_options = (
            MenueOption("global attribute managment", self.global_attribute_management),
            MenueOption("person managment", self.person_management),
        )
        # Global attribute management menue option
        self.glob_attr_manage_mp = (
            MenueOption("Education States management", None),
            MenueOption("Education Grade management", None),
            MenueOption("Education Group management", None),
            MenueOption("Lesson management", None),
        )
        # Education State management menue option
        self.es_manage_mp = (
            MenueOption("Show all", None, data.es),
            MenueOption("Add", None, data.es),
            MenueOption("Edit", None, data.es),
            MenueOption("Remove", None, data.es),
        )
        # Person management menue option
        self.person_manage_mp = (
            MenueOption("Show all", None),
            MenueOption("Search", None),
            MenueOption("Add", None),
            MenueOption("Edit", None),
            MenueOption("Remove", None),
        )
        # Exit/Back menue option
        self.exit_option = MenueOption("Exit", "Exit")
        # ipdb menue option
        self.ipdb_option = MenueOption("ipdb", "ipdb")
        

    # region Menues
    def menue(self, menue_options: tuple):
        # this variables will show if the requested menue has been called successfully or not
        menue_done = False
        # bottom message is a list containing errors that program have encountered that user has to fix when inputting data
        bottom_message = []
        while True:
            # reseting menue_done by each loop
            menue_done = False

            # cleaning the cli screen
            system("cls")
            print("main menue")

            # refactoring the menue so it would contain the "exit" option and having the method stored only (instead of the MenueOption class instance)
            ref_menue = self.option_print_refactor(menue_options)

            # Cheking if there are any error
            if bottom_message:
                for _ in range(len(bottom_message)):
                    print("-", bottom_message.pop(0))

            # Getting the user input
            inp = input("pls enter your choice: ")

            try:
                # Checking if the user input refers to a method that should be called
                # NOTE previously i was making the ref_menue[inp] able to have any type of value
                #   aside from MenueOption instancers, ive been using string and None types too and 
                #   match cased them within the else block. but now its forced to use only MenueOption instances
                if callable(ref_menue[inp].trigger):
                    system("cls")
                    # Calling that method
                    # this will also send the data_object (e.g. es, eg, gender, etc.)
                    ref_menue[inp].trigger(ref_menue[inp].data_object)
                    # To know if the ref_menue option has been run and excecuted, so there will be no need for match-case (in the exception else statement)
                    menue_done = True

            except TypeError as err:
                bottom_message.append(f"pls enter a valid choice \n{err}")
                continue

            except KeyError as err:
                # If the key was not defined in the refactor-print list
                # If the inp value was not empty
                if inp:
                    bottom_message.append(f"menue item out of range \n{err}")
                else:
                    bottom_message.append(f"unexpected KeyError: \n{err}")
                continue

            except BaseException as err:
                bottom_message.append(f"unexpected error: {type(err)}, {err}")
                continue

            else:
                # if the menue ooption was not done within the try block
                if not menue_done:
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
    def option_print_refactor(self, menue_options_main):
        # initializations
        refactored_menue = {}
        menue_options = [(option, option.name) for option in menue_options_main]

        # this part of code desides if the back option should be displayed as "Exit" or not
        # in other words, are we in the main menue or not?
        if menue_options == self.main_menue_options:
            exit_label = "Exit"
        else:
            exit_label = "Back"

        # adding additional options to the menue
        # Exit/Back option
        menue_options.append((self.exit_option, exit_label))

        # ipdb option (for development only)
        menue_options.append((self.ipdb_option, 'ipdb'))

        # printing options
        for index_id, option in enumerate(menue_options):
            refactored_menue[str(index_id + 1)] = option[0]
            print(f"{index_id + 1} {option[1]}")

        return refactored_menue

    # endregion

    # region triger funcs
    def global_attribute_management(self, data_object):
        self.menue(self.glob_attr_manage_mp)

    def person_management(self, data_object):
        self.menue(self.person_manage_mp)

    def show_all(self, data_object):
        # this show_all() function will call another show_all function within the DataObject object
        # The resault is returned within a tuple and will be used to print information
        resault = data_object.retrieve()

        # print(
        #     "{:<5}{:<20}{:<20}{:<10}{!s:<25}{:<15}{:<72}".format(*order)
        # )

    # endregion

    # region start
    # this function is created just because i dont want to call the "menu(main)" directly from main module
    #   (because i have to pass the self.main_menue_options from there and that would look ugly in the main module)
    def start(self):
        self.menue(self.main_menue_options)


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
