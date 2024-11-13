# NOTE find the tcl folder and use the path to set the following variable in venv/scripts/activate.bat
# set "TCL_LIBRARY=C:\Users\h.ramezani\AppData\Local\Programs\Python\Python313\tcl\tcl8.6"

# NOTE how to find the folder path:
# root = tk.Tk()
# print(root.tk.exprstring('$tcl_library'))
# print(root.tk.exprstring('$tk_library'))



# region IMPORTING
# For a cleaner look
from os import system

# Program Modules
import faker
from ui import Program
from bl import RuntimeDataAccessor
from dal import (
    run,
    fetch_data,
)

# for gui
import gui
import tkinter as tk

# endregion

# region ui options
# panel access functions
def run_gui(data):
    # Create the main window (root)
    root = tk.Tk()
    
    # Create the CounterApp
    app = gui.CounterApp(root, data)
    
    # Start the Tkinter event loop
    root.mainloop()


def run_cli(data):
    # running the ui app
    program = Program(data)
    program.start()


def run_dal(data):
    # only for direct dal access (dev mode)
    system('cls')
    run(data)

# endregion





# main: Containing functions for users to modify and manage the applicatoin (like adding person, organization, etc.)
def main():
    data = RuntimeDataAccessor()

    if input('do you wanna use faker or fetch? (leave blank for fetch) ') == "":
        fetch_data(data)

    else:
        # region initializations and fakers
        faker.init_data(data)
        person_gen = faker.fake_person(data, 5)
        for new_person in person_gen:
            data.person.item[new_person.id] = new_person

    # endregion

    inp = input('where are you going? (1: gui / 2: cli / 3: direct dal)')

    match inp:
        # GUI
        case '1':
            run_gui(data)

        # CLI
        case '2':
            run_cli(data)

        # DAL
        case '3':
            run_dal(data)

        case '':
            run_cli(data)

    system("cls")
    print("Good Luck")


if __name__ == "__main__":
    main()
