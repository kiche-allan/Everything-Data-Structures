# There is a sequence of words in CamelCase as a string of letters, , having the following properties:

# It is a concatenation of one or more words consisting of English letters.
# All letters in the first word are lowercase.
# For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.
# Given , determine the number of words in .

# Example

# There are  words in the string: 'one', 'Two', 'Three'.

# Function Description

# Complete the camelcase function in the editor below.

# camelcase has the following parameter(s):

# string s: the string to analyze
# Returns

# int: the number of words in 
# Input Format

# A single line containing string .

def camelcase(s):
    # Write your code here
    if not s:
        return 0
    count = 1 
    #initialize count for the first word
    for char in s:
        if char.isupper():
            count += 1
    return count
