import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Mov GUI")


# file frame
file_frame = Frame(root)
file_frame.pack(fill=X, padx=5, pady=5)

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="Add File")
btn_add_file.pack(side=LEFT)
btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="Delete file")
btn_del_file.pack(side=RIGHT)


# list frame
list_frame = Frame(root)
list_frame.pack(fill=BOTH, padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side=RIGHT, fill=Y)

list_file = Listbox(list_frame , selectmode=EXTENDED, height=15, yscrollcommand=scrollbar.set)
list_file.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.config(command=list_file.yview)


# save location frame
path_frame = LabelFrame(root, text="save location")
path_frame.pack(fill=X, padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side=LEFT, fill=X, expand=True,  padx=5, pady=5, ipady=4)

btn_dest_path = Button(path_frame, text="Search", width=10)
btn_dest_path.pack(side=RIGHT, padx=5, pady=5)



# option frame
frame_option = LabelFrame(root, text="Option")
frame_option.pack(padx=5, pady=5, ipady=5)

# Width
lbl_width = Label(frame_option, text="Width", width=8)
lbl_width.pack(side=LEFT)

opt_width = ["Original", "1024", "800", "640"]
cmd_width = ttk.Combobox(frame_option, state="readonly", width=10, values=opt_width)
cmd_width.current(0)
cmd_width.pack(side=LEFT, padx=5, pady=5)


# Space
lbl_space = Label(frame_option, text="Space", width=8)
lbl_space.pack(side=LEFT)

opt_space = ["None", "Narrow", "Normal", "Wide"]
cmd_space = ttk.Combobox(frame_option, state="readonly", width=10, values=opt_space)
cmd_space.current(0)
cmd_space.pack(side=LEFT, padx=5, pady=5)


# Space
lbl_format = Label(frame_option, text="Format", width=8)
lbl_format.pack(side=LEFT)

opt_format = ["PNG", "JPG", "BMP"]
cmd_format = ttk.Combobox(frame_option, state="readonly", width=10, values=opt_format)
cmd_format.current(0)
cmd_format.pack(side=LEFT, padx=5, pady=5)




# progressbar
frame_progress = LabelFrame(root, text="Progress")
frame_progress.pack(fill=X, padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill=X,  padx=5, pady=5)



# Running frame
frame_run = Frame(root)
frame_run.pack(fill=X, padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="Close", width=12, command=root.quit)
btn_close.pack(side=RIGHT, padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="Start", width=12)
btn_start.pack(side=RIGHT,  padx=5, pady=5)






root.resizable(False,False) 
root.mainloop()
