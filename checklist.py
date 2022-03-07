#tkinter structure file
#for now this is only tkinter
from tkinter import *
import tkinter as tk

def directory():

    #Debug version
    print("directory function called")
       
    #tkinter window creation
    #Consider adding padding a lot later in development
    title = Label(window, text="Grade Check Beta 1.0", font=("arial", 25))
    title.grid(row=0, column=1)
    
    print("made title")
    
    #Note that we're currently defaulting to use Chrome, change later
    #First window
    user = Button(window, text = "User friendly", font=("arial", 10), command=lambda:changeVersion())
    instant = Button(window, text = "Instant data", font=("arial", 10), command=lambda:changeVersion())
    user.grid(row=1, column=0)
    instant.grid(row=1, column=2)
    
    print("created buttons")

def changeVersion():
    if version == 0:
        version = 1
        data.append(version)
    else:
        version = 0
        data.append(version)
    