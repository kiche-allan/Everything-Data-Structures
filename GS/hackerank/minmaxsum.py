
# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

# Example

# The minimum sum is  and the maximum sum is . The function prints

# 16 24
# Function Description

# Complete the miniMaxSum function in the editor below.

# miniMaxSum has the following parameter(s):

# arr: an array of  integers
# Print

# Print two space-separated integers on one line: the minimum sum and the maximum sum of  of  elements.

# Input Format

# A single line of five space-separated integers.

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    min_sum = sum(arr[:4])
    max_sum = sum(arr[1:])
    print(min_sum, max_sum)