# Given a positive integer num, return true if num is a perfect square or false otherwise.

# A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

# You must not use any built-in library function, such as sqrt.

# class Solution:
#     def isperfectSquare(self, num: int) -> bool:
#         #0(sqet(num))
#         # for i in (1, num +1):
#         #     if i * i == num:
#         #         return True
#         # 0(log n)
#         l = 1
#         r = num

#         while l <= r:
#             mid = (l+r) // 2
#             if mid * mid == num:
#                 r = mid - 1
#             elif mid * mid < num:
#                 l = mid + 1
#             else:
#                 return True
#         return False


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 1
        r = num

        while l <= r:
            mid = (l + r) // 2
            if mid * mid >  num:
                r = mid - 1
            elif mid * mid < num:
                l = mid + 1
            else:
                return True
        return False