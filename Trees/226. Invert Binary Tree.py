class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        #swap the nodes 
        root.left, root.right = root.right, root.left

        #make two rcursive calls
        self.invertTree(root.left)
        self.invertTree(root.right)

        #return the root
        return root

        