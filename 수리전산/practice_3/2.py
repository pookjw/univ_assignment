def convertTuple(TUPLE):
    '''
    Usage:
    convertTuple([(a, b), (c, d), (e, f)])
    -> returns ([a, c, e], [b, d, f])
    '''
    TEMP = 0
    LIST_1 = []
    LIST_2 = []
    while TEMP < 3:
        LIST_1.append(TUPLE[TEMP][0])
        LIST_2.append(TUPLE[TEMP][1])
        TEMP += 1
    return(LIST_1, LIST_2)

print(convertTuple([(2,5), (3,6), (8,3)])) #result: ([2, 3, 8], [5, 6, 3])