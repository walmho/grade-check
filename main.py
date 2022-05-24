import init
import tkinter as tk
from tkinter import *

from checklist import userPreferences
import datagather as dt

print(userPreferences)

#Try and put this in a function later
selectedBrowser = userPreferences[0]
version = userPreferences[1]
userInfo = []
for i in range(2, len(userPreferences)-1):
    #Eventually make this load into a dictionary where the key is the site needed and values are user, password
    userInfo.append(userPreferences[i])

print(userInfo)

if init.userFriendly(selectedBrowser, version):
    if version == 1:
        if userInfo[0] == "StudentVUE":
            dt.studentVUE_UF(userInfo[1], userPreferences[2], version)
else:
    print("Using BeautifulSoup for instant data\n")
    #" "

print(userPreferences)
