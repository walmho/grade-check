import matplotlib
import selenium
import numpy as np
from selenium import webdriver
import tkinter as tk
from tkinter import *
#import BeautifulSoup

#Imagine having messy comments

def userFriendly(browser, version):
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
