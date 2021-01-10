import tkinter as tk
from tkinter import ttk

# initializes the window
root = tk.Tk()

# creates window header 
root.title('Calculator')

# output will be show at the top of the GUI
text1 = tk.Text(root,height=1,width=20)
text1.grid(row=0, column=0, columnspan=3,rowspan=1,padx=10,pady=10)

# entry input
entry= tk.Entry(root, text='Input')
entry.grid(row=1,column=0,columnspan=3,rowspan=1,padx=10,pady=10)

# operations 
def button_click(number):
    entry.delete(0,END)
    entry.insert(0,number)
def button_add():
    pass
def button_sub():
    pass
def button_mult():
    pass
def button_div():
    pass
def button_clear():
    pass

# number buttons 
button0 =   tk.Button(root,text = "0",padx=40,pady=20,command=lambda: button_click(0))
button1 =   tk.Button(root,text = "1",padx=40,pady=20,command=lambda: button_click(1))
button2 =   tk.Button(root,text = "2",padx=40,pady=20,command=lambda: button_click(2))
button3 = tk.Button(root,text = "3",padx=40,pady=20,command=lambda: button_click(3))
button4 = tk.Button(root,text = "4",padx=40,pady=20,command=lambda: button_click(4))
button5 = tk.Button(root,text = "5",padx=40,pady=20,command=lambda: button_click(5))
button6= tk.Button(root,text = "6",padx=40,pady=20,command=lambda: button_click(6))
button7 = tk.Button(root,text = "7",padx=40,pady=20,command=lambda: button_click(7))
button8 = tk.Button(root,text = "8",padx=40,pady=20,command=lambda: button_click(8))
button9 = tk.Button(root,text = "9",padx=40,pady=20,command=lambda: button_click(9))
equalsbutton= tk.Button(root,text = "=",padx=40,pady=20,command=lambda: button_equals(1))
addbutton= tk.Button(root,text = "+",padx=40,pady=20,command=lambda: button_add(1))
subbutton= tk.Button(root,text = "-",padx=40,pady=20,command=lambda: button_sub(1))
divbutton= tk.Button(root,text = "/",padx=40,pady=20,command=lambda: button_div(1))
multbutton= tk.Button(root,text = "x",padx=40,pady=20,command=lambda: button_mult(1))
clearbutton=tk.Button(root,text = "CLEAR",padx=115,pady=20,command=lambda: button_clear(1))

button1.grid(row=2,column=0)
button2.grid(row=2,column=1)
button3.grid(row=2,column=2)
button4.grid(row=3,column=0)
button5.grid(row=3,column=1)
button6.grid(row=3,column=2)
button7.grid(row=4,column=0)
button8.grid(row=4,column=1)
button9.grid(row=4,column=2)
button0.grid(row=5,column=0)
addbutton.grid(row=5,column=1)
subbutton.grid(row=5,column=2)
equalsbutton.grid(row=6,column=0)
divbutton.grid(row=6,column=1)
multbutton.grid(row=6,column=2)
clearbutton.grid(row=7,column=0,columnspan=3,rowspan=3)

# keeps the window running
root.mainloop()