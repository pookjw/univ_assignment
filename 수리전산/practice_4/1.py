def convertTuple(TUPLE):
    '''
        Usage:
        convertTuple([(a, b), (c, d), (e, f)])
        -> return ([a, c, e], [b, d, f])
        '''
    TEMP_1 = 0
    TEMP_2 = 0
    TEMP_3 = 0
    LIST = []
    while TEMP_1 < len(TUPLE[0]):
        LIST.append([])
        TEMP_1 += 1
    while TEMP_2 < len(TUPLE[0]):
        while TEMP_3 < len(TUPLE):
            LIST[TEMP_2].append(TUPLE[TEMP_3][TEMP_2])
            TEMP_3 += 1
        TEMP_3 = 0
        TEMP_2 += 1
    return tuple(LIST)

print(convertTuple([(2,5,6,2), (3,6,7,4), (8,3,5,7)])) #result: ([2, 3, 8], [5, 6, 3], [6, 7, 5], [2, 4, 7])
