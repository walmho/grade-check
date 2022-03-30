from random import choices
import tkinter as tk
from typing import OrderedDict

r = tk.Tk()
r.title("Basic Checklist")

#How checkbox normally works without the use of a loop. This is what it would look like if I did each function selection manually
def normalOptions():
    #Variable has to be an IntVar.
    appleVar = tk.IntVar()
    apple = tk.Checkbutton(r, text="Apples", variable=appleVar, justify=tk.CENTER)
    apple.grid(row=0, column=0)

    orangeVar = tk.IntVar()
    orange = tk.Checkbutton(r, text="Orange", variable=orangeVar, justify=tk.CENTER)
    orange.grid(row=1, column=0)

    pearVar = tk.IntVar()
    pear = tk.Checkbutton(r, text="Pear", variable=pearVar, justify=tk.CENTER)
    pear.grid(row=2, column=0)

    grapeVar = tk.IntVar()
    grape = tk.Checkbutton(r, text="Grape", variable=grapeVar, justify=tk.CENTER)
    grape.grid(row=3, column=0)

    #Not using .get() yet because as of assigning the values to selection, the user doesn't have a chance to click on anything in time.
    #Selections work if it's just a list of the IntVars. I'm trying to give each one keys as well so that way the code knows which command to use.
    #selections = [appleVar, orangeVar, pearVar, grapeVar]

    selections = {"apple":appleVar, "orange":orangeVar, "pear":pearVar, "grape":grapeVar}
    print(selections)

    finish = tk.Button(r, text="Return Selected", font=("arial", 10), command=lambda:returnSelected(selections))
    finish.grid(row=4, column=0)

def returnSelected(selectionDict):
    for i in range(len(selectionDict)):
        key = getKey(selectionDict, i)
        chosen = selectionDict[key].get()

        if chosen:
            print("The user likes {}.".format(key))
        else:
            print("The user does not like {}".format(key))

#Thank you stack overflow for telling me how to index dictionaries
def getKey(dictionary, n=0):
    if n < 0:
        n += len(dictionary)
    for i, key in enumerate(dictionary.keys()):
        if i == n:
            return key
    raise IndexError("dict index out of range")

#My attempt at doing the above with a loop to make it shorter
def optimizedOptions():
    #Add try and excepts for index errors, in case choices and intVars don't line up for some reason
    choices = ["apple", "orange", "grape", "pear"]
    #Tk intvars gather whether or not an item is selected
    intVars = []
    for i in range(len(choices)):
        intVars.append(tk.IntVar())

    #dictionary is needed for returning selected options
    selections = loadDictionary(intVars, choices)
    print(selections)

    #loop that creates and grids options in tkinter using the dictionary
    for i in range(len(choices)):
        temp = tk.Checkbutton(r, text=choices[i], variable=intVars[i], justify = tk.CENTER)
        temp.grid(row=i, column=0)

    finish = tk.Button(r, text="Return Selected", font=("arial", 10), command=lambda:returnSelected(selections))
    finish.grid(row=i+1, column=0)

#Given itemes and keys, return a dictionary - might not need this but it is a useful function 
def loadDictionary(items, keys):
    if len(items) != len(keys):
        print("ERROR: loadDictionary(items, keys) Too many keys / items")
        return

    dictionary = {}
    for i in range(len(items)):
        dictionary[keys[i]] = items[i]

    return dictionary

optimizedOptions()

r.mainloop()
