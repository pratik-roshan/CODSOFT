import tkinter
from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("570x600+100+200")
root.resizable(False,False)
root.configure(bg="#17161b")

equation = ""

def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def clear_last():
    global equation
    if equation:
        equation = equation[:-1]  # Remove the last character from the equation
        label_result.config(text=equation)


def calculate():
    global equation
    result = ""
    if equation !="":
        try:
            result = eval(equation)
        except:
            result = "error"
            equation = ""
    label_result.config(text=result)

def key_event(event):
    key = event.char
    if key.isdigit() or key in "+-*/%.":
        show(key)
    elif key == "\r":  # Handle Enter key for calculation
        calculate()
    elif key == "\x08":  # Handle Backspace key for clearing the last character
        clear_last()

label_result = Label(root, width=30, height=2, text="", font=("Times New Roman", 30), bg='#ccddff')
label_result.pack()

Button(root, text="C", width=5, height=1, font=("Times New Roman", 30, "bold"), bd=1, fg="#ffa500", bg="#2a2d36", command=lambda: clear()).place(x=10, y=100)
Button(root, text="\u2190", width=5, height=1, font=("Times New Roman", 30, "bold"), bd=1, fg="#ffa500", bg="#2a2d36", command=lambda: clear_last()).place(x=150, y=100)
Button(root, text="%", width=5, height=1, font=("Times New Roman", 30, "bold"), bd=1, fg="#ffa500", bg="#2a2d36",  command=lambda: show("%")).place(x=290, y=100)
Button(root, text="/", width=5, height=1, font=("Times New Roman", 30, "bold"), bd=1, fg="#ffa500", bg="#2a2d36", command=lambda: show("/")).place(x=430, y=100)

Button(root, text="7", width=5, height=1, font=("Times New Roman", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("7")).place(x=10, y=200)
Button(root, text="8", width=5, height=1, font=("Times New Roman", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("8")).place(x=150, y=200)
Button(root, text="9", width=5, height=1, font=("Times New Roman", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("9")).place(x=290, y=200)
Button(root, text="*", width=5, height=1, font=("Times New Roman", 30, "bold"), bd=1, fg="#ffa500", bg="#2a2d36", command=lambda: show("*")).place(x=430, y=200)

Button(root, text="4", width=5, height=1, font=("Times New Roman", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("4")).place(x=10, y=300)
Button(root, text="5", width=5, height=1, font=("Times New Roman", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("5")).place(x=150, y=300)
Button(root, text="6", width=5, height=1, font=("Times New Roman", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("6")).place(x=290, y=300)
Button(root, text="-", width=5, height=1, font=("Times New Roman", 30, "bold"), bd=1, fg="#ffa500", bg="#2a2d36", command=lambda: show("-")).place(x=430, y=300)

Button(root, text="1", width=5, height=1, font=("Times New Roman", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("1")).place(x=10, y=400)
Button(root, text="2", width=5, height=1, font=("Times New Roman", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("2")).place(x=150, y=400)
Button(root, text="3", width=5, height=1, font=("Times New Roman", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("3")).place(x=290, y=400)
Button(root, text="+", width=5, height=1, font=("Times New Roman", 30, "bold"), bd=1, fg="#ffa500", bg="#2a2d36", command=lambda: show("+")).place(x=430, y=400)

Button(root, text="0", width=5, height=1, font=("Times New Roman", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("0")).place(x=10, y=500)
Button(root, text=".", width=5, height=1, font=("Times New Roman", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show(".")).place(x=150, y=500)
Button(root, text="=", width=11, height=1, font=("Times New Roman", 30, "bold"), bd=1, fg="#fff", bg="#ffa500", command=lambda: calculate()).place(x=290, y=500)

# Bind keyboard keys to functions
root.bind("<Key>", key_event)

root.mainloop()
