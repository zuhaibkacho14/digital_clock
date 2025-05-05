# Digital Clock using Python

import tkinter as tk         #tkinter module hepls to creating GUI window
from time import strftime    # strtime use to get current time and date in specific format

root = tk.Tk()  #creating main window
root.title("Digital Clock")   # title of main window

# time funtion definations
def time():
    string = strftime("%I: %M: %S %p \n %D")  #current time and date in string
    label.config(text=string)            # update label text
    label.after(1000, time)          # every 1000 millisecond(1 sec) time() call

label = tk.Label(root, font="arial 30 bold", background="yellow", foreground="blue")
label.pack(anchor="center")

time()
root.mainloop() # open and running main window