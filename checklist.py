#tkinter structure file
#for now this is only tkinter; create specific functions later
from tkinter import *
import tkinter as tk

userPreferences = []

rootWindow = tk.Tk()

#tkinter window creation
#Consider adding padding a lot later in development
title = Label(rootWindow, text="Grade Check Beta 1.0", font=("arial", 25))
title.grid(row=0, column=1)

#First window
user = Button(rootWindow, text = "User friendly", font=("arial", 10), command=lambda:(userPreferences.append(1)))
instant = Button(rootWindow, text = "Instant data", font=("arial", 10), command=lambda:(userPreferences.append(2)))
user.grid(row=1, column=0)
instant.grid(row=1, column=2)

#Browser is being returned first despite being appended later due to lambda
browser = "Chrome"
userPreferences.append(browser)
        
rootWindow.mainloop()
    