from tkinter import *

window = Tk()
window.title("Miles to KM converter")
window.minsize(500, 300)
window.config(padx=30, pady=30)

inputt = Entry()
inputt.grid(column=1, row=0)

mylabel = Label(text="Miles")
mylabel.grid(column=2, row=0)

mylabel1 = Label(text="Is equal to")
mylabel1.grid(column=0, row=1)

inpute = Label(text=0)
inpute.grid(column=1, row=1)

mylabel2 = Label(text="KM")
mylabel2.grid(column=2, row=1)


def button_click():
    ind = inputt.get()
    ind2 = int(ind) * 1.60934
    inpute["text"] = str(ind2)
    print(ind2)


button = Button(text="CALCULATE", command=button_click)
button.grid(column=1, row=2)

window.mainloop()
