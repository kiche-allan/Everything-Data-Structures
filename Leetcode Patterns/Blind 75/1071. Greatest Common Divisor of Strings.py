# For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

# class Solution:
#      def gcdOfString(self, str1: str, str2: str) -> str:
#         # if str1 and str2 are equal, return str1
#         if str1 == str2:
#             return str1
#         # if str1 and str2 are not equal, return ""
#         if str1 != str2:
#             return ""
#         # if str1 is longer than str2, swap str1 and str2
#         if len(str1) > len(str2):
#             str1, str2 = str2, str1
#             #if str1 is not a substring of str2, return ""
#             if str1 not in str2:
#                 return ""
#             #if str1 is a substring of str2, return str1
#             else:
#                 return str1
#         # if str1 is not longer than str2, return ""
#         else:
#             return ""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1, len(str2))

        # helper function
        def isDivisor(l):
            if len1 % l or len2 % l:
                return False
            f1, f2 = len1 // l, len2 // l
            return str1[:l] * f1 == str1 and str1[:l] * f2 == str2

        for l in range(min(len1, len2), 0, -1):
            if isDivisor(l):
                return str1[:l]
        return ""
