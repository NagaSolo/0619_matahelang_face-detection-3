from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

root = Tk()
root.geometry("550x300+300+150")
root.resizable(width=True, height=True)

def openfn():
    filename = filedialog.askopenfilename(title='open')
    return filename

def open_img_sumber():
    x = openfn()
    img = Image.open(x)
    img = img.resize((250, 350), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.pack()
    name = Label(root, text=x)
    name.pack()

def open_img_target():
    x = openfn()
    img = Image.open(x)
    img = img.resize((250, 350), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.pack()
    name = Label(root, text=x)
    name.pack()

Button(root, text='Pilih Imej Sumber', command=open_img_sumber).pack()

Button(root, text='Pilih Imej Target', command=open_img_target).pack()
root.mainloop()