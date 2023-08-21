# LeetCode 231. Power of Two
# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2x.

# solution1 - iterative division
class Solution:
    def PowerOfTwo(self, n:int) -> bool:
        if n == 0:
            return False
        while n % 2 == 0:
            n /= 2
        return n == 1
    
#solution2
# mathematical approach
# import math

# class Solution:
#     def PowerOfTwo(self, n:int) -> bool:
#         if n <= 0:
#             return False
#         else:
#             power = math.log2(n)
#             return power = int(power)


#solution3 - bit manipulation
# class Solution:
#     def PowerOfTwo(self, n:int) -> bool:
#         if n <= 0:
#             return False
#         else:
#             return (n & n -1 ) ==0
            