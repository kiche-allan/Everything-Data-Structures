class TreeNode:
    def __init__(self, data, children = []):
        self.data = data
        self.children = children
    def __str__(self, level=0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret
        
    def addChild(self, TreeNode):
        self.children.append(TreeNode)
        
tree = TreeNode('Drinks', [])
cold = TreeNode('Cold', [])
hot = TreeNode('Hot', [])
tree.addChild(cold)
tree.addChild(hot)

tea = TreeNode('Tea', [])
coffee = TreeNode('Coffee', [])

colla = TreeNode('colla', [])
fanta = TreeNode('fanta', [])

cold.addChild(colla)
cold.addChild(fanta)
hot.addChild(tea)
hot.addChild(coffee)
print(tree)



def searchBT(rootNode, nodeValue):
    
    if not rootNode:
        return "The BT does not exist"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data ==nodeValue:
                return "Success"
            
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
                
        return "Not found"
    
print(searchBT(newBT, "Tea"))