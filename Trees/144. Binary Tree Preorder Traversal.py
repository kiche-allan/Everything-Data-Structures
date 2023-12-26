# Given the root of a binary tree, return the preorder traversal of its nodes' values.

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        head = root
        stack = []
        res = []

        while head or stack:
            if head:
                res.append(head.val)
                if head.right:
                    stack.append(head.right)
                head = head.left
            else:
                head = stack.pop()

        return res
        
        

