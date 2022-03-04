import tkinter as tk

from Main import Application
from StartPage import StartPage
from BrickBreaker import BrickBreak
from Hangman import HangMan

app = Application()

app.geometry('1280x800')

navMenu = tk.Menu(app)
menu = tk.Menu(navMenu, tearoff=0)

navMenu.add_cascade(menu=menu, label="Start")

menu.add_command(label="Start", command=lambda: app.showFrame(StartPage))
menu.add_command(label="Brick Breaker",
                 command=lambda: app.showFrame(BrickBreak))
menu.add_command(label="Hang Man", command=lambda: app.showFrame(HangMan))
menu.add_command(label="Coming Soon...", command=lambda: app.showFrame())

app.config(menu=navMenu)

app.mainloop()
