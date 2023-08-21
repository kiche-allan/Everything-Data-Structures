class Solution:
    def fib(self, N: int) -> int:
        
        seen = {0:0, 1:1}
        
        for i in range(2, N+1):
            seen[i] = seen[i-1] + seen[i-2]
        return(seen[N])
    
    # Intuition
# <!-- Describe your first thoughts on how to solve this problem. -->

# This question can be solved either through recursion or iteration

# # Approach
# <!-- Describe your approach to solving the problem. -->
# This approach uses a technique of memoization. It stores the already calculated vallues in a dictionary, where the keys are the inputs and the values are the corresponding output. This way when the function is called again with the same input, the output can be returned immediately without recalculating

# # Complexity
# - Time complexity:
# <!-- Add your time complexity here, e.g. $$O(n)$$ -->
# The time complexity of the above code is 0(n) which means that the number of operations increases linearly with the size of input(n). This is because when we are iterating through loop from 2 to N and in each iteration we are calculating the fibonacci number using the values from the previous iteration. We are storing the previously calculated fibonaci numbers in a dictionary so that the function can look up the value instead of recalculating. In this way we are avoiding the recalculation of the same values, making the function more efficient. 

# - Space complexity:
# <!-- Add your space complexity here, e.g. $$O(n)$$ -->

# The space complexity of the above code is also 0(n). This is because we are using a dictionary to store the previously calculated fibonacci numbers. The size of the dictionary increases linearly with the size of input(n).

# If we dont use memoization, the time complexity of the above code will be 0(2^n) and the space complexity wil be 0(n) because it will require to store the function call stack of size n
# # Code
# ```

# ```