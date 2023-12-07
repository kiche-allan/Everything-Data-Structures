# Given an integer array nums of unique elements, return all possible 
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return 
            
            #decision to include nums[i] in subset
            subset.append(nums[i])
            dfs(i + 1)

            #decisions not to include nums[i] in subset
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res