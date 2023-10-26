# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

# For example, the square matrix  is shown below:

# 1 2 3
# 4 5 6
# 9 8 9  
# The left-to-right diagonal = . The right to left diagonal = . Their absolute difference is .

def diagonalDifference(arr):
    # Write your code here
    n = len(arr)
    ltr = 0
    rtl = 0
    
    for i in range(n):
        ltr += arr[i][i]
        rtl += arr[i][n - 1- i]
    return abs(ltr-rtl)