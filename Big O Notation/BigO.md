Big O is a way to measure to measure the complexity of the algorithm. It describes the worst case scenario, in terms of number of baic operations such as additions, multiplications, comparisons e.tc. that an algorithm needs to perform in ordr to solve a problem of a certain size.
For example, an algorithm with time complexity of 0(n) needs to perform a certain number of operations proportional to the size of the input (n). An algorithm of a time complexity of 0(1) needs a constant number of operations regardless of the size of the input. 

0 1. (1) - constant time complexity
def constant_algorithm(arr):
     return arr[0]
     This algorithm simply returns the first element of the array, and the number of operations it performs does not depend on the size of the array

2. 0(n) -Linear Time Complexity
   def linear_algorithm(arr):
        for i in arr:
            print(i)
        This algorithm iterates through an array and prints each element, so the number of operations is proportional to the size of the array. 

3. 0(n^2) - Queadratic time complexity.
    def quadratic_algorithm(arr):
        for i in arr:
            for j in arr:
                print(i, j)
        This algorithm iterates through the array twice, so the number of operations performed is proportional to the size of the array squared

4. O(log(n)) - Logarithmic time complexity
    def binary_search(arr, x):
        low = 0
        high = len(arr)-1
        while low <= high:
            mid = (low + high)//2
            if arr[mid] == x:
                return mid
            elif arr[mid]< x:
                low = mid + 1
            else:
                high = mid -1
        return -1

This algorithm is a binary search algorithm which reduces the range of the search by half each time, so the number of operations it performs is proportional to log(n)

It's important to note that Big O notation describes the worst-case scenario, and that some algorithms may have a different time complexity depending on the input.

Big 0 is the language and metric used to describe the efficiency of algorithms


Algorithm run time notations
- Best case
- Average Case
- Worst case

- Big O - Its a complexity that is going to be less or equal to the worst case
- Big Omega - It is a complexity that is going to be atleast more than the best case
- Big Theta- Complexity that occur within the boundaries of the worst and the best cases

Algorithm run time complexities
Complexity              -------Name ---------                 -Sample
0(1)        --------- Constant - -------           -----Accessing a specific element in the array
0(N)           -------Linear --------              -----Loop through the array elements
0(Log N)       -------Logarithmic-----             -----Find an element in sorted array
0(N^2)          ------Quadratic-------              ----Looking at every index in the array twice
0(2^N)          ------Exponential------             ----Double recursion in Fibonacci