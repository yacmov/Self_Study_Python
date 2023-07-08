from tkinter import *

root = Tk()
root.title("Mov GUI")
root.geometry("320x240")

menu = Menu(root)

def create_new_file():
    print("Created new file")

# File Menu
menu_file = Menu(menu, tearoff= 0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New window")
menu_file.add_separator()
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable") # disable save all
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)


# Edit menu
menu.add_cascade(label="Edit")


# Language menu (radio botton)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="C++")
menu_lang.add_radiobutton(label="Java")
menu.add_cascade(label="Language", menu=menu_lang)


# View menu (checkbox)
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu_view.add_checkbutton(label="Terminal")
menu.add_cascade(label="View", menu=menu_view)



root.config(menu=menu)
root.mainloop()
