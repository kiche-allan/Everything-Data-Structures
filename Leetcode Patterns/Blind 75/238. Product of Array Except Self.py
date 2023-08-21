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
    
# def productExceptSelf(self, nums: List[int]) -> List[int]:
# This is the definition of a function productExceptSelf which takes a list of integers nums as input and returns a list of integers as output.

# n = len(nums)
# It calculates the length of the input list nums and assigns it to the variable n.

# left_product = [1] * n
# It initializes a new list left_product of length n, filled with 1's. This list will store the product of all elements to the left of the current element in the nums list.

# right_product = [1] * n
# Similarly, it initializes a new list right_product of length n, filled with 1's. This list will store the product of all elements to the right of the current element in the nums list.

# for i in range(1, n):
# This loop calculates the left products of each element in the nums list and stores them in the left_product list. It starts from index 1 because the first element's left product is always 1.

# left_product[i] = left_product[i-1]* nums[i-1]
# It calculates the left product of the current element by multiplying the previous element's left product (left_product[i-1]) with the corresponding element in the nums list (nums[i-1]).

# for i in range(n-2, -1, -1):
# This loop calculates the right products of each element in the nums list and stores them in the right_product list. It starts from n-2 because the last element's right product is always 1.

# right_product[i] = right_product[i+1]* nums[i+1]
# It calculates the right product of the current element by multiplying the next element's right product (right_product[i+1]) with the corresponding element in the nums list (nums[i+1]).

# ans = [left_product[i] * right_product[i] for i in range(n)]
# This line calculates the final output list ans by taking the element-wise product of left_product and right_product lists.

# return ans
# The function returns the ans list, which contains the product of all elements in nums except the element itself.

# In summary, this code uses two separate lists, left_product and right_product, to store the products of elements to the left and right of each element in the nums list. Then, it calculates the final result by taking the element-wise product of the two lists. This approach allows the function to compute the product of all elements except the element itself efficiently in linear time complexity.