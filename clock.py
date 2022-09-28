from cProfile import label
from cgitb import text
from logging import _Level
from sqlite3 import Row
import time
from tkinter import*
from tkinter import font
from tkinter.tix import COLUMN

root = Tk()
root.configure('background=black')

def start():
    text = time.strftime("%H:%M:%S")
    label.config(text=text)
    label.after(200,start)

label=label(root,font=("Defult",100),fg="red",bg="black")
label.grid(Row=0, COLUMN=1)
print("Done")
start()
root.mainloop()