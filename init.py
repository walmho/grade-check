import matplotlib
import selenium
import numpy as np
from selenium import webdriver
import tkinter as tk
from tkinter import *
#import BeautifulSoup

#tkinter window creation
window = tk.Tk()
window.title("Grade Check Beta")
#Consider adding padding a lot later in development
title = Label(window, text="Grade Check Beta 1.0", font=("arial", 25))
title.grid(row=0, column=1)

#Note that we're currently defaulting to use Chrome, change later
user = Button(window, text = "User friendly", font=("arial", 10), command=lambda:directory(1, "Chrome"))
instant = Button(window, text = "Instant data", font=("arial", 10), command=lambda:directory(2, None))
user.grid(row=1, column=0)
instant.grid(row=1, column=2)

def userVersion():
    if str(input("User friendly version? (y/n) ")).lower() == "y":
        return True
    else:
        return
    
def directory(version, browser):
    if version == 1:
        #Change to include different browsers later (if browser = Firefox driver = webdriver.Chrome)
        if browser == ("Chrome"):
            driver = webdriver.Chrome()
            #Note that an InvalidArgumentException might be due to a faulty website link
            #Currently using test site
            driver.get("https://stackoverflow.com/questions/66018451/how-to-get-the-chromedriver-automatically-updated-through-python-selenium-after")
        elif browser == ("Firefox"):
            driver = webdriver.Firefox()
        elif browser == ("Safari"):
            driver = webdriver.safari()
    elif version == 2:
        print("Soup verison pending")

window.mainloop()
