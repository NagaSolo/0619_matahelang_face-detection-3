import tkinter

def browse_file():
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

window = tkinter.Tk()
window.title('Tukar Muka')
window.geometry('600x400')

label = tkinter.Label(text='Aplikasi menukar rupa paras')
label.grid(column=0, row=0)

label_sumber_explorer = tkinter.Label(text='Sumber imej')
label.grid(column=0, row=0)

button_explore = tkinter.Button(window, text = "Browse Files", command=browse_file)
button_explore.grid(column = 1, row = 2)

button_exit = tkinter.Button(window, text = "Exit", command = exit)
button_exit.grid(column = 1,row = 3)

window.mainloop()