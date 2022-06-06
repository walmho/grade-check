#This .py file should ONLY contain functions (anda import lines)
from selenium import webdriver
import time
#from init import driver

#I feel like this should only be temporary for now. Try installing newer chromedriver version


#Might want to change all URL links to be stored in functions
#UF stands for user-friendly. these functions aren't called for the beautiful soup version.
def newWindow_UF(driver):
    #init is acting weird for calling functions from it. Once again, default the driver to chrome for now
    #init.driver.get("https://www.coolmathgames.com/")
    
    #If this project ever becomes big enough I might make a small website for it just to have something to open as default...
    driver.get("https://google.com")

def googleClassroom_UF(username, password, driver):
    #Opening new tab
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get("https://classroom.google.com/u/0/h")
    
    #logging in
    emailEntry = driver.find_element_by_id("identifierId")
    emailEntry.send_keys(username)
    nextButton = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div")
    nextButton.click()
    
    #To allow for time for the page to load
    time.sleep(3)
    
    #If possible try and go back and use something other than xpath because it's a lot messier, though it is foolproof
    passwordEntry = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
    passwordEntry.send_keys(password)
    nextButton = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div")
    nextButton.click()
    
    #Next to step is to pull data from classroom
    
def studentVUE_UF(username, password, driver):
    #Need to make this more intuitive (so it only switches to a new tab if another window is open, or makes a new one if it's the only command, etc.)
    driver.get("https://google.com")
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get("https://myvue.cascadetech.org/hillsboro/PXP2_Login_Student.aspx?regenerateSessionId=True")
    
    #logging in
    studentLogin = driver.find_element_by_id("ctl00_MainContent_username")
    studentLogin.send_keys(username)
    passwordLogin = driver.find_element_by_id("ctl00_MainContent_password")
    passwordLogin.send_keys(password)
    
    nextButton = driver.find_element_by_id("ctl00_MainContent_Submit1")
    nextButton.click()
    return
    
def emailCheck_UF(username, password, driver):
    #Same intuitive issue with studentVUE
    
    #Need to check to see what domain the email is in; gmail will require different code than outlook
    driver.get("https://outlook.office.com/mail/inbox")
    time.sleep(3)
    #logging in
    emailLogin = driver.find_element_by_id("i0116")
    emailLogin.send_keys(username)
    nextButton = driver.find_element_by_id("idSIButton9")
    nextButton.click()
    time.sleep(3)
    
    passwordEntry = driver.find_element_by_id("i0118")
    passwordEntry.send_keys(password)
    nextButton = driver.find_element_by_id("idSIButton9")
    nextButton.click()
    
    dontStayLogged = driver.find_element_by_id("idBtn_Back")
    dontStayLogged.click()
