"""
This is how I'm gonna schedule hours

IDEA: import the format example file that I'm using and is saved in the same directory


"""

from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import csv


def selectHoursFile():
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    print(filename)
    return filename

"""
Receives a file location, opens the csv

The format looks like this:

CLASS STARTS,Class name (optional),MON,TUES,WED,THURS,FRI,,CLASS ENDS,MON,TUES,WED,THURS,FRI
1,             Stats,             10:20:00 AM,,10:20:00 AM,,10:20:00 AM,,,11:15:00 AM,,11:15:00 AM,,11:15:00 AM
2,,,09:35:00 AM,,09:35:00 AM,,,,,10:55:00 AM,,10:55:00 AM,
3,,,11:30:00 AM,11:30:00 AM,11:30:00 AM,11:30:00 AM,,,,12:25:00 PM,12:25:00 PM,12:25:00 PM,12:25:00 PM
4,,,,,,09:10:00 AM,,,,,,,10:05:00 AM
5,,12:00:00 PM,01:00:00 PM,01:00:00 PM,01:00:00 PM,01:00:00 PM,,,,04:30:00 PM,04:30:00 PM,04:30:00 PM,04:30:00 PM
6,,,,,,,,,,,,,
7,,,,,,,,,,,,,
8,,,,,,,,,,,,,
9,,,,,,,,,,,,,
10,,,,,,,,,,,,,
11,,,,,,,,,,,,,
12,,,,,,,,,,,,,
13,,,,,,,,,,,,,
14,,,,,,,,,,,,,
15,,,,,,,,,,,,,

"""
def interpretCSVFormat(csvFile):
    #first open the file with the filepath
    classList = dict()
    with open(csvFile, "r") as csvOpen:
        #next populate a temporary dictionary for the classes
        tempDict = dict()
        classID = 0
        rowReader = csv.reader(csvOpen, delimiter=',', quotechar="'")
        for row in rowReader:
            #dictionary format: class ID::string of class days
            classTimes = row
            #print(row)
            tempDict[classID] = str(classTimes)
            classID = classID + 1
        del tempDict[0]
        print(tempDict)




