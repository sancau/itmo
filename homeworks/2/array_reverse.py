# reverse implementation (changes initial list in place)
def revert(iterable):
    length = len(iterable)
    for i in range(length // 2):
        target = length - i - 1
        iterable[i], iterable[target] = iterable[target], iterable[i]
    return iterable 
    
 
# calculates the number of '*' symbols in a string
stars_number = len([ch for ch in string if ch == '*'])
