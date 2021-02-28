from tkinter import *

# creating the window
window = Tk()
window.title("Calculator")

#creating the entry box
entry = Entry(window,width=35,font="none 18")
entry.grid(row=0,column=0,columnspan=4)

previous_num = 0
option = 0

def click(nr):
    '''
    Function which displays the number pressed in the entry box.
    nr - integer number
    '''
    current = entry.get()
    entry.delete(0,END)
    entry.insert(0,str(current) + str(nr))

def clear():
    '''
    Function which clears the entry box.
    '''
    entry.delete(0,END)

def equal():
    '''
    Function which does the specific operation based on the option selected before.
    Displays the result in the entry box.
    '''
    global previous_num,option
    current = int(entry.get())
    entry.delete(0,END)
    if option == "add":
        entry.insert(0,str(previous_num + current))
    elif option == "sub":
        entry.insert(0,str(previous_num - current))
    elif option == "mul":
        entry.insert(0,str(previous_num * current))
    elif option == "div":
        entry.insert(0,str(previous_num / current))

def add():
    '''
    Function which prepares the result for addition.
    '''
    global previous_num,option
    previous_num = int(float(entry.get()))
    option = "add"
    entry.delete(0,END)

def sub():
    '''
    Function which prepares the result for substraction.
    '''
    global previous_num,option
    previous_num = int(float(entry.get()))
    option = "sub"
    entry.delete(0,END)

def mul():
    '''
    Function which prepares the result for multiplication.
    '''
    global previous_num,option
    previous_num = int(float(entry.get()))
    option = "mul"
    entry.delete(0,END)

def div():
    '''
    Function which prepares the result for division.
    '''
    global previous_num,option
    previous_num = int(float(entry.get()))
    option = "div"
    entry.delete(0,END)

# creating the number buttons

button_1 = Button(window,text="1",command=lambda: click(1),padx=20,pady=20,width=5,font="none 20 bold")
button_1.grid(row=1,column=0)
button_2 = Button(window,text="2",command=lambda: click(2),padx=20,pady=20,width=4,font="none 20 bold")
button_2.grid(row=1,column=1)
button_3 = Button(window,text="3",command=lambda: click(3),padx=20,pady=20,width=4,font="none 20 bold")
button_3.grid(row=1,column=2)
button_4 = Button(window,text="4",command=lambda: click(4),padx=20,pady=20,width=5,font="none 20 bold")
button_4.grid(row=2,column=0)
button_5 = Button(window,text="5",command=lambda: click(5),padx=20,pady=20,width=4,font="none 20 bold")
button_5.grid(row=2,column=1)
button_6 = Button(window,text="6",command=lambda: click(6),padx=20,pady=20,width=4,font="none 20 bold")
button_6.grid(row=2,column=2)
button_7 = Button(window,text="7",command=lambda: click(7),padx=20,pady=20,width=5,font="none 20 bold")
button_7.grid(row=3,column=0)
button_8 = Button(window,text="8",command=lambda: click(8),padx=20,pady=20,width=4,font="none 20 bold")
button_8.grid(row=3,column=1)
button_9 = Button(window,text="9",command=lambda: click(9),padx=20,pady=20,width=4,font="none 20 bold")
button_9.grid(row=3,column=2)
button_0 = Button(window,text="0",command=lambda: click(0),padx=20,pady=20,width=4,font="none 20 bold")
button_0.grid(row=1,column=3)

# creating the functional buttons

button_add = Button(window,text="+",command=add,padx=20,pady=20,width=4,font="none 20 bold")
button_add.grid(row=2,column=3)
button_sub = Button(window,text="-",command=sub,padx=20,pady=20,width=4,font="none 20 bold")
button_sub.grid(row=3,column=3)
button_clear = Button(window,text="Clear",command=clear,padx=20,pady=20,font="none 20 bold")
button_clear.grid(row=4,column=0)
button_mul = Button(window,text="*",command=mul,padx=20,pady=20,width=4,font="none 20 bold")
button_mul.grid(row=4,column=1)
button_div = Button(window,text="/",command=div,padx=20,pady=20,width=4,font="none 20 bold")
button_div.grid(row=4,column=2)
button_eq = Button(window,text="=",command=equal,padx=20,pady=20,width=4,font="none 20 bold")
button_eq.grid(row=4,column=3)

# running the main app
window.mainloop()