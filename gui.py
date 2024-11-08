import tkinter
from tkinter import *
import tkinter as tk

root = Tk()
Label(root, text="thisis for thest").pack()
scrollbar = Scrollbar(root)
# scrollbar.pack(side=RIGHT, fill=Y)
mylist = Listbox(root)

for line in range(100):
    mylist.insert(END, 'This is line number' + str(line))
    
mylist.pack(side=LEFT, fill=BOTH)
# scrollbar.config(command=mylist.yview)

def main():
    # r.mainloop()
    mainloop()
    pass

if __name__ == '__main__':
    main()