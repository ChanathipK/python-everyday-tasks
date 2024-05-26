from tkinter import *
from tkinter import ttk

# tkdocs -> tutorials -> example

def tk_main():
    root = Tk();
    mainframe = ttk.Frame(root, padding="5 5 12 12");
    mainframe.grid(column=1, row=1, sticky=(N, W, E, S));
    root.mainloop()