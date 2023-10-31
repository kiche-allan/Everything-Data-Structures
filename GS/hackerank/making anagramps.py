# A student is taking a cryptography class and has found anagrams to be very useful. Two strings are anagrams of each other if the first string's letters can be rearranged to form the second string. In other words, both strings must contain the same exact letters in the same exact frequency. For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.

# The student decides on an encryption scheme that involves two large strings. The encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. Determine this number.

# Given two strings,  and , that may or may not be of the same length, determine the minimum number of character deletions required to make  and  anagrams. Any characters can be deleted from either of the strings.

# Example


# Delete  from  and  from  so that the remaining strings are  and  which are anagrams. This takes  character deletions.

# Function Description

# Complete the makeAnagram function in the editor below.

# makeAnagram has the following parameter(s):

# string a: a string
# string b: another string
# Returns

# int: the minimum total characters that must be deleted
# Input Format

# The first line contains a single string, .
# The second line contains a single string, .

def makeAnagram(a, b):
    # Write your code here
    char_count_a = {}
    char_count_b = {}
    
    #count the character frequencies in a string
    for char in a:
        char_count_a[char] = char_count_a.get(char, 0) + 1
        
    #count character frrequencies in string b
    for char in b:
        char_count_b[char] = char_count_b.get(char, 0) + 1
        
    #calculate the minimum number of deletions required
    deletions = 0
    for char in char_count_a:
        if char in char_count_b:
            deletions += abs(char_count_a[char] - char_count_b[char])
        else:
            deletions += char_count_a[char]
    for char in char_count_b:
        if char not in char_count_a:
            deletions += char_count_b[char]
    return deletions