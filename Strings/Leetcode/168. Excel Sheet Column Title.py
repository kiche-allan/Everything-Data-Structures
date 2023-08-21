# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

# For example:

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 

class Solution:
    def convertToTitle(self, colunNumber: int) -> str:
        result = ""
        
        while colunNumber > 0:
            remainder = colunNumber % 26
            if remainder == 0:
                remainder = 26
                colunNumber -= 1
                
            character = chr(ord('A') + remainder - 1)
            result = character + result
            
            colunNumber //= 26
            
        return result