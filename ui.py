# This module contains user interface functions that will commmunicate with user and has access to bl (business logic) module functions

# region Importing
from typing import Callable  # to assign functions to type hints
from os import system

# endregion


# region Program
class Program:
    def __init__(self, data) -> None:
        system("cls")

        self.data = data

        # Main Menue menue options
        self.main_menue_options = (
            self.MenueOption(
                "global attribute managment", self.global_attribute_management
            ),
            self.MenueOption("person managment", self.person_management),
        )
        # Global attribute management menue option
        self.glob_attr_manage_mp = (
            self.MenueOption("Education States management", None),
            self.MenueOption("Education Grade management", None),
            self.MenueOption("Education Group management", None),
            self.MenueOption("Lesson management", None),
        )
        # Education State management menue option
        self.es_manage_mp = (
            self.MenueOption("Show all", None, data.es),
            self.MenueOption("Add", None, data.es),
            self.MenueOption("Edit", None, data.es),
            self.MenueOption("Remove", None, data.es),
        )
        # Person management menue option
        self.person_manage_mp = (
            self.MenueOption("Show all", None),
            self.MenueOption("Search", None),
            self.MenueOption("Add", None),
            self.MenueOption("Edit", None),
            self.MenueOption("Remove", None),
        )

    # region Menues
    def menue(self, menue_options: tuple):
        # this variables will show if the requested menue has been called successfully or not
        menue_done = False
        # bottom message is a list containing errors that program have encountered that user has to fix when inputting data
        bottom_message = []
        while True:
            system("cls")
            print("main menue")

            # refactoring the menue so it would contain the "exit" option and having the method stored only (instead of the MenueOption class instance)
            ref_menue = self.option_print_refactor(menue_options)

            # Cheking if there are any error
            if bottom_message:
                for num in range(len(bottom_message)):
                    print("-", bottom_message.pop(0))

            # Getting the user input
            inp = input("pls enter your choice: ")

            try:
                # Checking if the user input refers to a method that should be called
                if callable(ref_menue[inp].trigger):
                    system("cls")
                    # Calling that method
                    # this will also send the data_object (e.g. es, eg, gender, etc.)
                    ref_menue[inp].trigger(ref_menue[inp].data_object)
                    # To know if the ref_menue option has been run and excecuted, so there will be no need for match-case (in the exception else statement)
                    menue_done = True

            except TypeError:
                bottom_message.append("pls enter a valid choice")
                continue

            except KeyError:
                # If the key was not defined in the refactor-print list
                # If the inp value was not empty
                if inp:
                    bottom_message.append("menue item out of range")
                continue

            except BaseException as err:
                bottom_message.append(f"unexpected error: {type(err)}, {err}")
                continue

            else:
                if not menue_done:
                    # defining a match case to handle multiple types of actions
                    match ref_menue[inp]:
                        # for exiting the current menue
                        case "Exit":
                            break
                        case None:
                            bottom_message.append(
                                f"the selected menue is not implemented yet, pls excuse the programmer! :)"
                            )

                        case _:
                            bottom_message.append(
                                f"there was a problem with menue options, pls contact admin: \n{ref_menue[inp]}, type: {type(ref_menue[inp])}"
                            )
                menue_done = False

    # endrgion

    # region Refactors
    def option_print_refactor(self, menue_options):
        refactored_menue = {}
        for index_id, option in enumerate(menue_options):
            refactored_menue[str(index_id + 1)] = option
            print(f"{index_id + 1} {option}")

        if menue_options == self.main_menue_options:
            exit_label = "Exit"
        else:
            exit_label = "Back"

        refactored_menue[str(index_id + 2)] = "Exit"
        print(f"{index_id + 2} {exit_label}")
        return refactored_menue

    class MenueOption:
        def __init__(self, name: str, trigger: Callable, data_object=None) -> None:
            self.name = name
            self.trigger = trigger
            self.data_object = data_object

        def __str__(self) -> str:
            return self.name

        def __repr__(self) -> str:
            return f'<MenueOption: "{self.name}">'

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
