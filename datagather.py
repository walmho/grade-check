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
    
    #To allow for time for the page to load
    time.sleep(3)
    
    gmailDomain = "@gmail.com"
    if gmailDomain not in email:
        #login again in the outlook portal. Change this code to narrow down which domain specifically is being used.
        #code currently only supports @hsd and @gmail
        emailEntry = driver.find_element_by_id("i0116")
        emailEntry.send_keys(email)
        nextButton = driver.find_element_by_id("idSIButton9")
        nextButton.click()
        
        time.sleep(3)
        
        passwordEntry = driver.find_element_by_id("i0118")
        passwordEntry.send_keys(password)
        nextButton = driver.find_element_by_id("idSIButton9")
        nextButton.click()
        
        #find better var name - clicking on the "no" button when asked if the code would like to stay signed in
        noLoginStay = driver.find_element_by_id("idBtn_Back")
        noLoginStay.click()
        
        time.sleep(4)
        
        verify = driver.find_element_by_class_name("VfPpkd-vQzf8d")
        verify.click()
   
newWindow_UF()
googleClassroom_UF("joner689@hsd.k12.or.us", "PASSWORDWOULDBEHERE!")
