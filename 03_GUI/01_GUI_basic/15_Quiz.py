# Create a notepad program using tkinter.

# [GUI conditions]
# 1. title: no title - windows notepad
# 2. Menu: File, Edit, Format, View, Help
# 3. Actual menu implementation: handles only 3 open, save, and exit within the file menu
# 3-1. Open: Open and show the contents of the mynote.txt file
# 3.2. Save: Save the current contents to the file mynote.txt
# 3-3. Exit: end the program
# 4. When the program starts, the text is empty
# 5. No need for the bottom status bar
# 6. The size and location of the program should be free but resizable
# 7. Add a vertical scroll bar to the right of the text

import os
from tkinter import *

root = Tk()
root.title("no title - windows notepad")
root.geometry("640x480")


#########################################################
# Create File Menu

filename = "mynote.txt"

menu = Menu(root)


def file_open():
    if os.path.isfile(filename):
        with open(filename, "r", encoding="utf8") as mynote:
            txt.delete("1.0", END)  # Delete txt before read
            txt.insert(END, mynote.read())  # add txt


def file_save():
    with open(filename, "w", encoding="utf8") as mynote:
        mynote.write(txt.get("1.0", END))


menu_file = Menu(menu, tearoff=0)
# Open and show the contents of the mynote.txt file
menu_file.add_command(label="Opne", command=file_open)
# Save the current contents to the file mynote.txt
menu_file.add_command(label="Save", command=file_save)
# Exit
menu_file.add_separator()
menu_file.add_command(label="Exit", command=quit)

menu.add_cascade(label="File", menu=menu_file)


#########################################################
# Create Edit Menu
menu.add_cascade(label="Edit")


#########################################################
# Create format Menu
menu.add_cascade(label="Format")


#########################################################
# Create view Menu
menu.add_cascade(label="View")


#########################################################
# Create help Menu
menu.add_cascade(label="Help")


#########################################################
# Text form and Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)


txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.config(command=txt.yview)


root.config(menu=menu)
root.mainloop()
