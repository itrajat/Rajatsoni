from tkinter import*
from tkinter.ttk import*

from time import strftime

root = Tk()
root.title("clock")

def time():
    string = strftime('%H:%M:%S')
    label.config(text=string)
    

label = Label(root, font=("ds-digital", 80), background ="black", foreground = "cyan")
label.pack(anchor='center')
time()

mainloop()
