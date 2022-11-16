# import the tkinter module
from tkinter import *
from tkinter import ttk

# create the root window
root = Tk()


# create a frame in the window to hold other widgets
frm = ttk.Frame(root, padding=100)
frm.grid() # use the grid geometry manager

ttk.Label(frm, text="Hey my friend").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=1)


# start the GUI
root.mainloop()