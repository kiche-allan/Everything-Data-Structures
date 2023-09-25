# There is a function signFunc(x) that returns:

# 1 if x is positive.
# -1 if x is negative.
# 0 if x is equal to 0.
# You are given an integer array nums. Let product be the product of all values in the array nums.

# Return signFunc(product).

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neg = 0
        for n in nums:
            if n == 0:
                return 0
            neg += (1 if n < 0 else 0)
        return -1 if neg % 2 else 1
    
# Time Complexity:

# The code uses a for loop to iterate through each element in the input list nums. The loop runs once for each element in the list, so the time complexity of this part is O(n), where n is the number of elements in nums.

# Inside the loop, there is a simple conditional check (if n == 0) and an addition operation (neg += ...). These operations are constant time operations, so they don't change the overall time complexity.

# Finally, there is another conditional check (return -1 if neg % 2 else 1) outside the loop. This check is also a constant time operation since it doesn't depend on the size of the input list.

# Therefore, the overall time complexity of the arraySign method is O(n), where n is the number of elements in the nums list.