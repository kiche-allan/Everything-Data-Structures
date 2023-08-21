# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

 
# log n means we handle it using binary search

class Solution:
    def Search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            
            #check the portion w r in
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            #check if in the right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                    
                else:
                    l = mid + 1
            
        return -1  
    
# Initialize two pointers, left and right, to the start and end of the array, respectively.
# While left <= right, do the following:
# a. Calculate the middle index mid as the average of left and right.
# b. Check if nums[mid] is equal to the target. If so, return mid.
# c. Check if nums[left] is less than or equal to nums[mid]. This means that the left half of the array is sorted.
# i. If nums[left] <= target < nums[mid], it means that the target is in the left sorted half. Update right = mid - 1 to search in the left half.
# ii. Otherwise, update left = mid + 1 to search in the right half.
# d. If nums[left] > nums[mid], it means that the right half of the array is sorted.
# i. If nums[mid] < target <= nums[right], it means that the target is in the right sorted half. Update left = mid + 1 to search in the right half.
# ii. Otherwise, update right = mid - 1 to search in the left half.
# If the target is not found in the array, return -1.

# Intuition
# Utilize binary search: The problem specifically asks for an algorithm with O(log n) runtime complexity, which indicates the use of binary search, as it is one of the most efficient search algorithms with logarithmic time complexity.

# Account for the rotated array: Since the array is rotated at an unknown pivot index, we need to consider this rotation while performing the binary search. This means that the usual binary search algorithm may not work directly on the given input array. We need to modify it to handle the rotation and search for the target element accordingly.

# Identify the sorted half: We can utilize the fact that at least one half of the rotated array is always sorted. This can be used to determine which half of the array to search in based on the target value and the values at the mid and end of the array.

# Handle edge cases: We need to be mindful of edge cases such as handling an empty array or an array with just one element, as well as ensuring that the target is within the range of the array values.

# Keep track of pointers: We can use pointers to keep track of the range of the array we are currently searching in, and update them accordingly based on the comparison of target value with the mid value and the sorted half of the array.

# Return the index: Once we find the target value in the array, we can return its index. If the target is not found, we can return -1 as per the problem statement.

# Approach
# Initialize two pointers, left and right, to the start and end of the array, respectively.
# While left <= right, do the following:
# a. Calculate the middle index mid as the average of left and right.
# b. Check if nums[mid] is equal to the target. If so, return mid as the target has been found.
# c. Check if nums[left] is less than or equal to nums[mid]. This means that the left half of the array is sorted.
# i. If nums[left] <= target < nums[mid], it means that the target is in the left sorted half. Update right = mid - 1 to search in the left half.
# ii. Otherwise, update left = mid + 1 to search in the right half.
# d. If nums[left] > nums[mid], it means that the right half of the array is sorted.
# i. If nums[mid] < target <= nums[right], it means that the target is in the right sorted half. Update left = mid + 1 to search in the right half.
# ii. Otherwise, update right = mid - 1 to search in the left half.
# If the target is not found in the array, return -1.
# The above approach takes advantage of the fact that at least one half of the rotated array is always sorted, and we can determine which half to search in based on the target value and the values at the mid and end of the array. By updating the pointers left and right based on these comparisons, we can narrow down the search range and eventually find the target element or determine that it is not present in the array.

# Complexity
# Time complexity:
# The time complexity of the approach is O(log n), as it uses a binary search algorithm which has a time complexity of O(log n). The space complexity is O(1), as the algorithm uses a constant amount of extra space for the pointers left, right, and mid, and does not require any additional data structures or memory allocation.

# In each iteration of the while loop, the search range is divided by half, effectively reducing the number of elements to search by half at each step. This results in a logarithmic time complexity of O(log n), where n is the number of elements in the input array.

# Space complexity:
# The time complexity of the approach is O(log n), as it uses a binary search algorithm which has a time complexity of O(log n). The space complexity is O(1), as the algorithm uses a constant amount of extra space for the pointers left, right, and mid, and does not require any additional data structures or memory allocation.

# In each iteration of the while loop, the search range is divided by half, effectively reducing the number of elements to search by half at each step. This results in a logarithmic time complexity of O(log n), where n is the number of elements in the input array.