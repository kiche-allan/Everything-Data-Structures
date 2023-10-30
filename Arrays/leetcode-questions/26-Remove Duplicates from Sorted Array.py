# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.


#SOLUTION ONE

# from ast import List


# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         l = 1
        
#         for r in range(1, len(nums)):
#             if nums[r] != nums[r-1]:
#                 nums[l] = nums[r]
                
#                 l + 1
#             return l

#SOLUTION TWO
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # Check if the input array is empty, return 0 if it is
        
        if not nums:
            return 0
        
        #initialize the two pointers, l and r and where l points to the last unique element and r iterates through the array
        
        l = 0
        
        for r in range(1, len(nums)):
            
            #if the current element is different from the previous element, increment l pointer and replace the element at l pointer with current elemnt
            if nums[r] != nums[l]:
                l += 1
                nums[l] = nums[r]
                
                # Return the length of the array containing unique elements
                #Return the length of the array containing unique elements
        # The length of the array is slow + 1, as the slow pointer points to the last unique element, which is at index slow
        
        return l + 1
    
    #Describe your first thoughts on how to solve this problem
    
    # My first thought for solving this problem was using two pointers. One pointer will iterate through the array and the other pointer will keep track of the last unique element. If the current element is different from the previous element, the unique element pointer will be incremented and the current element will be placed in new position
    
    #
    # Describe your approach to solving the problem.
    
    #My approach to solving this problem is to use two pointers, where one pointer iterates through the input array and the other pointer keeps track of the last unique element. The fast pointer will iterate through the array, starting from the second element, while the slow pointer starts from the first element.

#At each step, I will compare the current element at the fast pointer with the previous element at the slow pointer. If they are different, it means the current element is unique, so I will increment the slow pointer by 1 and replace the element at the slow pointer with the current element. This way, all duplicates will be removed in-place and the relative order of the elements will be preserved.

#Finally, I will return the length of the array containing only unique elements, which can be calculated as the slow pointer position + 1.
    
    
#time complexity
# The time complexity of the solution above is 0(n), where n is the number of elements in the array. The fast pointer iterates through the array once, while the slow pointer iterates through the array at most once. Therefore, the time complexity is 0(n). This is because we are using a single loop to iterate through the input array once. The time taken by the loop is directly proportional to the size of the input array so the time complexity is linear



#space complexity
# The space complexity of the solution is O(1), which means that the space used by the algorithm is constant and does not grow with the size of the input.

# The solution uses two pointers, slow and fast, which only take up a constant amount of memory, regardless of the size of the input array. The solution does not use any additional data structures or arrays, so the space complexity remains constant at O(1).