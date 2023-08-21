class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        i = 0

        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp


        while i <= r:
            if nums[i] ==0:
                swap(l, i)
                l += 1

            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1

            i += 1
            
# This code is a Python implementation of the Dutch National Flag algorithm to sort an array of colors represented by integers 0, 1, and 2. Here is a detailed explanation of each line of code:

# python
# Copy code
# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
# This is the class definition of the solution with a function sortColors that takes an input array nums and modifies it in place. The function does not return anything.

# scss
# Copy code
# l, r = 0, len(nums) - 1
# i = 0
# These lines initialize three pointers l, r, and i. l and r point to the left and right ends of the array respectively, while i is a variable that will traverse the array.

# less
# Copy code
# def swap(i, j):
#     tmp = nums[i]
#     nums[i] = nums[j]
#     nums[j] = tmp
# This is a helper function swap that takes two indices i and j and swaps the values at those indices in the input array nums.

# less
# Copy code
# while i <= r:
#     if nums[i] == 0:
#         swap(l, i)
#         l += 1
#     elif nums[i] == 2:
#         swap(i, r)
#         r -= 1
#         i -= 1
#     i += 1
# This is the main part of the function, which uses the Dutch National Flag algorithm to sort the array. The loop traverses the array from left to right using the i pointer, comparing each element to 0, 1, and 2, and performing the appropriate swap operations based on the comparison.

# If nums[i] is equal to 0, then it should be placed at the beginning of the array, so we swap it with the element at l and increment l to move the boundary of the 0s section to the right.

# If nums[i] is equal to 2, then it should be placed at the end of the array, so we swap it with the element at r and decrement r to move the boundary of the 2s section to the left. Since the swapped element could be a 0, 1, or 2, we need to recheck it again in the next iteration, hence we decrement i by 1.

# If nums[i] is equal to 1, then it is already in the correct position, so we simply increment i to move on to the next element.

# The loop continues until i exceeds r, at which point the array is sorted in place according to the order of 0s, 1s, and 2s.

# Overall, this code is a concise and efficient implementation of the Dutch National Flag algorithm in Python.
            
# Intuition
# My first thought upon reading the problem statement would be to use some sort of sorting algorithm to arrange the colors in the correct order. Since there are only three possible colors (red, white, and blue), and they can be represented by the integers 0, 1, and 2, I would consider using an algorithm that can work well with small integers, such as counting sort, bucket sort, or quick sort.

# After deciding on an appropriate algorithm, I would think about how to implement it in Python, and how to modify it to work specifically with this problem. For example, if using quick sort, I would need to partition the array into three parts rather than the usual two.

# Alternatively, I might also consider using a three-pointer approach, where I maintain three pointers, one for the next position where a 0 should be placed, one for the next position where a 2 should be placed, and one that traverses the array. By swapping elements as necessary, I could ensure that all the 0s are at the beginning of the array, all the 2s are at the end, and all the 1s are in the middle.

# Overall, my approach would be to carefully read and understand the problem statement, and then brainstorm possible solutions based on my existing knowledge of sorting algorithms and programming techniques.

# Approach
# There are multiple approaches to solving the problem of sorting an array of colors in linear time. One common and efficient approach is to use the Dutch National Flag algorithm, which is a three-pointer approach that partitions the array into three parts: the 0s, the 1s, and the 2s.

# Here is how I would approach solving the problem using the Dutch National Flag algorithm:

# Initialize three pointers, low, mid, and high, where low points to the start of the array, mid points to the start of the unclassified region, and high points to the end of the array.

# Traverse the array from mid to high using a loop. While traversing the array, compare the value at the mid pointer with the values 0, 1, and 2, and perform the following operations accordingly:

# a. If the value at mid is 0, swap it with the value at low and increment both low and mid.

# b. If the value at mid is 1, simply increment mid.

# c. If the value at mid is 2, swap it with the value at high and decrement high. Do not increment mid in this case, because the value at high may need to be swapped again.

# Repeat step 2 until mid is greater than high.

# After the loop completes, the array will be sorted in place as per the required order of 0s, 1s, and 2s.

# The time complexity of this algorithm is O(n), where n is the length of the array, since each element is compared and swapped at most twice. The space complexity is O(1), since the algorithm modifies the array in place and uses only three pointers.

# Complexity
# Time complexity:
# The time complexity of the given solution is O(n), where n is the length of the input array nums. This is because the algorithm traverses the array from left to right exactly once, and performs a constant number of operations on each element, including swaps, comparisons, and increments or decrements of the pointers.

# Specifically, the while loop in the function runs n times, and the maximum number of swaps that can occur is also n, since each element can be swapped at most once. Therefore, the time complexity of the algorithm is linear with respect to the size of the input, making it an efficient solution for sorting an array of colors.

# Space complexity:
# The space complexity of the given solution is O(1), which is constant space. This is because the algorithm modifies the input array in place, without requiring any additional data structures or memory allocations. The only extra space used is for the three pointers, which are O(1) space in total.

# Overall, the given solution is both time and space efficient, and is a good solution for sorting an array of colors in linear time.