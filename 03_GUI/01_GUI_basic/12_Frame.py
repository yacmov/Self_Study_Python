from tkinter import *

root = Tk()
root.title("Mov GUI")
root.geometry("320x240")

Label(root, text="Select Menu").pack(side="top")

Button(root, text="Order").pack(side="bottom")

# Burger Frame
frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text="Beef bauger").pack()
Button(frame_burger, text="Chicken bauger").pack()
Button(frame_burger, text="Cheese bauger").pack()


# Drink Frame
frame_drink = LabelFrame(root, text="Drink")
frame_drink.pack(side="right", fill="both", expand=True)
Button(frame_drink, text="Cola").pack()
Button(frame_drink, text="Juice").pack()




root.mainloop()
