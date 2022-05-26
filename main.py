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

#My sorry attempt at a sorting algorithm
userInfo = []
for i in range(2, len(userPreferences)):
    #Eventually make this load into a dictionary where the key is the site needed and values are user, password
    userInfo.append(userPreferences[i])
   
siteAmount = int(len(userInfo)/3)
print(siteAmount)

newInfo = []
newUser = []
for i in range(siteAmount):
    #No problems with appending the websites in the correct order
    website = userInfo[i]
    newInfo.append(website)

print(newInfo)

for j in range(siteAmount, len(userInfo)-siteAmount, 2):
    username = userInfo[j]
    password = userInfo[j+1]
    
    newUser.append([username, password])

print(userInfo)
print("\n\n")
print(newInfo)
print(newUser)

if init.userFriendly(selectedBrowser, version):
    if version == 1:
        for website in range(siteAmount):
            #siteAmount -= website
            #print("\n{}th iteration".format(website))
            #print(userInfo[website])
            
            if newInfo[website] == "Calculate GPA":
                studentVUE_UF(userInfo[website+siteAmount], userInfo[website+siteAmount+1], webdriver.Chrome(ChromeDriverManager().install()))
            elif newInfo[website] == "List Assignments (Google Classroom)":
                googleClassroom_UF(userInfo[website+siteAmount+siteAmount], userInfo[website+siteAmount+1], webdriver.Chrome(ChromeDriverManager().install()))
            elif userInfo[website] == "Check Email":
                emailCheck_UF(userInfo[website+siteAmount], userInfo[website+siteAmount+1], webdriver.Chrome(ChromeDriverManager().install()))

else:
    print("Using BeautifulSoup for instant data\n")
