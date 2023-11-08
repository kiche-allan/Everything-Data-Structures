# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1

        while left <= right:
            mid = left + (right - left) // 2 #calculate the middle index

            if nums[mid] == target:
                return mid  #target is found, return its index
            elif nums[mid] < target:
                left = mid + 1 #adjust the left boundary
            else:
                right = mid - 1 #adjust theright boundary\
        return -1
        