def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        smallest = i
        for j in range(i + 1, n):
            if arr[j] < arr[smallest]:
                smallest = j
        
        arr[i], arr[smallest] = arr[smallest], arr[i]
    return arr

# The time complexity of the above implementation of selection sort algorithm is O(n^2) because it uses nested loops. The outer loop iterates through the array once for each element, and the inner loop iterates through the remaining elements to find the smallest element. The number of operations performed is proportional to the size of the array squared.

# It's also important to note that although selection sort has a time complexity of O(n^2) it has a advantage of easy implementation and good for small lists. For large lists other sorting algorithm like quicksort, merge sort, etc which are more efficient and has better time complexity.

# The space complexity of the above implementation of selection sort algorithm is O(1) because it only uses a constant amount of space to store the index of the smallest element.