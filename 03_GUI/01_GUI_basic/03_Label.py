from tkinter import *

root = Tk()
root.title("Mov GUI")
root.geometry("320x240")


label1 = Label(root, text="Hello")
label1.pack()

photo = PhotoImage(file="03_GUI/01_GUI_basic/img/img_checkbutton.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="See you again!")
    
    global photo2 # if not setup global, gabage collected 
    photo2 = "03_GUI/01_GUI_basic/img/img_xbutton.png"
    photo.config(file=photo2)

btn = Button(root, text="Click", command=change)
btn.pack()

root.mainloop()
