from tkinter import *

window = Tk()
window.title("Working with tkinter and GUI apps")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

# The Label
my_label = Label(text="FOR DA LOVE OF DA GAME", font=("Times New Roman", 14, "bold"))
my_label.grid(column=0, row=4)

def button_clicked():
    print("Push the button")
    new_text = input.get()
    my_label.config(text=new_text)

# The Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=0, row=1)

# The New Button
new_button = Button(text="New Button")
new_button.grid(column=1, row=0)

# The Entry Window
input = Entry(width=20)
print(input.get())
input.grid(column=2, row=2)








window.mainloop()
