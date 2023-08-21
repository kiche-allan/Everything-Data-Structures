# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned)

class Solution:
    def reverse(self, x: int) -> int:
        rev_number = 0                            # initialize the reversed number to 0
        is_negative = x < 0                       # check if input integer is negative
        x = abs(x)                                # convert input integer to positive
        while x > 0:                              # loop through digits of the input integer
            remainder = x % 10                   # extract last digit of the input integer
            rev_number = rev_number * 10 + remainder # add extracted digit to reversed number
            x //= 10                             # remove last digit from input integer
        if is_negative:                           # adjust reversed number if input integer was negative
            rev_number = -rev_number
        if rev_number < -2**31 or rev_number > 2**31 - 1: # check for overflow
            return 0                              # return 0 if reversed integer overflows the range
        return rev_number                         # return the reversed integer if within the range

# Intuition
# My first thoughts on how to solve this problem would be to convert the integer to a string, reverse the string, and convert it back to an integer. However, this solution would not work in the case of an overflow, as the resulting integer may exceed the 32-bit integer range.

# To solve this problem while avoiding the overflow issue, I would need to reverse the integer using only mathematical operations without converting it to a string. One approach would be to repeatedly extract the last digit of the input integer using modulo division, then add each extracted digit to the reversed integer after shifting the digits one place to the left using multiplication by 10. I would also need to check for overflow after each addition to ensure that the resulting integer remains within the 32-bit integer range.

# Approach
# The approach I would use to solve this problem is to repeatedly extract the last digit of the input integer using modulo division, then add each extracted digit to the reversed integer after shifting the digits one place to the left using multiplication by 10. To handle negative input integers, I would first check if the input integer is negative and set a flag accordingly, then convert the input integer to its absolute value for the rest of the operations.

# After reversing the integer, I would check if the resulting integer is within the 32-bit integer range. To do this, I would compare the reversed integer to the upper and lower limits of the 32-bit integer range. If the reversed integer is outside this range, I would return 0 as required by the problem statement. If the reversed integer is within the range, I would return it.

# Overall, this approach avoids using string operations to reverse the integer and ensures that the resulting integer is within the 32-bit integer range, meeting the requirements of the problem statement.

# Complexity
# Time complexity:
# O(log(x))
# The time complexity of the mathematical operation approach is O(log(x)), where x is the input integer. This is because we need to extract each digit from the input integer, and the number of digits in the input integer is proportional to its logarithm.

# Space complexity:
# O(1)
# The space complexity of this approach is O(1), as we are only using a constant amount of additional space to store the reversed integer and some variables.