# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.
class Solution:
    def ReverseString(self,  s: List[str]) -> None:
       #initialize 2 pointers 
       l = 0
       r = len(s) - 1

       while l < r:
           s[l], s[r] = s[r], s[l]

           #increment the l pointer as you decrement the r pointer
           l += 1 
           r -= 1
        
           