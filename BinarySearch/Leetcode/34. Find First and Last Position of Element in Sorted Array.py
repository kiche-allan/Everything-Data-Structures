# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        l, r = 0, len(nums) - 1

        #find the first occurence of the target value

        while l <= r:
            m = (l + r ) // 2
            if nums[m] == target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
            if first == -1:
                return [-1, -1]
            # Find the last occurrence of the target value
            last = first
            while l <= r:
                m = (l + r ) // 2
                if nums[m] == target:
                    last= m
                    l = m + 1
                else:
                    r = m - 1
            return [first, last]
        

    