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
        trigger: Union['Menue', None, str, tuple],
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
            (Callable, type(None), str, Menue),
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

# region Menue
class Menue:
    def __init__(self, name: str, *menue_options: MenueOption):
        self.name = name
        # menue options list
        self.molist = menue_options

# endregion

# region Program
class Program:
    def __init__(self, data) -> None:
        system("cls")

        self.data = data

        # Education State management menue option
        self.mo_es_manage = Menue(
            'Education State management',
            MenueOption("Show all", self.show_all, data.es),
            MenueOption("Add", None, data.es),
            MenueOption("Edit", None, data.es),
            MenueOption("Remove", None, data.es),
        )
        # Person management menue option
        self.mo_person_manage = Menue(
            'Person management',
            MenueOption("Show all", self.show_all, data.person),
            MenueOption("Search", None, None),
            MenueOption("Add", None, None),
            MenueOption("Edit", None, None),
            MenueOption("Remove", None, None),
        )
        # Global attribute management menue option
        self.mo_glob_attr_manage = Menue(
            'Global Attributes management',
            MenueOption("Education States management", None, None),
            MenueOption("Education Grade management", None, None),
            MenueOption("Education Group management", None, None),
            MenueOption("Lesson management", None, None),
        )
        # Main Menue menue options
        self.mo_main_menue = Menue(
            'Main Menue',
            MenueOption("global attribute managment", self.mo_glob_attr_manage, None),
            MenueOption("person managment", self.mo_person_manage, None),
        )
        # Exit/Back menue option
        self.exit_option = MenueOption("Exit", "Exit")
        # ipdb menue option
        self.ipdb_option = MenueOption("ipdb", "ipdb")
        

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
        temp_menue_options = [(option, option.name) for option in menue_option_original.molist]

        # printing options
        for index_id, option in enumerate(temp_menue_options):
            refactored_menue[str(index_id + 1)] = option[0]
            print(f"{index_id + 1}- {option[1]}")
        
        # for an empty line
        print()

        # this part of code desides if the back option should be displayed as "Exit" or not
        # in other words, are we in the main menue or not?
        if menue_option_original.name == 'Main Menue':
            exit_label = "Exit"
        else:
            exit_label = "Back"

        # adding additional options to the menue
        # Exit/Back option
        refactored_menue['ipdb'] = self.ipdb_option
        print(f"(i)- ipdb")

        # adding additional options to the menue
        # Exit/Back option
        refactored_menue['q'] = self.exit_option
        print(f"(q)- {exit_label}")

        # for an empty line
        print()

        return refactored_menue

    # endregion

    # region triger funcs
    def show_all(self, data_object):
        # import ipdb; ipdb.set_trace()
        # cleaning the screen
        system('cls')

        # retrieving the list of data from data object
        lst = data_object.retrieve()

        # a variable that defines the current page we are in 
        # each page contains 10 rows of data
        page = 1
        # the end page defines the last page for the content 
        # (the main use is to define where the last page is so i could prevent any further page forward navigation)
        end_page = (len(lst) // 10 if len(lst) % 10 == 0 else len(lst) // 10 +1)

        while True:
            # cleaning the screen
            system("cls")

            # The header for the list
            print(data_object, f": ({page}/{end_page})", sep = "")

            # Printing list of data (10 items)
            try:
                for i in range((page - 1) * 10 + 1, page * 10 + 1):
                    print('{:<8}'.format(f'{i})'), lst[i])

            except IndexError:
                print('end')
                end_page = page

            except BaseException as err:
                print('unexpected error:')
                print(err)
            
            # Getting user input
            inp = input('q: quit / n: next page / p: previous page / any other key: refresh: ')

            # Checking the user input
            match inp:
                case 'n':
                    # preventing user from going further than the last page
                    if page < end_page:
                        page += 1

                case 'p':
                    if page > 1:
                        page -= 1
                
                case 'r':
                    continue

                case 'q':
                    break

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
