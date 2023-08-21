# Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

# Note:

# Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
# In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.
 

# Example 1:

# Input: n = 00000000000000000000000000001011
# Output: 3
# Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

class Solution:
    def hammingWeight(self, n:int) -> int:
        res = 0
        while n:
            res += n % 2
            n = n>> 1
        return res
    
# The given code defines a class Solution with a method hammingWeight that calculates the Hamming weight of an integer n, which represents a binary number. The Hamming weight is the number of '1' bits in the binary representation of the integer.

# The method starts by initializing a variable res to 0. It then enters a while loop that continues until n becomes 0. Inside the loop, it calculates the remainder of n divided by 2, which gives the value of the least significant bit (LSB) of n. This value is added to the res variable. Then, it right-shifts n by 1, effectively removing the LSB and shifting the rest of the bits to the right by one position. This process is repeated until all the bits of n have been processed.

# Finally, when the while loop exits, the method returns the value of res, which represents the Hamming weight of the original integer n.

# Overall, the given code correctly calculates the Hamming weight of an integer using bitwise operations and a loop. However, it can be further optimized using the bitwise AND operation instead of modulo and division to determine the LSB, like this: