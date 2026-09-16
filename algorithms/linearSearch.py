import random

##Linear Search
def LinearSearch(data, term):
    #beginning at the first item in the data
    #compare it to the search term
    # if they match then return a suitable value e.g. true
    #else move onto the next item in the data
    #once all items have been checked with no match found return False (or suitable)
    for i in data:
        if i == term:
            return True, i
    return False




data = [random.randint(1,10) for i in range(10)]
print(data)
term = 5
found = LinearSearch(data,term)
print(found)
