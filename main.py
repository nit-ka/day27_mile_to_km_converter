from tkinter import *


def mile_to_km_calculate():
    miles_input = float(entry_miles.get())
    km_output = miles_input * 1.609344
    label3.config(text=km_output)


# Window
window = Tk()
window.title("Mile to km Converter")
window.minsize(width=300, height=100)
window.config(padx=50, pady=50)

# Labels
label1 = Label(text="miles", font=("Calibri", 14, "normal"))
label1.config(padx=10, pady=10)
label1.grid(column=2, row=0)

label2 = Label(text="is equal to", font=("Calibri", 14, "normal"))
label2.config(padx=10, pady=10)
label2.grid(column=0, row=1)

label3 = Label(text="0", font=("Calibri", 14, "normal"))
label3.config(padx=10, pady=10)
label3.grid(column=1, row=1)

label4 = Label(text="km", font=("Calibri", 14, "normal"))
label4.config(padx=10, pady=10)
label4.grid(column=2, row=1)

# Entry
entry_miles = Entry(width=7, font=("Calibri", 14, "normal"))
entry_miles.insert(END, string="0")
entry_miles.grid(column=1, row=0)

# Button
button_calculate = Button(text="Calculate",
                          command=mile_to_km_calculate,
                          font=("Calibri", 14, "normal"))
button_calculate.config(padx=10, pady=10)
button_calculate.grid(column=1, row=2)

window.mainloop()
