"""
All string methods gonna go in here I guess

Let's put
"""

"""
input: takes in a string of class info and places the times into a list

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
    
Goes through, picks out the items based on where the commas are, and creates a list based on the items in there
"""
def lineList(classString):

    lineList = [x.strip() for x in classString.split(',')]
    lineList = [x.strip("'") for x in lineList]

    #print(lineList)
    return lineList
