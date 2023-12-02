# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is 
# the smallest in lexicographical order
#  among all possible results.

class Solution:
    def removeDuplicateLetters(self, s:str) -> str:
        last_occurence = {char: i for i, char in enumerate(s)}
        
        visited = set()
        stack = []
        

        for i, char in enumerate (s):
            if char in visited:
                continue
            while stack and char < stack[-1] and i < last_occurence[stack[-1]]:
                visited.remove(stack.pop())
            
            stack.append(char)
            visted.add(char)
        return ''.join(stack)
