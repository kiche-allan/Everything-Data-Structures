# Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

class Solution:
    def numTrees(self, n: int) -> int:
        # Initialize a dynamic programming table to store the number of unique BSTs for each number of nodes
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        
        # Calculate the number of unique BSTs for each number of nodes
        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]
                
        # Return the final result
        return dp[n]

# This is a Python class implementation of the same dynamic programming algorithm we discussed earlier. The numTrees function takes an integer n as input and returns an integer representing the number of unique binary search trees that can be formed from n distinct integers.

# Inside the function, we initialize a dynamic programming table dp to store the number of unique BSTs for each number of nodes. We start by setting dp[0] = 1 and dp[1] = 1 as the base cases.

# We then use a nested loop to calculate the number of unique BSTs for each value of i from 2 to n. For each value of i, we loop through all possible values of j from 1 to i, and calculate the number of unique BSTs that can be formed if j is the root of the tree. This is given by the product of the number of unique BSTs that can be formed from the integers 1 through j-1 for the left subtree, and the number of unique BSTs that can be formed from the integers j+1 through i for the right subtree. We add up these products for all possible values of j to get the total number of unique BSTs that can be formed from i distinct integers.

# Finally, we return dp[n] as the final result, which represents the number of unique binary search trees that can be formed from n distinct integers.