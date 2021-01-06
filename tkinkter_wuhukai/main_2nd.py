from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

root = Tk()
root.geometry("550x300+300+150")
root.resizable(width=True, height=True)

left_frame = Frame(root)
left_frame.pack(side=LEFT)

right_frame = Frame(root)
right_frame.pack(side=RIGHT)

def openfn():
    filename = filedialog.askopenfilename(title='open')
    return filename

def open_img_sumber():
    x = openfn()
    img = Image.open(x)
    img = img.resize((250, 350), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(left_frame, image=img)
    panel.image = img
    panel.pack()
    name = Label(left_frame, text=x)
    name.pack(side=BOTTOM)

Button(left_frame, text='Pilih Imej Sumber', command=open_img_sumber).pack(side=TOP)

def open_img_target():
    x = openfn()
    img = Image.open(x)
    img = img.resize((250, 350), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(right_frame, image=img)
    panel.image = img
    panel.pack()
    name = Label(right_frame, text=x)
    name.pack(side=BOTTOM)

Button(right_frame, text='Pilih Imej Target', command=open_img_target).pack(side=TOP)

root.mainloop()