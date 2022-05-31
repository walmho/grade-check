import init
import tkinter as tk
from tkinter import *

from checklist import userPreferences
from datagather import *
#As in, safety net
from checklist import raiseError
#import datagather as dt

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException

#Try and put this in a function later
selectedBrowser = userPreferences[0]
version = userPreferences[1]

userInfo = []
for i in range(2, len(userPreferences)):
    userInfo.append(userPreferences[i])
   
siteAmount = int(len(userInfo)/3)

newInfo = []
newUser = []
for i in range(siteAmount):
    #No problems with appending the websites in the correct order
    website = userInfo[i]
    newInfo.append(website)

for j in range(siteAmount, len(userInfo), 2):
    username = userInfo[j]
    password = userInfo[j+1]
    
    newUser.append([username, password])

compiledData = {}
for k in range(len(newInfo)):
    compiledData[newInfo[k]] = newUser[k]

if init.userFriendly(selectedBrowser, version):
    if version == 1:
        for website in range(siteAmount):
            #Right now this is using chrome and not referencing the version variable in userPreferences
            if newInfo[website] == "Calculate GPA":
                #This error won't even raise because studentvue displays user and password on the same webpage. Nothing will happen until more is added to the function to get it to scrape data
                try:
                    studentVUE_UF(compiledData[newInfo[website]][0], compiledData[newInfo[website]][1], webdriver.Chrome(ChromeDriverManager().install()))
                
                except WebDriverException:
                    raiseError()
                    driver.quit()

            elif newInfo[website] == "List Assignments (Google Classroom)":
                try:
                    googleClassroom_UF(compiledData[newInfo[website]][0], compiledData[newInfo[website]][1], webdriver.Chrome(ChromeDriverManager().install()))
                
                except WebDriverException:
                    raiseError()
                    driver.quit()

            elif userInfo[website] == "Check Email":
                try:
                    emailCheck_UF(compiledData[newInfo[website]][0], compiledData[newInfo[website]][1], webdriver.Chrome(ChromeDriverManager().install()))
                
                except WebDriverException:
                    raiseError()
                    driver.quit()

else:
    print("Using BeautifulSoup for instant data\n")
