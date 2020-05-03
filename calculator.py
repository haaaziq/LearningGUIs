from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.iconbitmap('calc.ico') #Add icon Location

#Entry Field
inp = Entry(root, width = 45, borderwidth = 5)
inp.grid(column = 0, row = 0, columnspan = 4)

#Function
def button_click(num):
    prev = str(inp.get())
    inp.delete(0,END)
    inp.insert(0,prev + str(num))

def button_clear():
    inp.delete(0,END)

def button_add():
    first_number = inp.get()
    global f_num
    global operation
    operation = "add"
    f_num = int(first_number)
    inp.delete(0,END)

def button_subtract():
    first_number = inp.get()
    global f_num
    global operation
    operation = "sub"
    f_num = int(first_number)
    inp.delete(0,END)

def button_multiply():
    first_number = inp.get()
    global f_num
    global operation
    operation = "mul"
    f_num = int(first_number)
    inp.delete(0,END)

def button_divide():
    first_number = inp.get()
    global f_num
    global operation
    operation = "div"
    f_num = int(first_number)
    inp.delete(0,END)


def button_equal():
    second_num = inp.get()
    inp.delete(0,END)

    if operation == "add":
        inp.insert(0,f_num+int(second_num))

    if operation == "sub":
        inp.insert(0,f_num-int(second_num))

    if operation == "mul":
        inp.insert(0,f_num*int(second_num))

    if operation == "div":
        inp.insert(0,f_num/int(second_num))


#Creating Buttons
button_1 = Button(root, text = "1", padx = 30, pady = 20, command = lambda: button_click(1))
button_2 = Button(root, text = "2", padx = 30, pady = 20, command = lambda: button_click(2))
button_3 = Button(root, text = "3", padx = 30, pady = 20, command = lambda: button_click(3))
button_4 = Button(root, text = "4", padx = 30, pady = 20, command = lambda: button_click(4))
button_5 = Button(root, text = "5", padx = 30, pady = 20, command = lambda: button_click(5))
button_6 = Button(root, text = "6", padx = 30, pady = 20, command = lambda: button_click(6))
button_7 = Button(root, text = "7", padx = 30, pady = 20, command = lambda: button_click(7))
button_8 = Button(root, text = "8", padx = 30, pady = 20, command = lambda: button_click(8))
button_9 = Button(root, text = "9", padx = 30, pady = 20, command = lambda: button_click(9))
button_0 = Button(root, text = "0", padx = 30, pady = 20, command = lambda: button_click(0))

button_addition = Button(root, text = "+", padx = 30, pady = 54, command = button_add)
button_equal_to = Button(root, text = "=", padx = 67, pady = 20, command = button_equal)
button_clr = Button(root, text = "Clear", padx = 56.5, pady = 20, command = button_clear)
button_sub = Button(root, text = "-", padx = 30, pady = 52, command = button_subtract)
button_mul = Button(root, text = "*", padx = 30, pady = 20, command = button_multiply)
button_div = Button(root, text = "/", padx = 30, pady = 20, command = button_divide)

#Adding Buttons to screen
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_0.grid(row=5, column=0)

button_addition.grid(row=4, column=3, rowspan = 2)
button_equal_to.grid(row=5, column=1, columnspan=2)
button_clr.grid(row=1, column=0, columnspan=2)
button_sub.grid(row=2, column=3, rowspan =2)
button_mul.grid(row=1, column=3)
button_div.grid(row=1, column=2)

root.mainloop()
