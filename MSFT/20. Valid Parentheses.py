# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
class Solution:
    def ValidParenthesis(self, s: str) -> bool:
        open_count = 0
        curly_count = 0
        square_count = 0

        for char in s :
            if char == '(':
                open_count += 1
            elif char == ')':
                open_count -= 1
            elif char ==  '{':
                curly_count += 1
            elif char == '}':
                curly_count -= 1
            elif char == '[]':
                square_count += 1
            elif char == ']':
                square_count -= 1

        if open_count == 0 and curly_count == 0 and square_count == 0:
            return True


# solution 2

# using stack data structure
class Solution:
    def isValidParenthesis(self, s: str) -> bool:
        stack = []
        matching_pairs = {'(': ')', '{': '}', '[': ']'}
        for char in s:
            if char in matching_pairs:
                stack.append(char)
            elif char in matching_pairs.values():
                if not stack or matching_pairs[stack.pop()] != char:
                    return False
            else:
                return False
            
        return not stack
