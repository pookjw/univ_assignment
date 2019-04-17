# Available on GitHub https://github.com/pookjw/univ_assignment/blob/master/수리전산/practice_2/fibonacci.py

import sys

def helpMessage():
    print("""fibonacci.py (https://github.com/pookjw/univ_assignment/blob/master/수리전산/practice_2/fibonacci.py) - 20182217
options:
-p1 [number]        solve Problem 1
-p2 [number]        solve Problem 2
-p3 [number]        solve Problem 3
-p4 [start] [end]   solve Problem 4""")

class superClass: # SuperClass to calculate fibonacci number
    def recursion(self, COUNT): # Problem 1
        if COUNT < 2:
            return COUNT
        return (self.recursion(COUNT-2) + self.recursion(COUNT-1))

    def iteration(self, COUNT): # Problem 2
        if COUNT < 2:
            return COUNT
        TEMP_1 = 1
        TEMP_2 = 1
        for LOOP in range(2, COUNT):
            TEMP_3 = TEMP_1
            TEMP_1 += TEMP_2
            TEMP_2 = TEMP_3
        return TEMP_1
    
class fibonacci(superClass): # Subclass to return you want
    def __init__(self, ALGORITHM):
        self.ALGORITHM = ALGORITHM
    def number(self, COUNT): # Problem 1 and 2
        if self.ALGORITHM == "recursion":
            return self.recursion(COUNT)
        elif self.ALGORITHM == "iteration":
            return self.iteration(COUNT)
    def sequence(self, START, END): # Problem 3 and 4
        TEMP_LIST = []
        for LOOP in range(START,END+1):
            TEMP_LIST.append(self.number(LOOP))
        return TEMP_LIST

try: # Problem 4 - ./fibonacci.py -p4 [START - like 4] [END - like 8]
    PROBLEM = str(sys.argv[1])
    START_NUMBER = int(sys.argv[2])
    END_NUMBER = int(sys.argv[3])
    if START_NUMBER < END_NUMBER:
        if PROBLEM == "-p4":
            problem4 = fibonacci("recursion")
            print(problem4.sequence(START_NUMBER, END_NUMBER))
    else:
        print("ERROR:", START_NUMBER, "is bigger than", END_NUMBER)
        print()
        helpMessage()
except IndexError:
    try: # Problem 1, 2 ,3 - ./fibonacci -p1 [NUMBER - like 5]
        PROBLEM = str(sys.argv[1])
        NUMBER = int(sys.argv[2])
        if PROBLEM == "-p1":
            problem1 = fibonacci("recursion")
            print(problem1.number(NUMBER))
        elif PROBLEM == "-p2":
            problem2 = fibonacci("iteration")
            print(problem2.number(NUMBER))
        elif PROBLEM == "-p3":
            problem3 = fibonacci("recursion")
            print(problem3.sequence(0, NUMBER))
        else:
            print("ERROR: Something is missing\n")
            helpMessage()
    except IndexError:
        helpMessage()
