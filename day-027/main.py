from curses import window
from importlib.resources import is_resource
from tkinter import *

def calc_miles():
  miles = float(mile_entry.get()) * 1.609344
  calc_km_label.config(text=round(miles, 4))

window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

mile_entry = Entry(width=8)
mile_entry.grid(column=1, row=0)

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

equal_label = Label(text="is esqual to")
equal_label.grid(column=0, row=1)

calc_km_label = Label(text="0")
calc_km_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calc_button = Button(text="Calculate", command=calc_miles)
calc_button.grid(column=1, row=2)

window.mainloop()