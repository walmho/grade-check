#tkinter structure file
#for now this is only tkinter; create specific functions later
from tkinter import *
import tkinter as tk

userPreferences = []

rootWindow = tk.Tk()
rootWindow.title("Grade Check Beta")

#tkinter window creation
#Consider adding padding a lot later in development
title = Label(rootWindow, text="Grade Check Beta 1.0", font=("arial", 25))
title.grid(row=0, column=1)

def chooseVersion():
    user = Button(rootWindow, text = "User friendly", font=("arial", 10), command=lambda:(userPreferences.append(1)))
    instant = Button(rootWindow, text = "Instant data", font=("arial", 10), command=lambda:(userPreferences.append(2)))
    user.grid(row=1, column=1)
    instant.grid(row=1, column=2)

def pickBrowser():
    supportedBrowsers = ["Chrome", "Safari", "Firefox"]
    selectionBox = Listbox(rootWindow, listvariable=supportedBrowsers, selectmode="single", )
    for browser in range(len(supportedBrowsers)):
        selectionBox.insert(browser+1, supportedBrowsers[browser])
    selectionBox.grid(row=1, column=0)
    chosenBrowser = selectionBox.get(ACTIVE)
    userPreferences.append(chosenBrowser)


chooseVersion()
pickBrowser()

rootWindow.mainloop()
    