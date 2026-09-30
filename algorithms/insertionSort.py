## Insertion Sort

#insertion sortingworks on the principle of "splitting" the data into 2 imaginary parts
#the sorted section and unsorted section
#insertion sort then works by taking each item in turn from the unsorted side of the data and places it into the correct position in the sorted side.
#once all unsorted items have been laced we know the data is sorted.


def insertionSort(data):
    # for eac item except the first
    # store each item being placed
    # store the start position of the current item i.e. i
    # while there are items to te left AND the item to the left is larger tahn the item being placed
    #   overwrite the value at the current postion with the item to its left
    #   take 1 away from the current position 
    # once this is completed we know the position to inser the data
    #update the value at the current position to the copy of the data we took

    for i in range(1,len(data)):
        currentItem = data[i]
        pos = i
        while pos > 0 and currentItem < data[pos-1]:
            data[pos] = data[pos - 1]
            pos = pos -1
            data[pos] = currentItem
            
            print(data)
    return data


data = [9,1,3,5,4,2,8]
print(insertionSort(data))

##big O
#best case time - O(n) still needs to check all the items against neightbours once

#wosrt case time - O(n^2) would perform n passes of the data each requiring n comparisons

#space - O(1) - as size of data ncreases/decreases we do not need additional memory spaces for the algorithms