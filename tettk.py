__author__ = 'xyang'

from tkinter import *
import time

tk = Tk()
tk.title("Game")
tk.resizable(0,0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
bg = PhotoImage(file="bg.gif")
w = self.bg.width()
h = self.bg.height()
for x in range(0, 10):
    for y in range(0, 8):
        canvas.create_image(x * w, y * h, image=bg, anchor='nw')