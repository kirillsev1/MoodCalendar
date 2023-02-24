import tkinter as tk
import json
import datetime
import matplotlib

matplotlib.use('TkAgg')

import matplotlib.pyplot as plt


class MoodCalendar:

    def __init__(self, master):
        self.master = master
        master.title("Mood calendar")

        self.mood_frame = tk.Frame(master, width=200, height=200)
        self.mood_frame.pack(side=tk.TOP)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("200x200")
    app = MoodCalendar(root)
    app.mainloop()
