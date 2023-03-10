import os
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

    def add_mood_happy(self):
        self.moods[datetime.datetime.now().isoformat()[:10]] = "happy"
        self.save_mood()

    def add_mood_sad(self):
        self.moods[datetime.datetime.now().isoformat()[:10]] = "sad"
        self.save_mood()

    def add_mood_neutral(self):
        self.moods[datetime.datetime.now().isoformat()[:10]] = "neutral"
        self.save_mood()

    def update_text(self):
        for mood in self.mood_arr:
            mood.destroy()
        for key, val in list(self.load_mood().items())[-7:]:
            label = tk.Label(self.master, text=f"{key}: {val}")
            self.mood_arr.append(label)
            label.pack(side=tk.TOP)

    def update_chart(self):
        self.moods = self.load_mood()
        happy_count = 0
        sad_count = 0
        neutral_count = 0
        for mood in self.moods.values():
            match mood:
                case "happy":
                    happy_count += 1
                case "sad":
                    sad_count += 1
                case "neutral":
                    neutral_count += 1
        labels = ["sad", "neutral", "happy"]
        colors = ["#EB0000", "#E9FF00", "#008E43"]
        values = [sad_count, neutral_count, happy_count]
        for val in values.copy():
            if val == 0:
                ind = values.index(val)
                labels.pop(ind)
                colors.pop(ind)
                values.pop(ind)
        plt.pie(values, labels=labels, colors=colors)
        plt.title("Statistic")
        plt.show()
        self.update_text()

    def save_mood(self):
        with open('moods.json', 'w') as f:
            json.dump(self.moods, f)
        self.update_text()

    @staticmethod
    def load_mood():
        if not os.path.exists("moods.json"):
            with open("moods.json", "w"):
                pass
        with open("moods.json", "r") as file:
            try:
                moods = json.load(file)
            except ValueError:
                moods = {}
        return moods

    @staticmethod
    def mainloop():
        tk.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("200x200")
    app = MoodCalendar(root)
    app.mainloop()
