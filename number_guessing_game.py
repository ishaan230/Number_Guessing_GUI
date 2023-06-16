import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random




secretnum = random.randint(0,10000)

def func():
    #get input
    str = enterNumField.get()
    value = int(str)

    if(value==secretnum):
        messagebox.showinfo(title=NONE,message="CONGRATS , YOU GUESSED THE NUM!!!!!")
        exit()
    elif(value<secretnum):
        
        # print("Go Higher!!!\n")
        messagebox.showinfo(title=NONE,message='GO HIGHER!!!')
    elif(value>secretnum):
        messagebox.showinfo(title=NONE,message="Go Lower!!!")

#tk config
root = tk.Tk()

root.configure(background='light yellow')

root.title('Guess the Number')

root.geometry('350x250')

menu = Menu(root)

root.config(menu=menu)

filemenu = Menu(menu)

menu.add_cascade(label='Options', menu=filemenu)

filemenu.add_command(label='Exit', command=root.quit)


#label
enternumber = Label(root, text = "Enter your Guess:",pady = 5)

#entry
enterNumField = Entry(root)

#button
Submit = Button(root, text = "Submit", fg = "Black", command = func)

#padding
enternumber.grid(row = 0 ,column= 2)

enterNumField.grid(row = 3 , column = 2,padx=100,pady=10)

Submit.grid(row = 5, column = 2,pady=5)

mainloop()
