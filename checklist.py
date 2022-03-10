#tkinter structure file
#for now this is only tkinter; create specific functions later
from tkinter import *
import tkinter as tk

userPreferences = [0, 0]

rootWindow = tk.Tk()
rootWindow.title("Grade Check Beta")

#tkinter window creation
#Consider adding padding a lot later in development
title = Label(rootWindow, text="Grade Check Beta 1.0", font=("arial", 25))
title.grid(row=0, column=1)

welcome = """Welcome to Grade Check Beta, the multi-purpose program for school.
             This program will one day calculate your GPA, locate missing assignments,
             and quickly open up the neccesarry programs you use every day.
"""

#Edit as needed and project evolves
tutorial = """To use this program, first select your browser and which version of this
              program you want to use. 'User friendly' will load your web pages right in 
              front of you, while 'Instant Data' will do everything off-screen and return
              all the data in a nice and neat way. Note that User friendly takes longer.
              
              Once you've selected your version and browser, a new window wil pop up. Check
              each option you'd like and then hit enter. Please be patient, your data will
              return soon.
"""
def toggle(version):
    if version == 1:
        user.configure(bg="green")
        instant.configure(bg="white smoke")

    elif version == 2:
        instant.configure(bg="green")
        user.configure(bg="white smoke")
    
    userPreferences[1] = version

def loadHelp():
    helpMe = Button(rootWindow, text="?", font=("arial", 15), command=helpPlease)
    helpMe.grid(row=3, column=0)

def chooseVersion():
    global user
    user = Button(rootWindow, text="User friendly", font=("arial", 10), command=lambda:toggle(1))
    global instant
    instant = Button(rootWindow, text = "Instant data", font=("arial", 10), command=lambda:toggle(2))
    user.grid(row=3, column=1)
    instant.grid(row=3, column=2)

def pickBrowser():
    descriptor = Label(rootWindow, text="Choose browser: ", font=("arial", 10))
    descriptor.grid(row=1, column=0)
    
    supportedBrowsers = ["Chrome", "Safari", "Firefox"]
    global selectionBox 
    selectionBox = Listbox(rootWindow, listvariable=supportedBrowsers, selectmode="single", )

    for browser in range(len(supportedBrowsers)):
        selectionBox.insert(browser+1, supportedBrowsers[browser])
    
    selectionBox.grid(row=2, column=0)

    global chosenBrowser
    chosenBrowser = selectionBox.get(ACTIVE)
    
    #Add a series of statements to check and make sure userPreferences have been filled properly
    nextWindow = Button(rootWindow, text="Next", font=("arial", 10), command=chooseOptions)
    nextWindow.grid(row=0, column=2)
    
def helpPlease():
    helpWindow = tk.Toplevel(rootWindow)
    helpWindow.title("Help")
    
    overview = Label(helpWindow, text=welcome, font=("arial", 10))
    overview.grid(row=0, column=0)
    windowTutorial = Label(helpWindow, text=tutorial, font=("arial", 10))
    windowTutorial.grid(row=1, column=0)
    
def chooseOptions():
    userPreferences[0] = selectionBox.get(ACTIVE)
    print(userPreferences)
    secondaryWindow = tk.Toplevel(rootWindow)
    secondaryWindow.title("Grade Check Beta")
    
    info = Label(secondaryWindow, text="Select what you would like to find: ", font=("arial", 10))
    info.grid(row=0, column=0)

loadHelp()
chooseVersion()
pickBrowser()

rootWindow.mainloop()
    