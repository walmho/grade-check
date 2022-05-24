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

    #print(userInfo)

if init.userFriendly(selectedBrowser, version):
    if version == 1:
        #Will need to find a way to automatically run the corresponding functions for each selection
        if userInfo[0] == "Calculate GPA":
            studentVUE_UF(userInfo[1], userInfo[2], webdriver.Chrome(ChromeDriverManager().install()))
else:
    print("Using BeautifulSoup for instant data\n")
    #" "
