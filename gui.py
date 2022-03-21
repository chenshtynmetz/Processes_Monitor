from tkinter import *
from tkinter import ttk

class Gui:
    def __init__(self):
        root = Tk()
        frm = ttk.Frame(root, padding=10)
        frm.grid()
        root.mainloop()