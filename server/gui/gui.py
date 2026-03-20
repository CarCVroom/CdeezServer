import tkinter as tk
from tkinter import font
import ctypes

try:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
except:
        pass
root = tk.Tk()

def printCoolShit():
        print("CoolShit")
        print(font.families())

root.title("Server GUI startup")
root.geometry("700x700")

frontText = tk.Label(root, text="CdeezServer", font=("Comic Sans MS", 25)).place(relx=0.5, rely=0.1, anchor="center")

IPLabel = tk.Label(root, text="IP:").place(relx=0.2, rely=0.25, anchor="center")
IPEntry = tk.Entry(root, width=35)
IPEntry.place(relx=0.5, rely=0.25, anchor="center")

PortLabel = tk.Label(root, text="Port:").place(relx=0.2, rely=0.35, anchor="center")
PortEntry = tk.Entry(root, width=35)
PortEntry.place(relx=0.5, rely=0.35, anchor="center")

RootLabel = tk.Label(root, text="Doc Root:").place(relx=0.2, rely=0.45, anchor="center")
RootEntry = tk.Entry(root, width=35)
RootEntry.place(relx=0.5, rely=0.45, anchor="center")

MaxConnLabel = tk.Label(root, text="Max Conn:").place(relx=0.2, rely=0.55, anchor="center")
MaxConnEntry = tk.Entry(root, width=35)
MaxConnEntry.place(relx=0.5, rely=0.55, anchor="center")

StartButton = tk.Button(root, text="Start Server", command=printCoolShit)
StartButton.place(relx=0.5, rely=0.75, anchor="center")

root.mainloop()