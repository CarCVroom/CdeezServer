import ctypes
import tkinter as tk
from tkinter import ttk
import os
import sys

# Sets local path for ctypes
ext = ".dll" if sys.platform == "win32" else ".so"
dir = os.path.dirname(os.path.abspath(__file__))
lib = ctypes.CDLL(os.path.join(dir, f"../mylib{ext}"))

root = tk.Tk()

# Name and size
root.title("simple calulator")
root.geometry("900x900")

one = tk.Button(root, height=10,width=20,text="1")
one.place(relx=0.32, rely=0.1, anchor="center")
        
two = tk.Button(root, height=10, width=20,text="2")
two.place(relx=0.5, rely=0.1, anchor="center")

three = tk.Button(root, height=10, width=20,text="3")
three.place(relx=0.68, rely=0.1, anchor="center")

four = tk.Button(root, height=10,width=20,text="4")
four.place(relx=0.32, rely=0.28, anchor="center")
        
five = tk.Button(root, height=10, width=20,text="5")
five.place(relx=0.5, rely=0.28, anchor="center")

six = tk.Button(root, height=10, width=20,text="6")
six.place(relx=0.68, rely=0.28, anchor="center")

seven = tk.Button(root, height=10,width=20,text="7")
seven.place(relx=0.32, rely=0.46, anchor="center")
        
eight = tk.Button(root, height=10, width=20,text="8")
eight.place(relx=0.5, rely=0.46, anchor="center")

nine = tk.Button(root, height=10, width=20,text="9")
nine.place(relx=0.68, rely=0.46, anchor="center")

zero = tk.Button(root, height=10, width=20,text="8")
zero.place(relx=0.5, rely=0.64, anchor="center")

equal = tk.Button(root, height=10, width=20,text="=")
equal.place(relx=0.68, rely=0.64, anchor="center")

pluss = tk.Button(root, height=10, width=20,text="+")
pluss.place(relx=0.32, rely=0.64, anchor="center")

divison = tk.Button(root, height=10, width=20,text="/")
divison.place(relx=0.5, rely=0.82, anchor="center")

minus = tk.Button(root, height=10, width=20,text="-")
minus.place(relx=0.68, rely=0.82, anchor="center")

multi = tk.Button(root, height=10, width=20,text="*")
multi.place(relx=0.32, rely=0.82, anchor="center")

#button = tk.Button(root, text="Submit", command=math)
#button.place(relx=0.5, rely=0.5, anchor="center")

label = tk.Label(root, text="test")
label.place(relx=0.5, rely=0.95, anchor="center")

root.mainloop()