#!/usr/bin/env python

from tkinter import *
from tkinter import ttk

root = Tk()

#content = ttk.Frame(root)
frame = ttk.Frame(root, width=200, height=150)
label = ttk.Label(frame, text="Full Name:")
entry = ttk.Entry(frame)

buttonNext = ttk.Button(frame, text="Next")
buttonQuit = ttk.Button(frame, text="Quit")

#content.grid(column=0, row=0)
frame.grid(column=0, row=0)
label.grid(column=0, row=0, columnspan=2)
entry.grid(column=0, row=1, columnspan=2)
buttonNext.grid(column=1, row=4)
buttonQuit.grid(column=0, row=4)


root.mainloop()