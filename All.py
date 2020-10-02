import jervis
#import  tkinter as TK
from tkinter import *
import subprocess

import os
def done():
    print('dfcbvn')
#    subprocess.call('python jervis.py', shell=True)
    print(os.getcwd())
    os.system('python jervis.py')
def done1():
    os.system('python first.py')

if __name__== '__main__':
    root=Tk()
    root.title('All in one')
    root.geometry('400x300')
#    menubar=Menu(root)
#    file=Menu(menubar, tearoff=0)
#    file.add_command(label='Run', command=done)
#    menubar.add_cascade(label='file', menu=file)
    mainframe = Frame(root)
    mainframe.grid(column=0, row=0)
    btn1 = Button(mainframe, text = 'Jervis for speech recognization !', bd = '5', command = done)     
    btn1.grid(column=1, row=5)
    btn2= Button(mainframe, text = 'Youtube video downloader' , bd = '5', command = done1) 
    btn3 = Button(mainframe, text = 'Close !', bd = '5', command = root.destroy) 
    btn2.grid (column=3, row=5)
    btn3.grid(column=9, row=5)
#    t=Text(mainframe, height=30, width=50)
#    t.grid(column=7, row=20)
#   root.config(menu=menubar)
    #root.resizable(True, True)
    root.mainloop()