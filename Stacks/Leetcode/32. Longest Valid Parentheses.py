# Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses 
# substring
# .

class Solution:
    def longestValidParenthesis(self, s:str) -> int:
        stack = [-1]
        max_length = 0
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                stack.pop()
                if len(stack) ==  0:
                    stack.append(i)
                else:
                    length = i - stack[-1]
                    max_length = max(max_length, length)
                    
        return max_length