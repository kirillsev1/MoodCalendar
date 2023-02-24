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

        self.happy_button = tk.Button(self.mood_frame, text="Happy", command=self.add_mood_happy)
        self.happy_button.pack(side=tk.LEFT)

        self.sad_button = tk.Button(self.mood_frame, text="Sad", command=self.add_mood_sad)
        self.sad_button.pack(side=tk.LEFT)

        self.neutral_button = tk.Button(self.mood_frame, text="Neutral", command=self.add_mood_neutral)
        self.neutral_button.pack(side=tk.LEFT)

        self.stats = tk.Button(master, text="Stats", command=self.update_chart)
        self.stats.pack(side=tk.BOTTOM)

        self.mood_arr = []
        self.moods = self.load_mood()
        self.update_text()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("200x200")
    app = MoodCalendar(root)
    app.mainloop()