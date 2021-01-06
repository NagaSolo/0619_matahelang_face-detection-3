from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

import cv2

from face_det import select_face
from face_swa import face_swap

root = Tk()
root.geometry("550x300+300+150")
root.resizable(width=True, height=True)

left_frame = Frame(root)
left_frame.pack(side=LEFT)

right_frame = Frame(root)
right_frame.pack(side=RIGHT)

bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM)

sumber_path = []
target_path = []
args = {}

def openfn():
    filename = filedialog.askopenfilename(title='open')
    return filename

def open_img_sumber(sumber_path=sumber_path):
    x = openfn()

    sumber_path = sumber_path.append(x)

    img = Image.open(x)
    img = img.resize((250, 350), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(left_frame, image=img)
    panel.image = img
    panel.pack()
    name = Label(left_frame, text=x)
    name.pack(side=BOTTOM)

Button(left_frame, text='Pilih Imej Sumber', command=open_img_sumber).pack(side=TOP)

def open_img_target(target_path=target_path):
    x = openfn()

    target_path = target_path.append(x)

    img = Image.open(x)
    img = img.resize((250, 350), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(right_frame, image=img)
    panel.image = img
    panel.pack()
    name = Label(right_frame, text=x)
    name.pack(side=BOTTOM)

Button(right_frame, text='Pilih Imej Target', command=open_img_target).pack(side=TOP)

def face_hug(args=args):
    # Read images
    src_img = cv2.imread(sumber_path[0])
    dst_img = cv2.imread(target_path[0])

    # Select src face
    src_points, src_shape, src_face = select_face(src_img)
    # Select dst face
    dst_points, dst_shape, dst_face = select_face(dst_img)

    if src_points is None or dst_points is None:
        print('Detect 0 Face !!!')
        exit(-1)

    output = face_swap(src_face, dst_face, src_points, dst_points, dst_shape, dst_img, args)

    args['out'] = 'results/result.jpg'

    dir_path = os.path.dirname(args['out'])
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)

    cv2.imwrite(args['out'], output)

    args['no_debug_window'] = False

    ##For debug
    if not args['no_debug_window']:
        cv2.imshow("From", dst_img)
        cv2.imshow("To", output)
        cv2.waitKey(0)
        
        cv2.destroyAllWindows()

def get_selection(args=args):
    if (col_cor.get() == 1) & (warp_2d.get() == 0):
        args['correct_color'] = 1
    elif (col_cor.get() == 0) & (warp_2d.get() == 1):
        args['warp_2d'] = 1
    elif (col_cor.get() == 0) & (warp_2d.get() == 0):
        args = {}
    else:
        args['correct_color'] = 1
        args['warp_2d'] = 1

col_cor = IntVar()
warp_2d = IntVar()
Checkbutton(bottom_frame, text='Ubahsuai Warna/Color Correction', variable=col_cor, onvalue=1, offvalue=0, command=get_selection).pack(side=TOP)
Checkbutton(bottom_frame, text='Warp 2D', variable=warp_2d, onvalue=1, offvalue=0, command=get_selection).pack(side=TOP)
Button(bottom_frame, text='Hasilkan imej gabungan', command=face_hug).pack(side=TOP)

root.mainloop()