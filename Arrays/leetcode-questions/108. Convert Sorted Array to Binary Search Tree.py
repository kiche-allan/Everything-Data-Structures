# Given an integer array nums where the elements are sorted in ascending order, convert it to a 
# height-balanced
#  binary search tree.

class Solution:
    def sortedArrayToBST(self, nums:List[int]) -> Optional[TreeNode]:
        def helper(l, r):
            if l > r:
                return None
            
            m = (l + r) // 2
            root = TreeNode(nums[m])
            root.left = helper(l, m - 1)
            root.right = helper(m + 1, r)
            return root
        return helper(0, len(nums) - 1)

# The code defines a class Solution with a method sortedArrayToBST. The method takes in a list of integers nums and returns an optional TreeNode, representing the root of a binary search tree.
# This line defines a recursive helper function named helper that takes in two parameters l and r, representing the left and right indices of the subarray to be processed. If l becomes greater than r, it means there are no elements to construct a subtree, so the function returns None.
# This line calculates the middle index m of the current subarray by finding the integer division of the sum of l and r by 2. It then creates a new TreeNode with the value nums[m] as the root of the subtree.
# These two lines recursively construct the left and right subtrees of the current root. It calls the helper function with updated indices to process the respective subarrays and assigns the return values to the left and right attributes of the current root node.
# This line initiates the recursive construction of the binary search tree by calling the helper function with the initial indices 0 and len(nums) - 1. It returns the result of the recursive construction, which is the root of the binary search tree representing the sorted array.

# The provided code follows a similar approach to the previous explanation. It constructs a height-balanced binary search tree recursively by dividing the sorted array into two halves. It selects the middle element as the root of each subtree and assigns the left and right subtrees using recursive calls to the helper function. Finally, it returns the root of the constructed binary search tree.