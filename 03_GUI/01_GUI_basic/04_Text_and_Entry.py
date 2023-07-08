from tkinter import *

root = Tk()
root.title("Mov GUI")
root.geometry("320x240")

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "Enter the text")

e = Entry(root, width=30)
e.pack()
e.insert(0, "One line only")

def btncmd():
    print(txt.get("1.0", END))
    # 1 : start line 1
    # 0 : start index 1
    # END : to the end
    print(e.get())

    txt.delete("1.0", END)
    e.delete(0, END)


btn = Button(root, text="Click", command=btncmd)
btn.pack()

root.mainloop()
