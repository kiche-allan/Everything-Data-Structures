# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #if both p and q subrees aret the same
        if not p and not q:
            return True

        #if one of the subtrees aint the ame
        if not p or not q:
            return False 
        
        #if the vallue of nodes aint the same
        if p.val != q.val:
            return False

        #recursively call the functio
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
       
        
        

# The time and space complexity of the isSameTree function is mainly determined by the depth of the binary trees and the number of nodes in the trees.

# Time Complexity:

# The function performs a depth-first traversal of both trees, comparing nodes along the way.
# In the worst case, where both trees have n nodes (where n is the number of nodes in the larger tree), the function will visit every node exactly once.
# Therefore, the time complexity of the isSameTree function is O(n), where n is the number of nodes in the larger of the two trees.
# Space Complexity:

# The space complexity is determined by the function call stack during the recursive calls.
# In the worst case, if the trees are unbalanced and have a depth of n, the function call stack can grow to a depth of n.
# Therefore, the space complexity of the isSameTree function is O(n) in the worst case.
# In summary, the time complexity is O(n), and the space complexity is O(n) in the worst case. However, in balanced binary trees, the depth and space complexity can be O(log n) for both time and space, where n is the number of nodes.