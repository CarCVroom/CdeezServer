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


# Gets all of the numbers and operator
entry = tk.Entry(root)
entry.place(relx=0.5, rely=0.4, anchor="center")

entry2 = tk.Entry(root)
entry2.place(relx=0.5, rely=0.46, anchor="center")

entry3 = ttk.Combobox(root, values=["+", "-", "*", "/"]) 
entry3.place(relx=0.5, rely=0.43, anchor="center")

def math():
        value1 = int(entry.get())
        value2 = int(entry2.get())
        value3 = ord(entry3.get()[0])
        
        resualt = lib.onePlusOne(value1, value2, value3)
        label.config(text=f'The answer is {resualt}')

button = tk.Button(root, text="Submit", command=math)
button.place(relx=0.5, rely=0.5, anchor="center")

label = tk.Label(root, text="")
label.place(relx=0.5, rely=0.55, anchor="center")

root.mainloop()