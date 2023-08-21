# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_product = [1] * n
        right_product = [1] * n

        for i in range(1, n):
            left_product[i] = left_product[i-1]* nums[i-1]

        for i in range(n-2, -1, -1):
            right_product[i] = right_product[i+1]* nums[i+1]

        ans = [left_product[i] * right_product[i] for i in range(n)]
        return ans
    
    
# We first create two arrays left_product and right_product of length n, initialized to 1.
# In the first pass, we compute the product of all elements to the left of each element and store it in the left_product array. We start with index 1 since the product of all elements to the left of index 0 is 1.
# In the second pass, we compute the product of all elements to the right of each element and store it in the right_product array. We start with index n-2 since the product of all elements to the right of index n-1 is 1.
# Finally, we compute the final answer by multiplying the corresponding elements of left_product and right_product.
# This approach has a time complexity of O(n) since we traverse the array twice. It also doesn't use division operation as required.




# Intuition
# Sure! When I first saw this problem, I thought about how to calculate the product of all elements in the array except the current element without using division operation. One approach that came to mind was to calculate the product of all elements to the left of the current element and the product of all elements to the right of the current element separately, and then multiply them to get the product of all elements except the current element.

# To do this, we can first create an array of length n to store the product of all elements to the left of each element. Then, we can iterate over the array from right to left, calculating the product of all elements to the right of each element and multiplying it with the corresponding element in the left product array to get the final product of all elements except the current element.

# This approach has a time complexity of O(n) and doesn't use division operation, but it requires O(n) extra space for the left product array. However, we can optimize it by using the same left product array to store the product of all elements to the right of each element in a backward pass of the array, thereby reducing the extra space requirement to O(1).

# So, my initial thoughts were to use two passes of the array to calculate the product of all elements except the current element, and to avoid using division operation to make the solution more efficient.

# Approach
# Create an array of length n to store the product of all elements to the left of each element. Initialize the first element of this array to 1.
# Iterate over the input array nums from left to right. For each index i, calculate the product of all elements to the left of nums[i] (excluding nums[i]) and store the result in left_product[i]. Update left_product[i] as left_product[i-1] * nums[i-1].
# Create a variable right_product and initialize it to 1.
# Iterate over the input array nums from right to left. For each index i, calculate the product of all elements to the right of nums[i] (excluding nums[i]) by multiplying right_product with left_product[i]. Update right_product as right_product * nums[i].
# Create an array answer of length n. For each index i, calculate the product of all elements except nums[i] as left_product[i] * right_product and store the result in answer[i].
# Return the answer array.

# Complexity
# Time complexity:
# O(n)
# where n is the length of the input array nums. This is because we iterate over the array three times: twice for calculating the left and right product arrays, and once for calculating the final answer array. Since we're doing a constant amount of work for each element of the array in each pass, the time complexity is O(n).

# Space complexity:
# O(n)

# n terms of space complexity, we're using three arrays: left_product, right_product, and answer. The left_product and right_product arrays each require O(n) space, since they have the same length as the input array. The answer array also requires O(n) space since we need to store the product of all elements except the current element for each index. Therefore, the total space complexity of our algorithm is O(n).

# The constraints:
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time
# Cannot use the division operation.