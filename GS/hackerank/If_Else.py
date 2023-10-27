# Given an integer,n, perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird
# Input Format

# A single line containing a positive integer, .

# import math
# import os
# import random
# import re
# import sys



# if __name__ == '__main__':
n = int(input())
if n % 2 ==1:
    print("Weird")
elif n in range(2, 6):
    print("Not Weird")
elif n in range(6, 21):
    print("Weird")
else:
    print("Not Weird")
    
# Explanation:

# First, we read the input integer using the input() function and convert it to an integer using the int() function.
# Then, we use an if-elif-else statement to implement the given logic.
# If the number is odd, we print "Weird".
# If the number is even and in the range 2 to 5, we print "Not Weird".
# If the number is even and in the range 6 to 20, we print "Weird".
# If the number is even and greater than 20, we print "Not Weird".