import random
import sys

'''
example:
$ ./file.py -n 9
[8, 9, 7, 2, 7, 3, 5, 5, 9]
55
'''

def sumDictionary(DICTIONARY):
    SUM = 0
    TEMP_2 = 0 # temp var for getting dictionary sum
    while TEMP_2 < len(DICTIONARY):
        SUM += DICTIONARY[TEMP_2]
        TEMP_2+=1
    return SUM

def printHelpMessage():
    print('sum of dictionary (20182217)\n\
    \ncommands:\
    \n-n [number]     length of random integer (1 from 9) dictionary')

try:
    INPUT_NUMBER = int(sys.argv[2]) # ./file.py -n [INPUT_NUMBER]
    TEMP_1 = 0 # temp var for creating random dictionry length
    RANDOM_DICTIONARY = [] # random dic

    # creating random dictionary
    while TEMP_1 < INPUT_NUMBER:
        RANDOM_DICTIONARY.append(random.randint(1, 9))
        TEMP_1+=1

    print(RANDOM_DICTIONARY) # created random dictionary
    print(sumDictionary(RANDOM_DICTIONARY))
except IndexError:
    printHelpMessage()
