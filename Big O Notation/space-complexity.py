def pairSumsequence(n):
    sum = 0
    for i in range(0, n+1):
        sum = sum + pairSum(i, i+1)
    return sum

def pairSum(a, b):
    return a + b

def pair
