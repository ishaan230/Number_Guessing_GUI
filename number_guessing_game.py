import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random



def func():
    global enterNumField
    #get input
    str = enterNumField.get()
    value = int(str)

    if(value==secretnum):
        messagebox.showinfo(title=NONE,message="CONGRATS , YOU GUESSED THE NUM!!!!!")
        choice = messagebox.askyesno(title='Play Again?',message='Do you want to play again?')
        if(choice):
            restart()
        else:
            exit()
    elif(value<secretnum):
        # print("Go Higher!!!\n")
        messagebox.showinfo(title=NONE,message='GO HIGHER!!!')
        enterNumField.delete(0,END)
    elif(value>secretnum):
        messagebox.showinfo(title=NONE,message="Go Lower!!!")
        enterNumField.delete(0,END)


def start():
    global enterNumField
    global secretnum
    global root
    
    secretnum = random.randint(0,1000)

    #tk config
    root = tk.Tk()

    root.configure(background='light yellow')

    root.title('Guess the Number')

    root.geometry('600x400')

    menu = Menu(root)

    root.config(menu=menu)

    filemenu = Menu(menu)

    menu.add_cascade(label='Options', menu=filemenu)

    filemenu.add_command(label='Restart', command=restart)
    filemenu.add_command(label='Exit', command=root.quit)


    #label
    enternumber = Label(root, text = "Enter your Guess:",pady = 5)

    #entry
    enterNumField = Entry(root)

    #button
    Submit = Button(root, text = "Submit", fg = "Black", command = func)

    #padding
    enternumber.grid(padx=(230,0), pady=(100,0))

    enterNumField.grid(padx=(230,0),pady=(20,0))

    Submit.grid(padx=(230,0),pady=(20,0))

    mainloop()
def restart():
    root.destroy()
    start()

start()
