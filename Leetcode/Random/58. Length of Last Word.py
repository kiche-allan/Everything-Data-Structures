# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal 
# substring
#  consisting of non-space characters only.
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        trimmed = s.strip()
        #find the last occurence of a space
        last_space = trimmed.rfind(' ')
        #extract the last word
        last_word = trimmed[last_space+1:]
        
        #return the length of the last word
        return len(last_word)
    
    
# Trim the string to remove any leading or trailing spaces.
# Find the last occurrence of a space in the trimmed string.
# Extract the substring after the last space (which represents the last word).
# Return the length of the last word.