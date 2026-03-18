import tkinter as tk

root = tk.Tk()

root.title("My first app")
root.geometry("300x200")

label = tk.Label(root, text = "")
label.place(x = 110, y = 40)

button = tk.Button(root, text = "Click me", command= lambda: label.config(text="You clicked the button"))
button.place(x=110, y =80)

root.mainloop()