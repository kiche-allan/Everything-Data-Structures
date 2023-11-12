# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #initialize two pointers to the beginning of the window
        charSet = set()
        l = 0
        res = 0
        

        #initialize a dictionary to store the last seen element within the string
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r-l + 1)

        return res