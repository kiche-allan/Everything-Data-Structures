class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #log n
        
        l, r = 0, len(nums) - 1
        while l <=  r:
            mid = (l + r) // 2
            
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return l  
        
# The provided code snippet is an implementation of the searchInsert function using the binary search algorithm to find the index of a target value in a sorted array. The function takes in an array nums and a target value target as input and returns the index where the target is found. If the target is not found, it returns the index where it would be inserted to maintain the sorted order.

# The binary search algorithm in the code snippet follows the same logic as explained earlier:

# Initialize the left pointer l to 0 and the right pointer r to the last index of the input array nums.
# Perform binary search by repeatedly dividing the search space in half until the left and right pointers meet or cross each other.
# Calculate the middle index mid as the average of the left and right pointers.
# If the value at nums[mid] is equal to the target, return mid as the index where the target is found.
# If the target is greater than the value at nums[mid], update the left pointer l to mid + 1 to search in the right half.
# If the target is less than the value at nums[mid], update the right pointer r to mid - 1 to search in the left half.
# Repeat steps 3-6 until the target is found or the left and right pointers cross each other.
# If the target is not found, return the left pointer l as the index where the target would be inserted to maintain the sorted order of the array.
# The code snippet correctly implements the binary search algorithm and meets the requirement of O(log n) runtime complexity.