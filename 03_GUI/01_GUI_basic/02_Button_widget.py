from tkinter import *

root = Tk()
root.title("Mov GUI")

btn1 = Button(root, text="Button 1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="Button 2")
btn2.pack()

# btn2 = Button(root, padx=5, pady=10, text="Button 222222222222")
# btn2.pack()
## value will show all and make button 

btn3 = Button(root, padx=10, pady=5, text="Button 3")
btn3.pack()

btn4 = Button(root, padx=10, pady=5, text="Button 4")
btn4.pack()

# btn4 = Button(root, padx=10, pady=5, text="Button 444444444")
# btn4.pack()
## setup button and fill the text. if text length is longer then butten will shown part of value 

# padx : add text then keep area of width value
# pady : add text then keep area of height value
# width : setup button size's width
# height : setup button size's height

btn5 = Button(root, fg="red", bg="yellow", text="Botton 5")
btn5.pack()

photo = PhotoImage(file="03_Practice_GUI/01_GUI_basic/img/img_checkbutton.png")
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("Clicked button")

btn7 = Button(root, text="Active botton", command=btncmd)
btn7.pack()


root.mainloop()
