import ctypes
import tkinter as tk
from tkinter import ttk
import os
import sys

math1 = ""
math2 = ""
valueOne = ""
valueTwo = ""
operator = ""

def value1(value):
        global valueOne, valueTwo, math2
        
        valueOne += str(value) 
        valueTwo += str(value)
        math2 += str(value)
        
        valueTwo = int(valueTwo)
        valueOne = int(valueOne)
        math2 = int(math2)
        label.config(text=f'1st number is {valueOne}, the seccond is {math2}, operator is {operator}')



def oparator1(value):
        global operator
        operator = value

        global math1 
        math1 = valueOne


def clear():
        global valueTwo
        valueTwo = 0
        global math1
        math1 = 0
        global valueOne
        valueOne = 0
        global math2
        math2 = 0
        global operator 
        operator = ""
        label.config(text=f'1st number is {valueOne}, the seccond is {math2}, operator is {operator}')


# Sets local path for ctypes
ext = ".dll" if sys.platform == "win32" else ".so"
dir = os.path.dirname(os.path.abspath(__file__))
lib = ctypes.CDLL(os.path.join(dir, f"../mylib{ext}"))

root = tk.Tk()

# Name and size
root.title("simple calulator")
root.geometry("900x900")

one = tk.Button(root, height=10,width=20,text="1", command=lambda: value1("1") )
one.place(relx=0.32, rely=0.1, anchor="center")
        
two   = tk.Button(root, height=10, width=20, text="2", command=lambda: value1("2"))
two.place(relx=0.5, rely=0.1, anchor="center")

three = tk.Button(root, height=10, width=20, text="3", command=lambda: value1("3"))
three.place(relx=0.68, rely=0.1, anchor="center")

four  = tk.Button(root, height=10, width=20, text="4", command=lambda: value1("4"))
four.place(relx=0.32, rely=0.28, anchor="center")

five  = tk.Button(root, height=10, width=20, text="5", command=lambda: value1("5"))
five.place(relx=0.5, rely=0.28, anchor="center")

six   = tk.Button(root, height=10, width=20, text="6", command=lambda: value1("6"))
six.place(relx=0.68, rely=0.28, anchor="center")

seven = tk.Button(root, height=10, width=20, text="7", command=lambda: value1("7"))
seven.place(relx=0.32, rely=0.46, anchor="center")

eight = tk.Button(root, height=10, width=20, text="8", command=lambda: value1("8"))
eight.place(relx=0.5, rely=0.46, anchor="center")

nine  = tk.Button(root, height=10, width=20, text="9", command=lambda: value1("9"))
nine.place(relx=0.68, rely=0.46, anchor="center")

zero  = tk.Button(root, height=10, width=20, text="0", command=lambda: value1("0"))
zero.place(relx=0.5, rely=0.64, anchor="center")

equal = tk.Button(root, height=10, width=20,text="=", command=lambda: math(operator, math1, math2))
equal.place(relx=0.68, rely=0.64, anchor="center")

pluss = tk.Button(root, height=10, width=20,text="+", command=lambda: oparator1("+"))
pluss.place(relx=0.32, rely=0.64, anchor="center")

divison = tk.Button(root, height=10, width=20,text="/", command=lambda: oparator1("/"))
divison.place(relx=0.5, rely=0.82, anchor="center")

minus = tk.Button(root, height=10, width=20,text="-", command=lambda: oparator1("-"))
minus.place(relx=0.68, rely=0.82, anchor="center")

multi = tk.Button(root, height=10, width=20,text="*", command=lambda: oparator1("*"))
multi.place(relx=0.32, rely=0.82, anchor="center")



def math(operatorF, math1, math2):
        operatorF = ord(operatorF[0])
        resualt = lib.onePlusOne(math1, math2, operatorF)
        label.config(text=f"The anwser is {resualt}")


label = tk.Label(root, text="")
label.place(relx=0.5, rely=0.95, anchor="center")

clearBtn = tk.Button(root, text="Clear")
clearBtn.place(relx=0.32, rely=0.8, anchor="center")

root.mainloop()