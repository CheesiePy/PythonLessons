from tkinter import *
from tkinter import ttk


def main():
    root = Tk()
    frm = ttk.Frame(root,padding = 10)
    frm.grid()
    ttk.Label(frm, text="May Lindenberg").grid(column=0, row=0)
    ttk.Button(frm,text="Quit", command=root.destroy).grid(column=1, row=0)
    root.mainloop()

main()

    