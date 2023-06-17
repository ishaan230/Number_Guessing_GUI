import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random

attempt = 0

def func():
    global attempt
    global enterNumField
    #get input
    str = enterNumField.get()
    value = int(str)
    attempt = attempt + 1
    if(value==secretnum):
        messagebox.showinfo(title=NONE,message=f"CONGRATS , YOU GUESSED THE NUMBER IN {attempt} TRYS!!!!!")
        choice = messagebox.askyesno(title='Play Again?',message='Do you want to play again?')
        if(choice):
            restart()
        else:
            messagebox.showinfo(title=NONE,message=f"THANKS FOR PLAYING,SEE YA!")
            exit()
    elif(value<secretnum):
        # print("Go Higher!!!\n")
        messagebox.showinfo(title=NONE,message=f'GO HIGHER!!!')
        enterNumField.delete(0,END)
    elif(value>secretnum):
        messagebox.showinfo(title=NONE,message=f"GO LOWER!!!")
        enterNumField.delete(0,END)


def start():
    global enterNumField
    global secretnum
    global root
    
    # secretnum = random.randint(0,1000)
    secretnum = 560

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
    global attempt
    attempt = 0
    root.destroy()
    root.quit()
    start()

start()
