# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        missing = n
        
        for i in range(n):
            missing ^= i ^ nums[i]
            
        return missing
    
# The variable n is assigned the length of the nums list, which represents the maximum number in the range [0, n].

# The variable missing is initialized with the value n, assuming it to be the missing number.

# The loop iterates over the range from 0 to n-1 (inclusive). Within each iteration:

# The XOR operation is performed between missing and the current index i.
# Then, the result of the XOR operation is further XORed with the current element nums[i]. This cancels out the numbers present in the list.
# After the loop, the variable missing holds the missing number, which was not canceled out by the XOR operations.

# Finally, the value of missing is returned as the result of the function.