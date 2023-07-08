import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Mov GUI")
root.geometry("320x240")

values = ["Day " + str(i) for i in range(1,32)]
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("Payment day")

readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly")
readonly_combobox.current(0)
readonly_combobox.pack()

def btncmd():
    print(combobox.get()) # selected value output
    print(readonly_combobox.get()) # selected value output



btn = Button(root, text="Select", command=btncmd)
btn.pack()

root.mainloop()
