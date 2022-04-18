"""
Purpose of this file is to be the actual scraper that gathers data from sites and inputs
into variables to be used in main.py for final analysis and display with matplotlib. file will
intake requested data from init.py and be used in main.py (I hope)

""" 

#This .py file should ONLY contain functions (anda import lines)
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

#I feel like this should only be temporary for now. Try installing newer chromedriver version
driver = webdriver.Chrome(ChromeDriverManager().install())

#Might want to change all URL links to be stored in functions
def newWindow():
    #init is acting weird for calling functions from it. Once again, default the driver to chrome for now
    #init.driver.get("https://www.coolmathgames.com/")
    driver.get("https://google.com")

def googleClassroom(username, password):
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get("https://classroom.google.com/u/0/h")
    
    
    
    
newWindow()
googleClassroom("not needed", "right now")
time.sleep(3)
driver.quit()
