# Reverse bits of a given 32 bits unsigned integer.

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res | (bit <<( 31 - i))
        return res

# for _ in range(bit_length): - This is a loop that iterates bit_length number of times, which is 32 in this case. The variable _ is used as a placeholder for the loop variable since it is not used within the loop.

# reversed_bits = (reversed_bits << 1) | (n & 1) - This line performs two operations:

# (reversed_bits << 1) - This left-shifts the value of reversed_bits by 1 bit. Shifting left by 1 is equivalent to multiplying the value by 2. This operation creates space for the next bit in reversed_bits.

# (n & 1) - This performs a bitwise AND operation between n and 1. The purpose of this operation is to extract the least significant bit of n. Since 1 in binary representation is 00000001, performing a bitwise AND with n will result in either 0 or 1, depending on the least significant bit of n.

# | - This performs a bitwise OR operation between the shifted reversed_bits and the extracted least significant bit of n. It sets the least significant bit of reversed_bits to the value of the extracted bit from n. This operation effectively adds the extracted bit to the reversed number.

# Finally, the result of the above operations is assigned back to reversed_bits, updating its value.

# n >>= 1 - This right-shifts the value of n by 1 bit. Shifting right by 1 is equivalent to integer division by 2. This operation discards the least significant bit of n so that the next bit can be extracted in the next iteration of the loop.

# The combination of these operations within the loop allows us to reverse the bits of the given 32-bit unsigned integer n and store the reversed bits in the variable reversed_bits