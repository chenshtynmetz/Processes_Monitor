import tkinter.simpledialog
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.ttk import Combobox
from monitor import Monitor
from tkinter import messagebox
from manual_mode import Manual

class Gui:
    def __init__(self):
        self.root = Tk()
        self.root.title("monitor")
        self.root.geometry("850x850")
        self.root.resizable(1, 1)
        self.frm = ttk.Frame(self.root, padding=10)
        self.frm.grid()
        self.flag = 1
        # self.monitor
        self.my_time = 0
        ttk.Button(self.frm, text="monitor mode", command=self.monitor_mode).grid(column=1, row=0)
        # ttk.Button(self.frm, text="stop monitor", commad=self.monitor.exit_monitor).grid(column=3, row=0)
        ttk.Button(self.frm, text="manual_mode", command=self.manual_mode).grid(column=1, row=3)
        self.root.mainloop()

    def monitor_mode(self):
        self.my_time = tkinter.simpledialog.askfloat("set time", "please enter period of time in seconds:", parent=self.root)
        self.monitor = Monitor(self.my_time)

    def manual_mode(self):
        time1 = self.enter_time()
        time2 = ""
        while True:
            if self.flag == 2:
                time2 = self.enter_time()
            if self.flag > 2:
                break
        print(time1)
        print(time2)


    def enter_time(self) -> str:
        man_root = Tk()
        man_root.title("set date")
        man_root.geometry("500x500")
        man_frm = ttk.Frame(man_root, padding=10)
        man_frm.grid()
        ttk.Button(man_frm, text="OK", command=man_frm.destroy).grid(column=15, row=60)
        time1 = ""
        ttk.Label(man_root, text="please enter the first time:").grid(column=1, row=0)
        ttk.Label(man_root, text="year:").grid(column=1, row=8)
        years = [i for i in range(2010, 2023)]
        year = StringVar(man_root)
        w = OptionMenu(man_root, year, *years).grid(column=1, row=12)
        ttk.Label(man_root, text="month:").grid(column=4, row=8)
        months = [i for i in range(1, 13)]
        month = StringVar(man_root)
        w = OptionMenu(man_root, month, *months).grid(column=4, row=12)
        ttk.Label(man_root, text="day:").grid(column=7, row=8)
        days = [i for i in range(1, 32)]
        day = StringVar(man_root)
        w = OptionMenu(man_root, day, *days).grid(column=7, row=12)
        ttk.Label(man_root, text="hour:").grid(column=1, row=18)
        hours = [i for i in range(0, 24)]
        hour = StringVar(man_root)
        w = OptionMenu(man_root, hour, *hours).grid(column=1, row=22)
        ttk.Label(man_root, text="minuet:").grid(column=4, row=18)
        minutes = [i for i in range(0, 60)]
        minute = StringVar(man_root)
        w = OptionMenu(man_root, minute, *minutes).grid(column=4, row=22)
        ttk.Label(man_root, text="second:").grid(column=7, row=18)
        secondes = [i for i in range(0, 60)]
        sec = StringVar(man_root)
        w = OptionMenu(man_root, sec, *secondes).grid(column=7, row=22)
        man_root.mainloop()
        time1 += year.get() + "-" + day.get() + " "
        mon_str = "0" + month.get() if (len(month.get()) == 1) else month.get()
        time1 += mon_str + "-"
        day_str = "0" + day.get() if (len(day.get()) == 1) else day.get()
        time1 += day_str + " "
        hour_str = "0" + hour.get() if (len(hour.get()) == 1) else hour.get()
        time1 += hour_str + ":"
        min_str = "0" + minute.get() if (len(minute.get()) == 1) else minute.get()
        time1 += min_str + ":"
        sec_str = "0" + sec.get() if (len(sec.get()) == 1) else sec.get()
        time1 += sec_str
        self.flag = self.flag + 1
        return time1


if __name__ == '__main__':
    Gui()