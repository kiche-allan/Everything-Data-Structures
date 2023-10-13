# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        #write a helper function
        def dfs(left, right):
            #if both of the nodes are none, it means they are symmetric
            if not left and not right:
                return True
            #if only one of the nodes is None, then its not symmetric
            if not left or not right:
                return False
        #recursively check the subtrees
            return (left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left))
        return dfs(root.left, root.right)

    
        