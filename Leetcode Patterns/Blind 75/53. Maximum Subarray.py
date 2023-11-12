# Given an integer array nums, find the 
# subarray
#  with the largest sum, and return its sum.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub =  nums[0]
        currentSum = 0
        for num in nums : #0(n) - time 
            if currentSum < 0:
                currentSum = 0
            currentSum  += num
            maxSub = max(maxSub, currentSum)
        return maxSub
        #0(1) space complexity
        
        