#A basic Image Viewer works on only predefined images

from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Image Viewer')
root.iconbitmap('viewer.ico')

#Images
image1 = ImageTk.PhotoImage(Image.open("images/1.jpg"))
image2 = ImageTk.PhotoImage(Image.open("images/2.jpg"))
image3 = ImageTk.PhotoImage(Image.open("images/3.jpg"))
image4 = ImageTk.PhotoImage(Image.open("images/4.jpg"))
image5 = ImageTk.PhotoImage(Image.open("images/5.jpg"))

img_list = [image1, image2, image3, image4, image5]

#First Image on screen
global gb_label
gb_label = Label(image = img_list[0])
gb_label.grid(row=0, column=0, columnspan=3)

#functions
def forward(img_num):
    global gb_label
    global gb_bback
    global gb_bforward
    gb_label.grid_forget()
    gb_label = Label(image = img_list[img_num])

    gb_bforward = Button(root, text='>>', command=lambda:forward(img_num+1))
    gb_bback = Button(root, text='<<', command=lambda:back(img_num-1))

    if img_num==4:
        gb_bforward = Button(root, text='>>', state=DISABLED)  

    gb_label.grid(row=0, column=0, columnspan=3)
    gb_bback.grid(row=1, column=0)
    gb_bforward.grid(row=1, column=2)


def back(img_num):
    global gb_label
    global gb_bback
    global gb_bforward
    
    gb_label.grid_forget()
    gb_label = Label(image = img_list[img_num])

    gb_bforward = Button(root, text='>>', command=lambda:forward(img_num+1))
    gb_bback = Button(root, text='<<', command=lambda:back(img_num-1))

    if img_num==0:
        gb_bback = Button(root, text='<<', state=DISABLED)
    
    gb_label.grid(row=0, column=0, columnspan=3)
    gb_bback.grid(row=1, column=0)
    gb_bforward.grid(row=1, column=2)
    

#-----------------------------------------------------------------
#Creating Buttons
exit_button = Button(root, text='Exit Viewer', command=root.quit)
button_forward = Button(root, text='>>', command=lambda:forward(1))
button_back = Button(root, text='<<', command=back, state=DISABLED)

#Sending on Screen
button_back.grid(row=1, column=0)
exit_button.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()