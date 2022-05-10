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
#UF stands for user-friendly. these functions aren't called for the beautiful soup version.
def newWindow_UF():
    #init is acting weird for calling functions from it. Once again, default the driver to chrome for now
    #init.driver.get("https://www.coolmathgames.com/")
    
    #If this project ever becomes big enough I might make a small website for it just to have something to open as default...
    driver.get("https://google.com")

def googleClassroom_UF(username, password):
    #Opening new tab
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get("https://classroom.google.com/u/0/h")
    
    #logging in
    emailEntry = driver.find_element_by_id("identifierId")
    emailEntry.send_keys(username)
    nextButton = driver.find_element_by_class_name("VfPpkd-vQzf8d")
    nextButton.click()
    
    #Throw in some exceptions here if it's a non-google account
    
    #passwordEntry = driver.find_element_by_id()
    
newWindow_UF()
googleClassroom_UF("jones.ryan.t.01@gmail.com", "right now")
time.sleep(10)
driver.quit()
