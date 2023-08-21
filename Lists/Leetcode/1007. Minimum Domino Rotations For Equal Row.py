# 1007. Minimum Domino Rotations For Equal Row

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        for target in [tops[0], bottoms[0]]:
            missingT, missingB = 0, 0
             
            for i, pair in enumerate(zip(tops, bottoms)):
                top, bottom = pair
                if not( top == target or bottom ==target):
                    break
                if top != t1: missingT += 1
                if bottom != t1: missingB += 1
                if i == len(tops) -1:
                    return min(missingT, missingB)
       
        return -1
            
# It uses a slightly different approach to iterate through each domino and count the number of rotations needed.

# The algorithm first tries to make the top values the same as the first top value or the bottom values the same as the first bottom value, which is the target. It then counts the number of rotations needed for each possibility and returns the minimum count.

# The code first iterates through two possibilities for the target: the first top value and the first bottom value. For each target, it initializes missingT and missingB as 0, which represent the number of dominos that need to be rotated to make all the tops or bottoms equal to the target.

# It then iterates through each domino using enumerate(zip(tops, bottoms)). For each domino, it checks if either the top or bottom value is equal to the target. If not, it means that it is impossible to make all the tops or bottoms equal to the target, so it breaks out of the loop.

# If either the top or bottom value is not equal to the target, it increments the corresponding missing variable by 1.

# Finally, if it reaches the end of the loop, it means that it is possible to make all the tops or bottoms equal to the target, so it returns the minimum of the two missing variables.

# If it doesn't find any target that satisfies the condition, it returns -1.

# The time complexity of this algorithm is also O(n), where n is the length of top

# Intuition
# My first thought to solve this problem is to use a brute force approach where we try all possible combinations of rotating the dominos and check which combination gives us the minimum number of rotations to make all the tops or bottoms equal. However, this approach has a very high time complexity and is not practical for large inputs.

# A better approach would be to count the frequency of each number in both tops and bottoms using a dictionary, and check if there is at least one number with a frequency equal to the length of tops or bottoms. If there is, we can make all the values in tops or bottoms equal to that number. Then we can iterate through each domino and count the number of rotations needed to make its top or bottom equal to the target value. We take the minimum of these counts as the answer.

# This approach has a time complexity of O(n), where n is the length of tops or bottoms, and is much more efficient than the brute force approach.

# Approach
# The approach to solve this problem involves finding a number that occurs in all dominos either as top or bottom. Once such a number is found, we can make all the dominos have that number on either top or bottom by rotating the dominos as required.

# Complexity
# Time complexity:
# 0(n)
# The time complexity of the above solution is O(n), where n is the length of the input lists tops and bottoms. This is because we iterate through the dominos only once to count the frequency of each number and to find a number that occurs in all dominos. The subsequent iteration through the dominos to count the number of rotations needed for each domino also takes O(n) time.

# Space complexity:
# 0(1)
# The space complexity of the above solution is O(1) because we use a constant amount of space to store the dictionaries top_count and bottom_count and the variables target, missingT and missingB. The size of the dictionaries is at most 6, as there are only 6 possible values for a domino, and the other variables take constant space. Therefore, the space complexity of the solution is independent of the input size.