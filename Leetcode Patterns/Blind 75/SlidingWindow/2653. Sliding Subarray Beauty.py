# Given an integer array nums containing n integers, find the beauty of each subarray of size k.

# The beauty of a subarray is the xth smallest integer in the subarray if it is negative, or 0 if there are fewer than x negative integers.

# Return an integer array containing n - k + 1 integers, which denote the beauty of the subarrays in order from the first index in the array.

# A subarray is a contiguous non-empty sequence of elements within an array.
from sortedcontainers import SortedList
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        ans = []

        N = len(nums)
        sorted_list = SortedList()
        for i in range(N):
            sorted_list.add(nums[i])

            if i - k >= 0:
                sorted_list.remove(nums[i-k])

            if len(sorted_list) >= k:
                #print the sorted list
                t = sorted_list[x -1]
                if t >= 0:
                    ans.append(0)
                else:
                    ans.append(t)
        return ans
                    

