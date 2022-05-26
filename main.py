import init
import tkinter as tk
from tkinter import *

from checklist import userPreferences
from datagather import *
#import datagather as dt

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#Try and put this in a function later
selectedBrowser = userPreferences[0]
version = userPreferences[1]
userInfo = []
for i in range(2, len(userPreferences)):
    #Eventually make this load into a dictionary where the key is the site needed and values are user, password
    userInfo.append(userPreferences[i])

print(userInfo)

if init.userFriendly(selectedBrowser, version):
    if version == 1:
        siteAmount = int(len(userInfo)/3)
        for website in range(siteAmount):
            #Var declaration needs to be later or else a list index error will rise
            #username = website+1
            #password = website+2
            print("\n{}th iteration".format(website))
            print(userInfo[website])
            
            if userInfo[website] == "Calculate GPA":
                studentVUE_UF(userInfo[website+siteAmount], userInfo[website+siteAmount+1], webdriver.Chrome(ChromeDriverManager().install()))
            elif userInfo[website] == "List Assignments (Google Classroom)":
                googleClassroom_UF(userInfo[website+1], userInfo[website+siteAmount+2], webdriver.Chrome(ChromeDriverManager().install()))
            elif userInfo[website] == "Check Email":
                emailCheck_UF(userInfo[website+siteAmount], userInfo[website+siteAmount+1], webdriver.Chrome(ChromeDriverManager().install()))
            
        #If there's only one selection:
        #The code below works but is commented out cause it only allows one function to be run
        # if len(userInfo) == 3:
        #     #Will need to find a way to automatically run the corresponding functions for each selection
        #     #Third value passed in function needs to change to be a var so different browsers can actually be used
        #     if userInfo[0] == "Calculate GPA":
        #         studentVUE_UF(userInfo[1], userInfo[2], webdriver.Chrome(ChromeDriverManager().install()))
        #     elif userInfo[0] == "List Assignments (Google Classroom)":
        #         googleClassroom_UF(userInfo[1], userInfo[2], webdriver.Chrome(ChromeDriverManager().install()))
        #     elif userInfo[0] == "Check Email":
        #         emailCheck_UF(userInfo[1], userInfo[2], webdriver.Chrome(ChromeDriverManager().install()))

else:
    print("Using BeautifulSoup for instant data\n")
    #" "
