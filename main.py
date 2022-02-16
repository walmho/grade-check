import init
import tkinter as tk
from tkinter import *
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

if init.userVersion():
    print("Using a descriptive, visual based GUI to gather data...\n")
    init.directory(1, "Chrome")
    
else:
    print("Using BeautifulSoup to quickly gather data...\n")
    init.directory(2, None)


