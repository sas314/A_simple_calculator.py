#A_simple_calculator
import tkinter as tk
from tkinter import *
global num1
window = tk.Tk()
buttons = [[1, 2, 3,0],
           [4, 5, 6,"/"],
           [7, 8, 9,"."],
           ["+", "-", "*","="]]
label = tk.Label(text="", font=("Helvetica", 30, "bold"))
label.pack()
frame = Frame(window)
frame.pack()
flag = 1
def get(row, column):
    global num1
    result=0
    if str(buttons[row][column]['text']) != "=" :
        num1 += str(buttons[row][column]['text'])
        label.config(text=num1)
    if buttons[row][column]['text'] =="=":
        try:
           result= str(eval(num1))
           label.config(text=result)
           num1=""

        except ZeroDivisionError:
            label.config(text="undefined")
            num1 = ""
        except SyntaxError:
            label.config(text="Syntax Error")
            num1 = ""

def clear():
    global num1
    num1=""
    label.config(text=num1)

num1 = ""
for r in range(4):
    for c in range(4):
        buttons[r][c] = Button(frame, text=buttons[r][c], font=("Helvetica", 20), width=5, height=2, command=lambda row=r, column=c: get(row, column))
        buttons[r][c].grid(row=r, column=c, padx=5, pady=5)
Button_clear=Button( text="clear", font=("Helvetica", 20), width=5, height=2,  command= lambda :clear())
Button_clear.pack()
window.mainloop()
