from selenium import webdriver

#Imagine having messy comments

def userFriendly(selectedBrowser, version):
    if version == 1:
    #Change to include different browsers later (if browser = Firefox driver = webdriver.Chrome)
        if selectedBrowser == ("Chrome"):
            return True
        elif selectedBrowser == ("Firefox"):
            driver = webdriver.Firefox()
        elif selectedBrowser == ("Safari"):
            driver = webdriver.safari()
        elif selectedBrowser == ("Edge"):
            driver = webdriver.Edge()

    elif version == 2:
        print("Soup verison pending")
