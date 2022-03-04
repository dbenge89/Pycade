import tkinter as tk

from StartPage import StartPage
from BrickBreaker import BrickBreak
from Hangman import HangMan


class Application(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Pycade")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.count = 0
        self.frames = {}

        for Page in (StartPage, BrickBreak, HangMan):
            frame = Page(container, self)
            self.frames[Page] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.showFrame(StartPage)

    def getView(self):
        return self.count

    def raiseView(self, targetFrame):
        self.count += 1
        self.frames[targetFrame].label2.config(text=self.getView())

    def showFrame(self, targetFrame):
        frame = self.frames[targetFrame]
        self.frames[targetFrame].label2.config(text=self.getView())
        frame.tkraise()