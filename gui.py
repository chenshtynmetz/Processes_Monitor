from tkinter import *
from tkinter import ttk
import tkinter as tk
from monitor import Monitor
from tkinter import messagebox

class Gui:
    def __init__(self):
        self.root = Tk()
        self.root.title("monitor")
        self.root.geometry("850x850")
        self.root.resizable(1, 1)
        self.frm = ttk.Frame(self.root, padding=10)
        self.frm.grid()
        self.text = tk.StringVar()
        ttk.Button(self.frm, text="monitor mode", command=self.monitor_mood).grid(column=1, row=0)
        self.root.mainloop()

    def monitor_mood(self):
        time_root = Tk()
        time_root.title("set time")
        time_root.geometry("500x500")
        time_frm = ttk.Frame(time_root, padding=10)
        time_frm.pack(padx=10, pady=10, fill='x', expand=True)
        # time_frm.grid()
        l1 = ttk.Label(time_frm, text="please enter period of time in seconds:")
        l1.pack(fill='x', expand=True)
        # ttk.Entry(time_frm, widget=)
        textbox = ttk.Entry(time_root, textvariable=self.text)
        textbox.pack(fill='x', expand=True)
        textbox.focus()
        ok_button = ttk.Button(time_frm, text="OK", command=self.start_monitor)  #set command to exit
        ok_button.pack(fill='x', expand=True, pady=5)
        time_root.mainloop()

    def start_monitor(self):
        my_time = self.text.get()
        Monitor(float(my_time))


if __name__ == '__main__':
    Gui()