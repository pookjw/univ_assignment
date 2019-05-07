def removeDuplicatedValue(ARRAY):
    '''
    Usage:
    removeDuplicatedValue(DUPLICATED_ARRAY)
    '''
    COUNT = 0
    while COUNT<len(ARRAY):
        TEMP = ARRAY[COUNT] # element to remove duplicated value
        while ARRAY.count(TEMP) != 1: # if has duplicated value, run this loop until ARRAY.count(TEMP) is 1.
            print("removed", TEMP)
            ARRAY.remove(TEMP)
        COUNT+=1
    return ARRAY

a = [30, 10, 30, 40, 10, 40, 30, 10, 40, 10, 40, 10, 30, 40]
print(removeDuplicatedValue(a))

'''
result:
removed 30
removed 30
removed 30
removed 40
removed 40
removed 40
removed 40
removed 10
removed 10
removed 10
removed 10
[10, 30, 40]
'''