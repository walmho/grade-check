import matplotlib
import selenium
import numpy as np
from selenium import webdriver
import tkinter as tk
from tkinter import *
#import BeautifulSoup

data = []
    
window = tk.Tk()
window.title("Grade Check Beta")

def userFriendly(version):
    if version == 1:
    #Change to include different browsers later (if browser = Firefox driver = webdriver.Chrome)
        if browser == ("Chrome"):
            #driver = webdriver.Chrome()
            #Note that an InvalidArgumentException might be due to a faulty website link
            #Currently using test site
            #driver.get("https://stackoverflow.com/questions/66018451/how-to-get-the-chromedriver-automatically-updated-through-python-selenium-after")
            #Also include try and except in case user is offline
            print("Offline")
            return True
            
        elif browser == ("Firefox"):
            driver = webdriver.Firefox()
        elif browser == ("Safari"):
            driver = webdriver.safari()
    elif version == 2:
        print("Soup verison pending")

def directory():        
    #tkinter window creation
    #Consider adding padding a lot later in development
    title = Label(window, text="Grade Check Beta 1.0", font=("arial", 25))
    title.grid(row=0, column=1)
    
    #Note that we're currently defaulting to use Chrome, change later
    #First window
    user = Button(window, text = "User friendly", font=("arial", 10), command=lambda:changeVersion())
    instant = Button(window, text = "Instant data", font=("arial", 10), command=lambda:changeVersion())
    user.grid(row=1, column=0)
    instant.grid(row=1, column=2)

def changeVersion():
    if version == 0:
        version = 1
        data.append(version)
    else:
        version = 0
        data.append(version)
    

window.mainloop()
