# Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 ==0 and x !=0):
            return False

        reversed_num = 0
        num = x 

        while num > 0:
            digit = num % 10
            reversed_num = reversed_num *10 + digit
            num //=10

        return x == reversed_num

# class Solution: - This declares a class named Solution.

# def isPalindrome(self, x: int) -> bool: - This defines a method named isPalindrome, which takes an integer x as input and returns a boolean value indicating whether x is a palindrome.

# if x < 0 or (x % 10 == 0 and x != 0): - This line checks if x is negative or if it ends with a 0 but is not 0 itself, in which case it cannot be a palindrome. If either of these conditions is true, the method returns False.

# reversed_num = 0 - This initializes a variable reversed_num to 0.

# num = x - This assigns the value of x to a variable num.

# while num > 0: - This starts a while loop that will execute as long as num is greater than 0.

# digit = num % 10 - This calculates the remainder when num is divided by 10, which is the rightmost digit of num.

# reversed_num = reversed_num * 10 + digit - This multiplies reversed_num by 10 and adds digit to the result. This effectively "shifts" the digits of reversed_num one place to the left and adds the new digit to the rightmost position.

# num //= 10 - This integer divides num by 10, effectively removing the rightmost digit.

# return x == reversed_num - This checks if the original input x is equal to the reversed number reversed_num. If they are equal, then x is a palindrome, and the method returns True. If they are not equal, then x is not a palindrome, and the method returns False.