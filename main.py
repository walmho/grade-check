import init
import tkinter as tk
from tkinter import *
#import chromedriver_autoinstaller

"""
Step 1: Gather data of wanted websites, graphs, grades, etc.
Step 2: Check to see what user wanted
Step 3: Call proper functions from datagather site based on data list variable below
"""
from checklist import userPreferences
import datagather as dt

print(userPreferences)
#potentially add in a "loader" function here that puts userPreference data into an easier format to code then "Userpreferences[n]"

if init.userFriendly(userPreferences[0], userPreferences[1]):
    if userPreferences[0] == 1:
        print("Using the user friendly version\n")
        if userPreferecnes[2] == "StudentVUE":
            dt.studentVUE_UF(userPreferences[3], userPreferences[4])
else:
    print("Using BeautifulSoup for instant data\n")
    #" "

print(userPreferences)
