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
storeGrades(History, ComputerScience)
loadGrades()
print(GradesDB)
input("Press Enter to Exit Program")




