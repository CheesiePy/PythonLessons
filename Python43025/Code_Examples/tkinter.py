

from tkinter import ttk, Tk

# Create the main window widget
root = Tk()

frame = ttk.Frame(root, padding=10)
frame.grid()

# Create a label widget
ttk.Label(frame, text="Hello, Tkinter!").grid(column=0, row=0)
ttk.Button(frame, text="Exit", command=root.destroy).grid(column=1, row=0)
root.mainloop()