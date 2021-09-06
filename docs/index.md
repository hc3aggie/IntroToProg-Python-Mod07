# Write a Script that demonstrates Pickling and Exception Handling.
## Henry Chisolm: September 5, 2021

## Introduction:
  The purpose of this assignment is to create a new script that demonstrates the techniques of pickling and exception handling in a python.  Pickling is the process where a data from a file is converted and stored in a binary way which obscures the data and condenses it.  Exception handling is the process when writing scripts where one identifies errors and can custom code a message (or rather error message) so it is easier for another user or collaborator to understand where the program may be faltering.  To do this I created a script that stored some data for a gradebook and then later loaded the data.  Additionally, we were asked to post this in a GitHub page.
## Code:
~~~
# --------------------#
# Title: Examples of Pickling and Exception Handling
# Dev: HChisolm
# Date 9/3/2021
# ChangeLog: (Who, When, What)
#   HChisolm 09/03/2021, Create Script
#   HChisolm 09/05/2021, Appended script to include error handling
# ---------------------#


########### Pickling - how to convert data to a binary file. ##############

import pickle
# do first to pickle mode is imported for all subsequent values

# Data
strFile = "PicklingExample.txt"
DBFile = None
file = None
History = {"Henry": "91", "Diana": "94", "Richard": "88", "Caroline": "97"}
ComputerScience = {"Henry": "82", "Diana": "92", "Richard": "94", "Caroline": "95"}
# added here becuse I created local vaviables in my data to initially load the data bit needed global
GradesDB = {}
GradesDB["History"] = History
GradesDB["ComputerScience"] = ComputerScience
# Processing
# Create a program that stores grade data
def storeGrades(History, ComputerScience):
    # data to be stored in dictionary database of Grades
    History = {"Henry": "91", "Diana": "94", "Richard": "88", "Caroline": "97"}
    ComputerScience = {"Henry": "82", "Diana": "92", "Richard": "94", "Caroline": "95"}

    GradesDB = {}
    GradesDB["History"] = History
    GradesDB["ComputerScience"] = ComputerScience
    # pickling process
    DBFile = open(strFile, "ab")
    pickle.dump(GradesDB, DBFile)
    print(GradesDB)
    DBFile.close()

def loadGrades():
    try:
        DBFile = open(strFile, "rb")
        #unpickling to display
        GradesDB = pickle.load(DBFile)
        for keys in GradesDB:
            print ("Course:", "\n", keys, ":", GradesDB[keys])
        DBFile.close
    ####### Custom Exception Error #######
    except FileNotFoundError as e:
        print ("File not found.")

# Presentation
print ("Grade Book Program")
input("Press Enter to continue program")
# running and loading our initial information
storeGrades(
History, ComputerScience)
loadGrades()
print(GradesDB)
input("Press Enter to Exit Program")
~~~
## Scope of the Assignment:
The scope of this assignment involves creating a script, which displays the concepts of pickling and exception handling.  So to analyze this assignment we will look at the (1) initial code to set up the assignment, (2) code for pickling, and (3) code to do error handling.
## *(1) Initial Script:*
This assignment asked us to make a program that highlighted pickling and exception handling without being provided with initial code to adapt and modify.  Additionally, we were asked to research the topics of pickling and error handling to highlight and explain different ways it can be used and utilized in a program.  So to highlight this I created a grade book program, with two functions storeGrades and loadGrades, to be the beginning code for a gradebook program.
#### storeGrades:
I created a function with two local variable (it took me a while to realize the local v. global variable in how I was programming my script and the ramnifications), History and ComputerScience followed by a {} or a dictionary entry with name keys and grades. The purpose of this function was to have a hard coded beginning for further adapting and entering data.
~~~
def storeGrades(History, ComputerScience):
    # data to be stored in dictionary database of Grades
    History = {"Henry": "91", "Diana": "94", "Richard": "88", "Caroline": "97"}
    ComputerScience = {"Henry": "82", "Diana": "92", "Richard": "94", "Caroline": "95"}
 ~~~
This was followed by creating a variable Grades DB which acted as directory for the data that we had just scripted, allowing both the courses of History and ComputerScience (our variables) to be pulled up.  
~~~
    GradesDB = {}
    GradesDB["History"] = History
    GradesDB["ComputerScience"] = ComputerScience
~~~
Finally in this function we pickle the information, which will be discussed later.  To do this through a variable strFile which we have open and create a file “PicklingExamples.txt” in an “ab”, which will append the file (create or open and add information but won’t erase initial information in a binary form)
#### loadGrades:  
Next up was creating a function that loaded the data from the function storeGrades in the prior step.  In this case we did a try command with an except that dealt with exception handling, that will be discussed later in this paper.  We opened the strFile which we created earlier on “rb”  which is read mode but also in binary, we further have to unpickle it which is discussed later but the outcome is the file is loaded into our program.
~~~
    try:
        DBFile = open(strFile, "rb")
        #unpickling to display
        GradesDB = pickle.load(DBFile)
        for keys in GradesDB:
            print ("Course:", "\n", keys, ":", GradesDB[keys])
        DBFile.close
~~~
A for loop was used bringing up the dictionary keys displaying what was initially in the program. What is displayed isn’t the most elegant but it does convey the information.
#### Presentation and Variable Handling:
Finally, the program runs the two functions that were scripted storeGrades and loadGrades.  A few points were added to get the script to pause and or display data for screen capture.  A print and input key were added to just pause the program before our functions were called.  
~~~
print ("Grade Book Program")
input("Press Enter to continue program")
~~~
This is followed by our functions and finally printing or GradesDB which was the dictionry we set up in the storeGrades function.  Although in this case I had created a local variable in the function as opposed to a global variable so, I added the variable from the storeGrades function outside of the function to have information to be drawn upon.
Final results of our program running:

    
