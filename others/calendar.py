from tkinter import *
from tkcalendar import Calendar

root = Tk()
root.title("Calendar 2021")

cal = Calendar(root, selectmode = 'day',
    year = 2021,
    month = 5,
    day = 15)
cal.pack()

def grad_date():
    date.config(text = 'Selected date is: ' + cal.get_date())

Button(root, text = 'Get Date',
    command = grad_date).pack(pady = 20)

date = Label(root, text = '')
date.pack(pady = 20)

mainloop()