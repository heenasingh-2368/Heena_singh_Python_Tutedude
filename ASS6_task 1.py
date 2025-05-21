from tkinter import *

# Create main window
window = Tk()
window.geometry("500x500")
window.title("Simple Calculator")

# Entry widget
e = Entry(window, width=56, borderwidth=5)
e.place(x=0, y=0)

# Function to insert number/operator
def click(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + str(num))

# Clear function
def clear():
    e.delete(0, END)

# Function to evaluate expression
def equal():
    try:
        result = eval(e.get())
        e.delete(0, END)
        e.insert(0, str(result))
    except:
        e.delete(0, END)
        e.insert(0, "Error")

# Number Buttons
b1 = Button(window, text="1", width=12, command=lambda: click(1))
b1.place(x=10, y=60)

b2 = Button(window, text="2", width=12, command=lambda: click(2))
b2.place(x=130, y=60)

b3 = Button(window, text="3", width=12, command=lambda: click(3))
b3.place(x=250, y=60)

b4 = Button(window, text="4", width=12, command=lambda: click(4))
b4.place(x=10, y=110)

b5 = Button(window, text="5", width=12, command=lambda: click(5))
b5.place(x=130, y=110)

b6 = Button(window, text="6", width=12, command=lambda: click(6))
b6.place(x=250, y=110)

b7 = Button(window, text="7", width=12, command=lambda: click(7))
b7.place(x=10, y=160)

b8 = Button(window, text="8", width=12, command=lambda: click(8))
b8.place(x=130, y=160)

b9 = Button(window, text="9", width=12, command=lambda: click(9))
b9.place(x=250, y=160)

b0 = Button(window, text="0", width=12, command=lambda: click(0))
b0.place(x=130, y=210)

# Operator Buttons
b_plus = Button(window, text="+", width=12, command=lambda: click("+"))
b_plus.place(x=10, y=210)

b_minus = Button(window, text="-", width=12, command=lambda: click("-"))
b_minus.place(x=250, y=210)

b_mul = Button(window, text="*", width=12, command=lambda: click("*"))
b_mul.place(x=10, y=260)

b_div = Button(window, text="/", width=12, command=lambda: click("/"))
b_div.place(x=130, y=260)

b_eq = Button(window, text="=", width=12, command=equal)
b_eq.place(x=250, y=260)

b_clear = Button(window, text="Clear", width=12, command=clear)
b_clear.place(x=130, y=310)

# Run the GUI event loop
window.mainloop()
