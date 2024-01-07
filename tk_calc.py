# 7 January 2024
'''
Welcome to my first Python project involving Tkinter in Python!
A simple calculator constructed as a GUI application.

The code creates a basic calculator using Tkinter in Python.
It defines functions for handling button clicks, sets up the
GUI components, and uses a grid layout for button placement.
The "=" button evaluates expressions, while "Error" is displayed
in red if an evaluation exception occurs.

NOTE: Please have tkinter, a Python binding to the Tk GUI toolkit,
installed before running this code. Thank you.
'''
from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("Calculator")

def Take_input(button):
    current_input = inputtxt.get("1.0", "end-1c")

    if button == "C":
        inputtxt.delete("1.0", END)
    elif button == "=":
        try:
            result = eval(current_input)
            inputtxt.delete("1.0", END)
            inputtxt.insert(END, str(result))
        except Exception as e:
            inputtxt.delete("1.0", END)
            inputtxt.insert(END, "Error")
            inputtxt.tag_configure("error", foreground="red")
            inputtxt.tag_add("error", "1.0", "end")
    else:
        inputtxt.insert(END, button)

l = Label(text="Crystal's Calculator")
inputtxt = Text(root, height=2, width=25, bg="#e2e0e0")

buttons = [
    "1", "2", "3", "+",
    "4", "5", "6", "-",
    "7", "8", "9", "*",
    "C", "0", "=", "/"
]

row_val = 1
col_val = 0

for button in buttons:
    if button == "=":
        Button(root, text=button, height=3, width=4, command=lambda b=button: Take_input(b), bg="blue", fg="white").grid(row=row_val + 2, column=col_val)
    elif button == "+":
        Button(root, text=button, height=3, width=4, command=lambda b=button: Take_input(b)).grid(row=row_val + 2, column=col_val)
    else:
        Button(root, text=button, height=3, width=4, command=lambda b=button: Take_input(b)).grid(row=row_val + 2, column=col_val)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

l.grid(row=0, column=0, columnspan=4)
inputtxt.grid(row=1, column=0, columnspan=4)

root.mainloop()
