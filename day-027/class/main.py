from tkinter import *
 
def button_clicked():
  text = input.get()
  my_label.config(text=text)

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=200, pady=200)
my_label = Label(text="I am a Label", font=("Sans serif", 16, "bold"))
my_label.grid(column=0, row=0)
my_label["text"] = "new text"

button = Button(text="Button", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

input = Entry(width=15)
input.grid(column=3, row=2)


window.mainloop()