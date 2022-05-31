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

# print(userInfo)
# print("\n\n")
# print(compiledData)
# print("\n")

if init.userFriendly(selectedBrowser, version):
    if version == 1:
        for website in range(siteAmount):
            #Right now this is using chrome and not referencing the version variable in userPreferences
            if newInfo[website] == "Calculate GPA":
                studentVUE_UF(compiledData[newInfo[website]][0], compiledData[newInfo[website]][1], webdriver.Chrome(ChromeDriverManager().install()))
            elif newInfo[website] == "List Assignments (Google Classroom)":
                googleClassroom_UF(compiledData[newInfo[website]][0], compiledData[newInfo[website]][1], webdriver.Chrome(ChromeDriverManager().install()))
            elif userInfo[website] == "Check Email":
                emailCheck_UF(compiledData[newInfo[website]][0], compiledData[newInfo[website]][1], webdriver.Chrome(ChromeDriverManager().install()))

else:
    print("Using BeautifulSoup for instant data\n")
