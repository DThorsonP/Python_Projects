from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    kilo_result_label.config(text=f"{km}")
    

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx= 25, pady=20)

miles_input = Entry(width=15)
miles_input.grid(column=1, row=0)

miles_label = Label(text="miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilo_result_label = Label(text="0")
kilo_result_label.grid(column=1, row=1)

kilo_label = Label(text="km")
kilo_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)




window.mainloop()
