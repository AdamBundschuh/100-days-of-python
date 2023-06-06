from tkinter import *


def miles_to_km():
    miles = float(entry_miles.get())
    km = round(miles * 1.609344, 2)
    label_converted.config(text=km)


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

# Label Components
label_converted = Label(text="0", font=("Arial", 16))
label_converted.grid(column=1, row=1)
label_converted.config(pady=10)

label_miles = Label(text="Miles", font=("Arial", 16))
label_miles.grid(column=2, row=0)
label_miles.config(padx=10)

label_km = Label(text="Km", font=("Arial", 16))
label_km.grid(column=2, row=1)

label_equal = Label(text="is equal to", font=("Arial", 16))
label_equal.grid(column=0, row=1)

# Button Components
button_calc = Button(text="Calculate", command=miles_to_km)
button_calc.grid(column=1, row=2)

# Entry Components
entry_miles = Entry(width=10)
entry_miles.grid(column=1, row=0)

# Keep window open
window.mainloop()
