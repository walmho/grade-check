import init
import tkinter as tk
from tkinter import *
#import chromedriver_autoinstaller

"""
Step 1: Gather data of wanted websites, graphs, grades, etc.
Step 2: Check to see what user wanted
Step 3: Call proper functions from datagather site based on data list variable below
"""
import datagather as dt
from checklist import userPreferences

if init.userFriendly(userPreferences[0], userPreferences[1]):
    if userPreferences[0] == 1:
        print("Using the user friendly version\n")
        #This code here will run the neccesary functions from datagather
else:
    print("Using BeautifulSoup for instant data\n")
    #" "

print(userPreferences)
