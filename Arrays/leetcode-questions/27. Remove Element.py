# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.

class Solution:
    def removeElemennt(self, nums:List[int], val:int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
                
        return k
    
    
# The code is defining a class Solution with a method removeElement. The method takes in two parameters: nums, which is a list of integers, and val, which is the integer value we want to remove from nums. The method returns an integer, which is the count of elements in nums that are not equal to val.

# This line initializes a variable k to 0. k will keep track of the index where we want to place the next element that is not equal to val.

# This line sgtarts a loop that iterates over the indices of the nums list. It uses the range(len(nums)) function to generate a sequence of indices from 0 to len(nums) - 1.

# This line checks if the value at index i in nums is not equal to val. If the condition is true, it means the current element is not equal to val, and we want to keep it in the modified nums list.
# This line increments the value of k by 1, indicating that we have placed one more element in the modified nums list.

# After the loop finishes, we have iterated over all the elements in nums, and the modified nums list contains all the elements not equal to val, placed at the beginning of the list.

# This line returns the value of k, which represents the count of elements in nums that are not equal to val.