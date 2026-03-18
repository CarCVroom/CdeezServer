import ctypes
import tkinter as tk
import os

dir = os.path.dirname(os.path.abspath(__file__))
lib = ctypes.CDLL(os.path.join(dir, "../mylib.so"))

root = tk.Tk()

root.title("simple calulator")
root.geometry("900x900")

entry = tk.Entry(root)
entry.place(relx=0.5, rely=0.4, anchor="center")
entry2 = tk.Entry(root)
entry2.place(relx=0.5, rely=0.45, anchor="center")

def math():
        value1 = int(entry.get())
        value2 = int(entry2.get())
        resualt = lib.onePlusOne(value1, value2)
        label.config(text=resualt)

button = tk.Button(root, text="Submit", command=math)
button.place(relx=0.5, rely=0.5, anchor="center")

label = tk.Label(root, text="")
label.place(relx=0.5, rely=0.55, anchor="center")

root.mainloop()