from tkinter import *

root = Tk()
root.title("Mov GUI")
root.geometry("320x240")

listbox = Listbox(root, selectmode="extended", height=0)
# extended : multi selection allowed
# single : only one can sellect
# height = 0 : show everything mentioned
# height = 3 : show 3 at one time 
listbox.insert(0, "Apple")
listbox.insert(1, "Strawberry")
listbox.insert(2, "Banana")
listbox.insert(END, "Water melon")
listbox.insert(END, "Grape")
listbox.pack()


def btncmd():
    # Delete
    # listbox.delete(0) # delete index 0 / end : delete index end

    # count
    # print("{} lists are in".format(listbox.size()))

    # value check
    # print("List from 1 to 3", str(listbox.get(0, 2)))

    # current sellected (1,2,3,4)
    print("Sellected list :", listbox.curselection())



btn = Button(root, text="Click", command=btncmd)
btn.pack()

root.mainloop()
