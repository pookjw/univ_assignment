import random
import sys

def printHelpMessage():
    print('Pyramid creation (20182217)\n\
    \ncommands:\
    \n-n, --row     row of pyramid you want\
    \n--random      random pyramid. You can set range. (example: ./[file].py --random 5 means row is less than 5.)')

def printPyramid(ROW):
    COL=(ROW*2)-1
    COUNT_OF_STAR=1
    while COL >= COUNT_OF_STAR:
        COUNT_OF_SPACE=int((COL-COUNT_OF_STAR)/2)
        print((' '*COUNT_OF_SPACE), end='')
        print(('*'*COUNT_OF_STAR), end='')
        print('')
        COUNT_OF_STAR+=2

# Scan what argument it is using 'IndexError: list index out of range'.
try: # if ./[file].py -n 5 or ./[file].py --row 5. It means, lens(sys.argv) == 2.
    INPUT_ARGUMENT = str(sys.argv[1])
    INPUT_NUMBER = int(sys.argv[2])
    if (INPUT_ARGUMENT == '-n') or (INPUT_ARGUMENT == '--row'): # row of pyramid you want
        if (INPUT_NUMBER>0):
            printPyramid(INPUT_NUMBER)
        else:
            print('Not a positive number.')
    elif (INPUT_ARGUMENT == '--random'): # random pyramid. You can set range. (example: ./[file].py --random 5 means row is less than 5.)
        if (INPUT_NUMBER>0):
            RANDOM_NUMBER=random.randint(1, INPUT_NUMBER)
            print('random number:', RANDOM_NUMBER)
            printPyramid(RANDOM_NUMBER)
        else:
            print('Not a positive number.')
    else:
        printHelpMessage()
except IndexError: # if ./[file].py --random. It means, lens(sys.argv) == 1.
    printHelpMessage()
