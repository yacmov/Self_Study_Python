import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("Mov GUI")
root.geometry("320x240")


# booking system by Train
def info():
    msgbox.showinfo("Notice", "Booking success")
def warn():
    msgbox.showwarning("Wanning", "The seat was taken")
def error():
    msgbox.showerror("Error", "Payment unsuccessful")
def okcancel():
    msgbox.askokcancel("Confirm / Cancel", "The seat include an infant. Do you want to keep continue?")
def retrycancel():
    response = msgbox.askretrycancel("Re Try / Cancel", "An error occur, Do you want to re try?")
    print(response) # True = 1, False = 0
    if response == 1: print("Re Try")
    elif response == 0: print("Cancel")

def yesno():
    msgbox.askyesno("Yes / No", "The seat located reverse do you want to keep continue?")
def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="The booking wasn't saved, \n Do you want to save before closing program?")
    # Yes : quit after save
    # No : quit without save
    # Cancel : close the popup message window and back to before
    print(response) # True = 1, False = 0
    if response == 1: print("Yes")
    elif response == 0: print("No")
    else: print("Cancel")




Button(root, command=info, text="Notice").pack()
Button(root, command=warn, text="Warnning").pack()
Button(root, command=error, text="Error").pack()


Button(root, command=okcancel, text="Confirm CANCEL").pack()
Button(root, command=retrycancel, text="Retry CANCEL").pack()
Button(root, command=yesno, text="Yes No").pack()
Button(root, command=yesnocancel, text="Yes No Cancel").pack()

root.mainloop()
