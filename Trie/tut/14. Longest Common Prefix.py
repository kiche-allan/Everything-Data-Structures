# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]

        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix

# The function first checks if the input array is empty. If it is, then there can be no common prefix, and the function returns an empty string.

# If the input array is not empty, the function initializes a variable prefix to be the first string in the array. The function then iterates over the rest of the strings in the array, checking whether the prefix is a prefix of each string. If the prefix is not a prefix of a string, the function shortens the prefix by one character and tries again. The function repeats this process until it finds a common prefix for all strings or until the prefix is an empty string.

# If the function successfully finds a common prefix for all strings, it returns the prefix. Otherwise, it returns an empty string.


# The from typing import List line imports the List type hint from the typing module. This type hint is used to specify that the strs parameter is a list of strings.
# The class Solution: line declares a new class called Solution.
# The def longestCommonPrefix(self, strs: List[str]) -> str: line declares a new method called longestCommonPrefix within the Solution class. This method takes in a list of strings (strs) as its parameter and returns a string.
# self, strs: List[str]) -> str: line declares a new method called longestCommonPrefix within the Solution class. This method takes in a lis

