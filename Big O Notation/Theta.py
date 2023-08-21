# Theta notation (Θ notation) is a way of expressing the upper and lower bounds of an algorithm's running time complexity. It provides a tight bound on the growth of the running time of an algorithm. The running time of an algorithm is often expressed using big O notation, which provides an upper bound on the growth of the running time. However, big O notation can be too loose, and Theta notation provides a tighter bound by expressing both the upper and lower bounds.

# The notation is used to describe the time complexity of an algorithm and is typically represented by the Greek letter Theta (Θ) followed by a mathematical expression. The mathematical expression represents the function that describes the running time of the algorithm.


def find_max(arr):
    max_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val

# In this example, the time complexity of the function is O(n) because the time it takes to execute the function increases linearly with the size of the input array. This is because we are iterating through the array once and in each iteration we are comparing the current element with the current maximum value. We can also express the time complexity using Theta notation as Θ(n), which means that the function will always run in linear time.

