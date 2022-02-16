import matplotlib
import selenium
import numpy as np
from selenium import webdriver
#import BeautifulSoup

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
            driver.get("https://stackoverflow.com/questions/66018451/how-to-get-the-chromedriver-automatically-updated-through-python-selenium-after")
        elif browser == ("Firefox"):
            driver = webdriver.Firefox()
        elif browser == ("Safari"):
            driver = webdriver.safari()
    elif version == 2:
        print("Soup verison pending")

