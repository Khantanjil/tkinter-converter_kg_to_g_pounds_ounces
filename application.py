""" Please create a python program that expects a kilogram input value and converts that value to grams, pounds and
ounces when the user pushes the convert button"""

from tkinter import *

# Create the window
window = Tk()


def converter():
    g = float(e1_value.get()) * 1000
    p = float(e1_value.get()) * 2.20462
    o = float(e1_value.get()) * 35.274
    t1.insert(END, g)
    t2.insert(END, p)
    t3.insert(END, o)


l1 = Label(window, text="Kg")
l1.grid(row=0, column=0)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

b1 = Button(window, text="Convert", command=converter)
b1.grid(row=0, column=2)

t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=0)

t2 = Text(window, height=1, width=20)
t2.grid(row=1, column=1)

t3 = Text(window, height=1, width=20)
t3.grid(row=1, column=2)

# Show the window
window.mainloop()  # This is the same as Tk().mainloop()
