# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral.

 

# Example 1:

# Input: num = 3
# Output: "III"
# Explanation: 3 is represented as 3 ones.

class Solution:
    def intToRoman(self, num: int) -> str:
        roman_numerals = {
            1000 : "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
            
        }
        result = ''
        for value, symbol in roman_numerals.items():
            while num >= value:
                result += symbol
                num -= value
        return result
s = Solution()
print(s.intToRoman(2))  # Output: "II"
print(s.intToRoman(12))  # Output: "XII"
print(s.intToRoman(27))  # Output: "XXVII"
print(s.intToRoman(4))  # Output: "IV"
print(s.intToRoman(9))  # Output: "IX"

# 28-29 - This defines a class named Solution with a method intToRoman() that takes an integer num as input and returns a string as output.
# 30-45 - This is a dictionary that maps the integer values to their corresponding Roman numeral symbols. It provides the mapping between the input integer and the Roman numerals.
# 46- This initializes an empty string result to store the final Roman numeral.
# 47-50 - This is a loop that iterates through the items in the roman_numerals dictionary. For each item, it checks if the input num is greater than or equal to the current value. If so, it appends the corresponding symbol to the result string, and subtracts the value from num. This process is repeated until num becomes less than the current value, effectively constructing the Roman numeral symbol by symbol.
# his returns the final Roman numeral as a string.

# The overall logic of the code is to iterate through the dictionary of Roman numerals in descending order of their values, and for each value, check if it can be subtracted from the input num while keeping it non-negative. If so, append the corresponding symbol to the result and subtract the value from num. This process is repeated until num becomes zero, 