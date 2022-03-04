import tkinter as tk
from tkinter import ttk

import StartPage as StartPage
import BrickBreaker as BrickBreak
import Hangman as HangMan

fontType = ("Verdana", 12)


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Start Page", font=fontType)
        label.pack(pady=10, padx=10)

        self.label2 = ttk.Label(self, text=controller.getView(), font=fontType)
        self.label2.pack(pady=10, padx=10)

        button = ttk.Button(self,
                            text="Brick Breaker",
                            command=lambda: controller.showFrame(BrickBreak))
        button.pack()

        button2 = ttk.Button(self,
                             text="Hang Man",
                             command=lambda: controller.showFrame(HangMan))
        button2.pack()

        button3 = ttk.Button(self,
                             text="Start Page",
                             command=lambda: controller.raiseView(StartPage))
        button3.pack()