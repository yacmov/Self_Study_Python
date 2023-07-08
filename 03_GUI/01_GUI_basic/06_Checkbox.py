from tkinter import *

root = Tk()
root.title("Mov GUI")
root.geometry("320x240")

chkvar = IntVar() # chkvar add int value
chkbox = Checkbutton(root, text="Do not show today again", variable=chkvar)
# chkbox.select() # able check box
# chkbox.deselect() # disable check box
chkbox.pack()

chkvar2 = IntVar() # chkvar add int value
chkbox2 = Checkbutton(root, text="Do not show 7 days", variable=chkvar2)
chkbox2.pack()


def btncmd():
    print(chkvar.get())
    print(chkvar2.get())

btn = Button(root, text="Click", command=btncmd)
btn.pack()

root.mainloop()
