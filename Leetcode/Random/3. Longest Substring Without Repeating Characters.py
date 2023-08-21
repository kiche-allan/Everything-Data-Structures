# Given a string skelel, fsdfghjklfdfghind the length of the longest substring without repeating characters.
class Solution:
    def lengthOfLongestSubstring(self, s:str) -> str:
        char_set = set()
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)
            
        return max_len
    


# We define a class Solution with a method lengthOfLongestSubstring() that takes a string s as input and returns an integer as output.
# We initialize an empty set char_set to keep track of the characters in the current substring.
# We also initialize two pointers left and right to represent the start and end of the current substring, respectively.
# We initialize a variable max_len to store the length of the longest substring without repeating characters.
# We iterate through the characters in the input string s using the right pointer.
# For each character, we check if it is already in char_set. If so, we remove the character at the left pointer from char_set and move the left pointer to the right to eliminate the repeating character.
# We then add the current character to char_set and update max_len by taking the maximum of its current value and the length of the substring between left and right (inclusive).
# We continue this process until we reach the end of the input string s.
# Finally, we return the max_len as the length of the longest substring without repeating characters.