# Omega notation describes the best-case scenario in terms of the number of basic operations that an algorithm needs to perform in order to solve a problem of a certain size. aIts the opposite of big o notation

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] ==x:
            return i
        return -1
    print(linear_search)
    
#The best-case scenario for this linear search algorithm is when the element is found at the first index (Ω(1)) and the worst-case scenario is when the element is not found in the array and the algorithm has to iterate through all the elements (O(n)). The average-case scenario is when the element is found after iterating through half of the elements (Θ(n/2))

#Another example is the binary search algorithm. The best-case scenario is when the element is found at the middle of the array. The number of operations the algorithm performs is log(n) in the best case, so the time complexity is Ω(log(n))

# It's important to note that the best-case scenario does not always occur, and that the actual time complexity of an algorithm may be affected by factors such as the input size and the distribution of the data. However, Ω notation provides an insight into the minimum number of operations an algorithm can perform to solve a problem.

# In general, the lower the value of Ω the better the algorithm is. Algorithm with Ω(1) is considered to be best as the time complexity is constant regardless of the input size.
# Also, it's important to note that Omega notation gives the lower bound of the time complexity, meaning that the time complexity of the algorithm will always be greater than or equal to the value represented by the Omega notation.