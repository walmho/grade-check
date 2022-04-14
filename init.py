#import matplotlib
#import selenium
#import numpy as np
import tkinter as tk
from tkinter import *
#import BeautifulSoup

#Imagine having messy comments

def userFriendly(selectedBrowser, version):
    if version == 1:
    #Change to include different browsers later (if browser = Firefox driver = webdriver.Chrome)
        if selectedBrowser == ("Chrome"):
            #driver = webdriver.Chrome()
            #Note that an InvalidArgumentException might be due to a faulty website link
            #Currently using test site
            #driver.get("https://stackoverflow.com/questions/66018451/how-to-get-the-chromedriver-automatically-updated-through-python-selenium-after")
            #Also include try and except in case user is offline
            print("Offline")
            return True
            
        # elif selectedBrowser == ("Firefox"):
        #     driver = webdriver.Firefox()
        # elif selectedBrowser == ("Safari"):
        #     driver = webdriver.safari()
        # elif selectedBrowser == ("Edge"):
        #     driver = webdriver.edge()

    elif version == 2:
        print("Soup verison pending")
