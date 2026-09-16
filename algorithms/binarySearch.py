def binarySearch(data,term):
    ##list must be sorted
    #set upper and lower pointers
    #find length of the list
    #find middle item of list
    #compare item to the term
    #if it is the same return suitable value, e.g. true
    #if not see if the value is less than or greater than middle value
    #if greater than then discard the middle and anything left
    #if less than then disregard the middle and anything right
    #find the next middle value and repeat until value is found
    #if theres no match then return false or another suitable value
    length = len(data)
    startPointer = 0
    endPointer = length -1
    while startPointer < endPointer:
        middle = (startPointer + endPointer)//2
        
        if data[middle] == term:
            return True, term
        elif data[middle] > term:
            endPointer = middle -1 
        else:
            startPointer = middle +1
        
    return False, -1


data = [1,2,3,4,5,6,7,8,9]
success = binarySearch(data,2)
print(success)
