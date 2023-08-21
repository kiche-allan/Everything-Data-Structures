# To delete a node from a binary tree, you need to perform the following steps:

# Find the node to delete in the binary tree.
# If the node has no children, simply delete it by updating its parent to remove the reference to the node.
# If the node has one child, replace the node with its child by updating its parent to point to the child.
# If the node has two children, find the node's successor (i.e., the smallest node in the node's right subtree) and replace the node's value with the successor's value. Then delete the successor node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def deleteNode(root: TreeNode, key: int) -> TreeNode:
    if not root:
        return None
    
    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.left = deleteNode(root.right, key)
        
def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The BT has been successfully deleted"
#setting up a value is 0(1) time complexity

# deleteBT(newBT)
# levelOrderTraversal(newBT)