from tkinter import *

root = Tk()
root.title("Mov GUI")
root.geometry("320x240")

label1 = Label(root, text="select menu").pack()

burger_var = IntVar() # add value as int
btn_burger1 = Radiobutton(root, text="Beef burger", value=1, variable=burger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root, text="Chicken burger", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="Cheese burger", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()


label1 = Label(root, text="select drink").pack()

drink_var = StringVar() # add value as int
btn_drink1 = Radiobutton(root, text="Cola", value="Cola", variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text="Fanta", value="Fanta", variable=drink_var)
btn_drink3 = Radiobutton(root, text="Juice", value="Juice", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()




def btncmd():
    print(burger_var.get())
    print(drink_var.get())

btn = Button(root, text="Order", command=btncmd)
btn.pack()

root.mainloop()
