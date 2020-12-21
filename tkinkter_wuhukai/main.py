import tkinter

def browse_sumber_image():
    from tkinter import filedialog
    filename = filedialog.askopenfilename(
        initialdir = "/",
        title = "Pilih sumber imej",
        filetypes = (
            ("jpg files", "*.jpg*"), 
            ("all files", "*.*")
        )) 
       
    # Change label contents 
    label_sumber_explorer.configure(text="Imej untuk sumber dipilih: "+filename)

def browse_driving_image():
    from tkinter import filedialog
    filename = filedialog.askopenfilename(
        initialdir = "/",
        title = "Pilih sumber imej",
        filetypes = (
            ("jpg files", "*.jpg*"), 
            ("all files", "*.*")
        )) 
       
    # Change label contents 
    label_driving_explorer.configure(text="Imej untuk sumber dipilih: "+filename)

window = tkinter.Tk()
window.title('Tukar Muka')
window.geometry('600x400')

label = tkinter.Label(text='Aplikasi menukar rupa paras')
label.grid(column=1, row=0)

label_sumber_explorer = tkinter.Label(text='Sumber imej')
label_sumber_explorer.grid(column=1, row=0)

button_sumber_explore = tkinter.Button(window, text = "Browse imej sebagai sumber", command=browse_sumber_image)
button_sumber_explore.grid(column = 1, row = 2)

button_sumber_exit = tkinter.Button(window, text = "Exit", command = exit)
button_sumber_exit.grid(column = 1,row = 3)

label_driving_explorer = tkinter.Label(text='Driving imej')
label_driving_explorer.grid(column=1, row=5)

button_driving_explore = tkinter.Button(window, text = "Browse imej sebagai driver", command=browse_driving_image)
button_driving_explore.grid(column=1, row = 6)

button_driving_exit = tkinter.Button(window, text = "Exit", command = exit)
button_driving_exit.grid(column=1,row = 7)

window.mainloop()