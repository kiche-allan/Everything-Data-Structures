# Insertion sort is a sorting algorithm that places an unsorted element at its suitable place in each iteration.

# divide the given array into two partsTake the first element from unsorted array and find its correct position in sorted array
# repeat untill unsorted array is empty
def insertionSort(customList):  
    for i in range(1, len(customList[j])):
        key = customList[j][i]
        j = i-1
        while j>=0 and key < customList[j]:
            customList[j + 1] = customList[j]
            j -= 1
            
        customList[j +1 ] = key
        
    print(customList)

cList = [2, 1, 7, 6, 5, 3, 4, 9, 8]
insertionSort(cList)

# In this implementation, customList is the list to be sorted. The algorithm iterates through each item in the list, starting from the second item (i=1). It compares the current item with the items before it, and swaps them if necessary, until the current item is in its correct position. The outer loop continues until all items have been sorted, and the sorted list is returned.

# when to use insertion sort

# -when we have insufficient memory
# -easy to implement
# - when we have a continuos inflow of numbers and we want to keep them sorted


# when to avoid insertion sort
# - when time is a concern