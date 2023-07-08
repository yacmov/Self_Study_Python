from tkinter import *

root = Tk()
root.title("Mov GUI")
root.geometry("320x240")


frame = Frame(root)
frame.pack()

scrollar = Scrollbar(frame)
scrollar.pack(side="right", fill=Y)


listbox = Listbox(frame,selectmode="ëxtended", height=10, yscrollcommand=scrollar.set)
for i in range(1, 32):
    listbox.insert(END, "Day" + str( i))
listbox.pack(side=LEFT)

scrollar.config(command=listbox.yview)


root.mainloop()
