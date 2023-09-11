class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0

        while a> 0 or b> 0 or c> 0:
            bit_a = a & 1
            bit_b = b & 1
            bit_c = c & 1

            if bit_c == 0:
                flips += (bit_a + bit_b)
            else:
                if bit_a == 0 and bit_b == 0:
                    flips += 1
            a >>= 1
            b >>= 1
            c >>= 1

        return flips
        
# class Solution:: This line defines a Python class named Solution.

# def minFlips(self, a: int, b: int, c: int) -> int:: This is the method definition. It declares a method named minFlips that takes three integers a, b, and c as input parameters and returns an integer. The goal of this method is to calculate the minimum number of bit flips required to make (a OR b) == c.

# flips = 0: Initialize a variable flips to 0. This variable will be used to keep track of the minimum number of bit flips needed.

# while a > 0 or b > 0 or c > 0:: This line sets up a while loop that continues as long as at least one of the integers a, b, or c has bits remaining to be processed.

# bit_a = a & 1: Extract the least significant bit of a by performing a bitwise AND operation with 1 (a & 1). This stores the result in the bit_a variable.

# bit_b = b & 1: Extract the least significant bit of b by performing a bitwise AND operation with 1 (b & 1). This stores the result in the bit_b variable.

# bit_c = c & 1: Extract the least significant bit of c by performing a bitwise AND operation with 1 (c & 1). This stores the result in the bit_c variable.

# if bit_c == 0:: This conditional checks if the least significant bit of c is 0.

# flips += (bit_a + bit_b): If bit_c is 0, this line increments the flips variable by the sum of bit_a and bit_b. This means that if either a or b has a 1-bit at the same position where c has a 0-bit, it counts as a flip.

# else:: If bit_c is not 0 (i.e., it's 1), this block of code is executed.

# if bit_a == 0 and bit_b == 0:: This conditional checks if both bit_a and bit_b are 0 when bit_c is 1. This means that if both a and b have 0-bits at the same position where c has a 1-bit, it counts as a flip.

# flips += 1: If both bit_a and bit_b are 0 when bit_c is 1, increment the flips variable by 1, indicating that a flip is required.

# a >>= 1, b >>= 1, c >>= 1: Right-shift a, b, and c by 1 bit, effectively discarding the least significant bits so that the next bit can be processed in the next iteration of the loop.

# Finally, when the while loop completes, return the flips variable, which contains the minimum number of bit flips required to make (a OR b) == c.1318