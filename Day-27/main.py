from tkinter import *


def button_clicked():
    new_text = input.get()
    result.config(text=float(new_text)*1.609344)


window = Tk()
window.title("Miles to KM converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

#Label
my_label = Label(text="I Am a Label", font=("Arial", 18, "bold"))
my_label.config(text="Please input miles")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

my_label_2 = Label(text="I Am a Label", font=("Arial", 18, "bold"))
my_label_2.config(text="Result")
my_label_2.grid(column=0, row=1)
my_label_2.config(padx=50, pady=50)

#Label KM
result = Label(text="I Am a Label", font=("Arial", 12, "bold"))
result.grid(column=1, row=1)
result.config(padx=50, pady=50)

#Button
button = Button(text="Convert to KM", command=button_clicked)
button.grid(column=2, row=0)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=1, row=0)

window.mainloop()