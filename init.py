from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#Imagine having messy comments

def userFriendly(selectedBrowser, version):
    if version == 1:
    #Change to include different browsers later (if browser = Firefox driver = webdriver.Chrome)
        if selectedBrowser == ("Chrome"):
            driver = webdriver.Chrome(ChromeDriverManager().install())
            return True
        elif selectedBrowser == ("Firefox"):
            driver = webdriver.Firefox()
        elif selectedBrowser == ("Safari"):
            driver = webdriver.safari()
        elif selectedBrowser == ("Edge"):
            driver = webdriver.Edge()

    elif version == 2:
        print("Soup verison pending")
