import tkinter as tk
from tkinter import ttk

# initializes the window
root = tk.Tk()

# creates window header 
root.title('Calculator')

# output will be show at the top of the GUI
text1 = tk.Text(root)
text1.grid(row=0, column=0, columnspan=3, rowspan=1)

# number buttons 
button0 = tk.Button(root)
button1= tk.Button(root)
button2 = tk.Button(root)
button3 = tk.Button(root)
button4 = tk.Button(root)
button5 = tk.Button(root)
button6= tk.Button(root)
button7 = tk.Button(root)
button8 = tk.Button(root)
button9 = tk.Button(root)
equalsbutton= tk.Button(root)
addbutton= tk.Button(root)
subbutton= tk.Button(root)
divbutton= tk.Button(root)
multbutton= tk.Button(root)

button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)
button0.grid(row=4,column=0)
addbutton.grid(row=4,column=1)
subbutton.grid(row=4,column=2)
equalsbutton.grid(row=5,column=0)
divbutton.grid(row=5,column=1)
multbutton.grid(row=5,column=2)
# keeps the window running
root.mainloop()