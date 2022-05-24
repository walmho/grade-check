import init
import tkinter as tk
from tkinter import *

from checklist import userPreferences
from datagather import *
#import datagather as dt

print(userPreferences)

#Try and put this in a function later
selectedBrowser = userPreferences[0]
version = userPreferences[1]
userInfo = []
for i in range(2, len(userPreferences)):
    #Eventually make this load into a dictionary where the key is the site needed and values are user, password
    userInfo.append(userPreferences[i])

print(userInfo)

if init.userFriendly(selectedBrowser, version):
    print("\nconfirmed browser was selected (chrome)")
    if version == 1:
        print("\nbrowser is Chrome")
        print("{} is current value compared against StudentVUE".format(userInfo[0]))
        if userInfo[0] == "Calculate GPA":
        
            studentVUE_UF(userInfo[1], userPreferences[2], webdriver.Chrome())
else:
    print("Using BeautifulSoup for instant data\n")
    #" "

print(userPreferences)
