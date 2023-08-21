class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []  # Create an empty list to store the result of triplets
        nums.sort()  # Sort the given list of integers
        for i, a in enumerate(nums):  # Loop over the list using enumerate to access both the value and index
            if i > 0 and a == nums[i-1]:  # Skip duplicate elements
                continue
            l, r = i + 1, len(nums) - 1  # Initialize two pointers, l on the left and r on the right
            while l < r:  # Iterate while left pointer is less than right pointer
                threeSum = a + nums[l] + nums[r]  # Calculate the sum of three elements
                if threeSum > 0:  # If sum is greater than 0, decrement the right pointer
                    r -= 1
                elif threeSum < 0:  # If sum is less than 0, increment the left pointer
                    l += 1
                else:  # If sum is 0, append the triplet to the result list and increment left pointer
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:  # Skip duplicate elements
                        l += 1
        return res  # Return the list of triplets

# Intuition
# My first thought to solve this problem is to sort the input list in non-descending order. Then, for each number in the list, we will check if we can find a pair of numbers in the remaining list that adds up to the negation of the current number. We will use a two-pointer technique to find the pair of numbers. Since we need to return all possible triplets, we will continue the process for every number in the list. Finally, we will return all the triplets that satisfy the condition.

# Approach
# The problem requires us to find all unique triplets in the input array nums that sum up to zero. One possible approach is to sort the array in non-decreasing order and then for each element in the array, use a two-pointer approach to find all pairs of elements (in the remaining part of the array) that sum up to the negative of the current element. Since the input can have duplicate elements, we need to be careful not to include duplicate triplets in our result.

# The time complexity of this approach will be O(n^2), where n is the length of the input array, because we are iterating over each element once and then doing a linear search in the remaining part of the array.

# The space complexity of this approach will be O(1), because we are not using any additional data structures to store the input or the result.

# Complexity
# Time complexity:
# The time complexity of the above solution is O(n^2), where n is the length of the input array nums. This is because we are iterating over the input array twice in the worst case scenario.

# Space complexity:
# The space complexity of the above solution is O(1), as we are not using any additional data structures that grow with the input siz