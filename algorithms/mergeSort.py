## Merge sort

#merge sort is a divide and conquer algorithm 
#this is to say it breaks the problem down into its smallest easiest to solve parts
#these small easy to solve parts are them recombined into larher solved parts until the whole problem is solved
#divide and conquer algorithms are recursive 

#Divide stage: the sort will recursively split the data until it s in size 1 sorted arrays
#Merge stage: the smaller sub-arrays/ left and right arrays aer combined by:
# - comparing the first item in both arrrays
# - the smaller* is removed and added to a new larger array
# - this continues until one of the sub-arrays is empty
# - at which point that array with the data items still in it is added to the larger array

# this new larger sorted array is then returned to the previous call where it will be combined with another array
# this continues until the initial call merges arrays into a complete sorted array


# data[:mid] start to mid uninc
#right.pop(0) returns and removes item 0

def mergeSort(data):
    #divide
    #if data is size 1 or lower, return it

    #otherwide
    #find the middle of the data
    #recursively call the merge sort but pass in the "left" side of the data
    #store the return of this in a variable called left or similar
    #recursively call the merge sort but pass in the "right" side of the data
    #store the return of this in a varibale called right or similar

    #merge
    #whist there are still data items in Left and Right arrays
        #compare the first items of both left and right arrays
        #remove the smaller and add it to a new merged array
    #once one of left / right is empty- add the remaininh content of the other array into the new merged array
    #return the new merged array
    if len(data) <= 1:
        return(data)
    
    mid = len(data)//2
    left = mergeSort(data[:mid])
    right = mergeSort(data[mid:])

    mergedArr = []
    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:
            mergedArr.append(right[0])
            right.pop(0)
        
        else:
            mergedArr.append(left[0])
            left.pop(0)

    if len(left) > 0:
        mergedArr = mergedArr + left
    else:
        mergedArr = mergedArr + right
    return mergedArr






unsortedData = [9,8,7,6,5,4,3,2,1]
sortedData = mergeSort(unsortedData)
print(sortedData)