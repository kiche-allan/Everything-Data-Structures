# Merge sort is a divide-and-conquer sorting algorithm that works by recursively dividing the input array into halves, sorting each half, and then merging the sorted halves back together. Here is the basic algorithm:

# Divide the input array into two halves.
# Sort each half by recursively applying the merge sort algorithm.
# Merge the sorted halves back together into a single sorted array.

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    #divide the array into two halves
    mid = len(arr)
    left = arr[:mid]
    right = arr[mid:]
    
    #recursively sort each half
    left = merge_sort(left)
    right = merge_sort(right)
    
    #merge the sorted halves
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result += left[i:]
    result += right[j:]
    
    return result
            