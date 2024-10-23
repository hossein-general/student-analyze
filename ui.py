# This module contains user interface functions that will commmunicate with user and has access to bl (business logic) module functions

# region Importing
from typing import Callable  # to assign functions to type hints
from os import system

# endregion


# region Program
class Program:
    def __init__(self) -> None:
        system("cls")
        self.main_menue_options = (
            self.MenueOption(
                "global attribute managment", self.global_attribute_management
            ),
            self.MenueOption("person managment", self.person_management),
        )

    # region Menues
    def main_menue(self):
        menue_done = False
        bottom_message = []
        while True:
            system("cls")
            print("main menue")

            # refactoring the menue so it would contain the "exit" option and having the method stored only (instead of the MenueOption class instance)
            ref_menue = self.option_print_refactor(self.main_menue_options)

            # Cheking if there are any error
            if bottom_message:
                for num in range(len(bottom_message)):
                    print("-", bottom_message.pop(0))

            # Getting the user input
            inp = input("pls enter your choice: ")

            try:
                # Checking if the user input refers to a method that should be called
                if callable(ref_menue[inp]):
                    system("cls")
                    # Calling that method
                    ref_menue[inp]()
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
                        case _:
                            bottom_message.append(
                                f"there was a problem with menue options, pls contact admin: \n{ref_menue[inp]}, type: {type(ref_menue[inp])}"
                            )
                            bottom_message.append("test")
                menue_done = False

    # region Other functions
    def global_attribute_management(self):
        print("global has been called")
        input()

    def person_management(self):
        print("person management has been called")
        input()

    # endregion

    # endrgion

    # region Refactors
    def option_print_refactor(self, menue_options):
        refactored_menue = {}
        for index_id, option in enumerate(menue_options):
            refactored_menue[str(index_id + 1)] = option.trigger
            print(f"{index_id + 1} {option}")

        refactored_menue[str(index_id + 2)] = "Exit"
        print(f"{index_id + 2} Exit")
        return refactored_menue

    class MenueOption:
        def __init__(self, name: str, trigger: Callable) -> None:
            self.name = name
            self.trigger = trigger

        def __str__(self) -> str:
            return self.name

        def __repr__(self) -> str:
            return f'<MenueOption: "{self.name}">'

    # endregion


# endregion


def main():
    # --Only for testing purposes--
    program = Program()
    program.main_menue()


if __name__ == "__main__":
    main()
