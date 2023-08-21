from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_counts = {}
        for num in nums:
            if num in num_counts:
                num_counts[num] += 1
            else:
                num_counts[num] = 1
        for num, count in num_counts.items():
            if count == 1:
                return num
            
            
# We start by importing the List type from the typing module and defining a Solution class with a method called singleNumber that takes in a list of integers called nums and returns a single integer.

# We create an empty dictionary called num_counts to store the count of each number in nums.

# We loop through each number in nums and update its count in the dictionary. If the number is already in the dictionary, we increment its count. Otherwise, we add it to the dictionary with a count of 1.

# We loop through the dictionary using the items method to find the number with a count of 1, which is the non-duplicate element. We return that number.

# The main advantage of this approach is that it works even if there are multiple elements in nums that appear only once. However, it requires extra space to store the dictionary, which violates the constant extra space requirement of the problem.