from init import userVersion

def directory(version, browser):
    if version == 1:
        #Change to include different browsers later (if browser = Firefox driver = webdriver.Chrome)
        driver = webdriver.browser()
        

userVersion()
if userVersion:
    print("Using a descriptive, visual based GUI to gather data...\n")
    directory(1, "Chrome")
    
else:
    print("Using BeautifulSoup to quickly gather data...\n")
    directory(2)

