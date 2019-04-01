import datetime
import sys
now = datetime.datetime.now()
CURRENT_YEAR=int("%d" % now.year)

def printHelpMessage():
    print('Leap year determination (20182217)\n\
    \ncommands:\
    \n-c, --current   determine that current year is a leap year\
    \n-y, --year      determine its a leap year')

def printLeapYear(YEAR):
    if YEAR % 400 == 0:
        print(YEAR, 'is a leap year. (reason:', YEAR, 'modulo 400 is 0.)')
    elif YEAR % 100 == 0:
        print(YEAR, 'is not a leap year. (reason:', YEAR, 'modulo 100 is 0.)')
    elif YEAR % 4 == 0:
        print(YEAR, 'is a leap year. (reason:', YEAR, 'modulo 4 is 0.)')
    else:
        print(YEAR, 'is not a leap year. (reason:', YEAR, 'modulo 4 is not 0.)')

# Scan what argument it is using 'IndexError: list index out of range'.
try: # if ./[file].py -y 2028 or ./[file].py --year 2028. It means, lens(sys.argv) == 2.
    INPUT = int(sys.argv[2])
    if (INPUT>0):
        printLeapYear(INPUT)
    else:
        print('Not a positive number.')
except IndexError: # if ./[file].py -c or ./[file].py --cureent. It means, lens(sys.argv) == 1.
    try:
        INPUT=str(sys.argv[1])
        if (INPUT == '--current') or (INPUT == '-c'):
            printLeapYear(CURRENT_YEAR)
        else:
            printHelpMessage()
    except IndexError: # if ./[file].py. It means, lens(sys.argv) == 1.
        printHelpMessage()
