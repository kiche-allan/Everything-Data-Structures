# Given an integer array nums, return the length of the longest strictly increasing 
# subsequence
# .

class Solution:
    def lengthofLIS(self, nums):
        if not nums:
            return 0
        n = len(nums)
        dp = [1]* n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp = max(dp[i], dp[j]+1)
        return max(dp)
