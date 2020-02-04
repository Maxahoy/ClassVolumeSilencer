"""
Creates a data structure for class  storage

Each class will have an ID, a name (optional)
    A Mon start & end, a Tues start & end, a Wed start & end, a Thurs start & end, and a Fri start & end.

    If

"""

import StringProcessing

class Schedule:
    #data structures for classes

    #class start times for each day of week
    monStartTimes = dict()
    tuesStartTimes = dict()
    wedStartTimes = dict()
    thursStartTimes = dict()
    friStartTimes = dict()

    #class end times for each day of week
    monEndTimes = dict()
    tuesEndTimes = dict()
    wedEndTimes = dict()
    thursEndTimes = dict()
    friEndTimes = dict()

    classes = list()

    #function to fill in the data structures

    #function to change times


# I would love to call this one "class", but that's a protected keyword.
# I'll be calling it "section", instead. This is intended to be for each class a student takes.
class Section:

    classID = 0

    classDays = list()

    classStartTime = 0
    classEndTime = 0

    #returns a startTime time object and a endTime time object
    # TODO: make it read in a start & end time for classes
    # Assume for now that classes will always start and end at the same time, every day of the week
    def getTimes(csvDict, classID):
        start = ""
        end = ""

        classString = csvDict[classID]
        return start, end

    #TODO: make it read in days that a class occurs, assuming same days every week

    """
    1: ['1', 'Stats', '10:20:00 AM', '', '10:20:00 AM', '', '10:20:00 AM', '', '', '11:15:00 AM', '', '11:15:00 AM', '', '11:15:00 AM']",
       
    2: "['2', '', '', '09:35:00 AM', '', '09:35:00 AM', '', '', '', '', "
       "'10:55:00 AM', '', '10:55:00 AM', '']"
       
    Day of week with comma dictionary:
    Start
    Monday = 3rd item,
    Tues = 4th item
    Wed = 5
    Thurs = 6
    Fri = 7
    
    End
    Mon = 10
    Tues = 11
    Wed = 12
    Thurs = 13
    Fri = 14
    
    
    """
    def getDays(csvDict, classID):
        dayList = list()

        classString = csvDict[classID]

        return dayList

    def __init__(self, csvDict, classID):
        startTime, endTime = self.getTimes(csvDict, classID)

        dayList = self.getDays(csvDict, classID)

        self.classID = classID
        self.classDays = dayList
        self.classStartTime = startTime
        self.classEndTime = endTime
