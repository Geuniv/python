# code 10 - 04.py

from tkinter import *

window = Tk()

photo = PhotoImage(file ="../GIF/dog.gif")
lable1 = Label(window, image = photo)

lable1.pack()

window.mainloop()