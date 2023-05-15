from tkinter import *
from datetime import timedelta
import tkinter as tk


class CountdownTimer:
    def __init__(self, master):
        self.master = master
        master.title("Countdown Timer ---By SRINIVAAS")

        self.label = Label(master, font=("Arial", 50), text="00:00:00")
        self.label.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")

        self.entry_label = Label(master, text="Set time:")
        self.entry_label.grid(row=1, column=0, padx=20, pady=5, sticky="w")

        self.entry = Entry(master)
        self.entry.grid(row=1, column=1, padx=20, pady=5, sticky="ew")
        self.entry.bind("<Return>", lambda event: self.start())

        self.start_button = Button(master, text="Start", command=self.start)
        self.start_button.grid(row=2, column=0, padx=20, pady=5, sticky="ew")

        self.pause_button = Button(master, text="Pause", command=self.pause, state="disabled")
        self.pause_button.grid(row=2, column=1, padx=20, pady=5, sticky="ew")

        self.resume_button = Button(master, text="Resume", command=self.resume, state="disabled")
        self.resume_button.grid(row=3, column=0, padx=20, pady=5, sticky="ew")

        self.reset_button = Button(master, text="Reset", command=self.reset, state="disabled")
        self.reset_button.grid(row=3, column=1, padx=20, pady=5, sticky="ew")

        self.stop_button = Button(master, text="Stop", command=self.stop, state="disabled")
        self.stop_button.grid(row=4, column=0, columnspan=2, padx=20, pady=5, sticky="ew")

        self.time_left = timedelta()
        self.running = False
        self.paused = False
        self.time_interval = timedelta(seconds=1)

        # configure the grid to resize widgets automatically
        for i in range(2):
            self.master.columnconfigure(i, weight=1)
        for i in range(5):
            self.master.rowconfigure(i, weight=1)

        # allow resizing of the window
        self.master.resizable(True, True)

    def start(self):
        try:
            h, m, s = map(int, self.entry.get().split(":"))
            self.time_left = timedelta(hours=h, minutes=m, seconds=s)
            self.label.config(text=str(self.time_left))
            self.entry.config(state="disabled")
            self.start_button.config(state="disabled")
            self.pause_button.config(state="normal")
            self.reset_button.config(state="normal")
            self.stop_button.config(state="normal")
            self.running = True
            self.master.after(0, self.countdown)
        except ValueError:
            pass


    def pause(self):
        self.paused = True
        self.pause_button.config(state="disabled")
        self.resume_button.config(state="normal")

    def resume(self):
        self.paused = False
        self.pause_button.config(state="normal")
        self.resume_button.config(state="disabled")
        self.master.after(0, self.countdown)

    def reset(self):
        self.running = False
        self.paused = False
        self.time_left = timedelta()
        self.label.config(text="00:00:00")
        self.entry.delete(0, END)
        self.entry.config(state="normal")
        self.start_button.config(state="normal")
        self.pause_button.config(state="disabled")
        self.resume_button.config(state="disabled")
        self.reset_button.config(state="disabled")
        self.stop_button.config(state="disabled")

    def stop(self):
        self.running = False
        self.paused = False
        self.label.config(text="00:00:00")
        self.entry.config(state="normal")
        self.start_button.config(state="normal")
        self.pause_button.config(state="disabled")
        self.resume_button.config(state="disabled")
        self.reset_button.config(state="disabled")
        self.stop_button.config(state="disabled")

    def countdown(self):
        if self.running:
            if not self.paused:
                self.time_left -= self.time_interval
                self.label.config(text=str(self.time_left))
                if self.time_left.total_seconds() == 0:
                    self.running = False
                    self.label.config(text="00:00:00")
                    self.entry.config(state="normal")
                    self.start_button.config(state="normal")
                    self.pause_button.config(state="disabled")
                    self.resume_button.config(state="disabled")
                    self.reset_button.config(state="disabled")
                    self.stop_button.config(state="disabled")
                    self.label.config(text="Time's up!")
                    return
            self.master.after(1000, self.countdown)

root = tk.Tk()
timer = CountdownTimer(root)
root.mainloop()
