# Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted. The algorithm gets its name from the way smaller elements "bubble" to the top of the list as it is being sorted.

# Here's the pseudocode for the bubble sort algorithm:

# Start at the beginning of the list
# Compare the first two elements. If the first is greater than the second, swap them.
# Move to the next pair of elements, and compare them.
# Continue this process until the end of the list is reached.
# Repeat steps 1-4 for n-1 times, where n is the number of elements in the list.

def bubble_sort(arr):
    n = len(arr)
    
    #traverse through all array elements
    for i in range(n):
        # the last i elements are already in place
        for j in range(0, n-i-1):
            #traverse the array from 0 to n-i-1
            #swap if the element found is greater than the next element
            if arr[j] > arr[j +1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    # return arr
arr = [ 2, 4, 8, 9, 3, 5, 7]
bubble_sort(arr)
# The function takes an array arr as input and returns the sorted array. It uses two nested loops to traverse the array and compare adjacent elements. The outer loop controls the number of passes and the inner loop performs the comparisons and swaps. At the end of each pass, the largest element in the unsorted portion of the array "bubbles up" to its correct position.