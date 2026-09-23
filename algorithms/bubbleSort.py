## Bubble Sort

    #start with first item,  compare to right adjacent data item
    #if ascending, if it is larger than right adj item then data items swap
    #if not larger than stay as is
    #continue to do the same action to all data items until all have been comapred to right adj item
    #this is condsidered a pass
    #continue to perform passes on the data until a full pass has been done with no swaps bring made


def BubbleSort(data):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(data)-1):
            if data[i] > data[i+1]:
                temp = data[i]
                data[i] = data[i+1]
                data[i+1] = temp
                sorted = False
  
    return data

unsortedData = [9,3,6,2,8,1,4,5,7]
sortedData = BubbleSort(unsortedData)
print(sortedData)

# bigO
#best case time
## the data is already sorted
##O(n) - still needs to check all the items against neightbours once

#wost case time
##data is in reverse order
##O(n^2)- would perform n passes of the data each requiring n comparisons

#space
## O(1) - as size of data ncreases/decreases we do not need additional memory spaces for the algorithms

