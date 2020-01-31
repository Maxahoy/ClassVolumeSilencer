"""
Intro:
Author: Maxwell Williams
Goal: A background script that can be started from the command line. You put in your class schedule, it interprets that,
confirms with you, and automatically turns off your volume every time you're in class.

Eventual goal:
-a GUI to select class times with some form of timesheet.
-Windows support
-Auto startup on boot up

Libraries that will prove useful:
ALSA (Advanced Linux Sound Architecture): python-alsaaudio
    import alsaaudio

RELEVANT:
https://askubuntu.com/questions/689521/control-volume-using-python-script

The task scheduler I'll use is called cron

"""

import HoursSelect

#csvFile = HoursSelect.selectHoursFile()

csvFile = "/home/maxwell/maxahoy/ClassVolumeSilencer/CSV_example.csv"
print(csvFile)
HoursSelect.interpretCSVFormat(csvFile)