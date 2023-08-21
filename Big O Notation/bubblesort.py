def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j +1]:
                arr[j], arr[j +1] = arr[j + 1], arr[j]
    return arr

#In this example, the time complexity of the function is O(n^2) because the time it takes to execute the function increases quadratically with the size of the input array. This is because we are iterating through the array twice, once in the outer loop and once in the inner loop. The number of iterations in the inner loop is dependent on the outer loop. We can also express the time complexity using Theta notation as Θ(n^2), which means that the function will always run in quadratic time.