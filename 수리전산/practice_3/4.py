def returnDuplicatedKey(DICTIONARY_1, DICTIONARY_2):
    '''
    Usage:
    returnDuplicatedKey(DICTIONARY_1, DICTIONARY_2)
    -> returns duplicated key as Array
    '''
    TEMP_DICTIONARY=[]
    for TEMP in DICTIONARY_1.keys():
        if TEMP in DICTIONARY_2: # if DICTIONARY_1 key in DICTIONARY_2
            TEMP_DICTIONARY.append(TEMP)
    return TEMP_DICTIONARY

a_zoo={
    'mammal': 'Lion',
    'reptiles': 'Cobra',
    'Fish' : 'Tuna',
    'Bird' : 'Woodpecker',
    'Invertebrate': 'octopus',
    }
b_zoo={
    'mammal': 'Elephant',
    'reptiles': 'Alligator',
    'Fish' : 'Shark',
    'Bird' : 'Eagle',
    'Amphibians' : 'frog',
    }
print(returnDuplicatedKey(a_zoo, b_zoo)) # result: ['mammal', 'reptiles', 'Fish', 'Bird']