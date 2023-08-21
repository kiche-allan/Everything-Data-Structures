# Quick sort is a divide and conquer algorithms

# find pivot number and make sure the smallest numbers located at the left of pivot and bigger numbers locate at the right of the pivot
# Unlike merge sort extra space is not required


# Quick sort is a divide-and-conquer sorting algorithm that works by partitioning an array into two sub-arrays, one with elements smaller than a chosen pivot element and the other with elements larger than the pivot. It then recursively sorts the sub-arrays. Here is the basic algorithm:

# Choose a pivot element from the array.
# Partition the array into two sub-arrays: one with elements smaller than the pivot and one with elements larger than the pivot.
# Recursively apply the quick sort algorithm to each sub-array.


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) ]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    
    return quick_sort(left) + middle + quick_sort(right)