import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Mov GUI")
root.geometry("320x240")
####################################

# # progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# # # indeterminate : infinitly working
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# # determinate : fill from 0 to 100



# progressbar.start(10) # 10ms moving
# progressbar.pack()

####################################
# def btncmd():
#     progressbar.stop()
####################################
# btn = Button(root, text="Stop", command=btncmd)
# btn.pack()



p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()


def btncmd2():
    for i in range(1, 101):
        time.sleep(0.01) # 0.01 second

        p_var2.set(i) # progress value set
        progressbar2.update() # ui update
        


        if i == 20 or i == 50:
            print("complated {}%".format(i))
        elif i == 100:
            print("Done {}%".format(i))
        
btn2 = Button(root, text="Start", command=btncmd2)
btn2.pack()



root.mainloop()
