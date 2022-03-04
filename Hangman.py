import tkinter as tk
from tkinter import ttk

import StartPage as StartPage
import BrickBreaker as BrickBreak

fontType = "Verdana"


class HangMan(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Hang Man", font=fontType)
        label.pack(pady=10, padx=10)

        self.label2 = ttk.Label(self, text=controller.getView(), font=fontType)
        self.label2.pack(pady=10, padx=10)

        button1 = ttk.Button(self,
                             text="Back to Home",
                             command=lambda: controller.showFrame(StartPage))
        button1.pack()

        button2 = ttk.Button(self,
                             text="Brick Breaker",
                             command=lambda: controller.showFrame(BrickBreak))
        button2.pack()

        button3 = ttk.Button(self,
                             text="Hang Man",
                             command=lambda: controller.raiseView(HangMan))
        button3.pack()