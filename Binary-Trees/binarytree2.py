class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size
        
newBT = BinaryTree(8)


def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            rootNode = customQueue.dequeue()
            if rootNode.leftChild:
                customQueue.enqueue(rootNode.leftChild)
            if rootNode.rightChild:
                customQueue.enqueue(rootNode.rightChild)
        deepesNode = root.value
        return deepesNode
    
deepesNode = getDeepestNode(newBT)
print(deepesNode.data)

def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            rootNode = customQueue.dequeue()
            if rootNode is dNode:
                rootNode = None
                return
            if rootNode.rightChild:
                if rootNode.rightChild is dNode:
                    rootNode.rightChild = None
                    return
                else:
                    customQueue.enqueue(rootNode.rightChild)
            if rootNode.leftChild:
                if rootNode.leftChild is dNode:
                    rootNode.leftChild = None
                    return
                else:
                    customQueue.enqueue(rootNode.leftChild)

def deleteNodeBT(rootNode, node):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            rootNode = customQueue.dequeue()
            if rootNode.data == node:
                rootNode.data = getDeepestNode(rootNode)
                deleteDeepestNode(rootNode)
                return
            if rootNode.leftChild:
                customQueue.enqueue(rootNode.leftChild)
            if rootNode.rightChild:
                customQueue.enqueue(rootNode.rightChild)
                
def searchNode(self, nodeValue):
    if not self.rootNode:
        return "The tree does not exist"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(self.rootNode)
        while not (customQueue.isEmpty()):
            rootNode = customQueue.dequeue()
            if rootNode.data == nodeValue:
                return "The node is present in the tree"
            if rootNode.leftChild:
                customQueue.enqueue(rootNode.leftChild)
            if rootNode.rightChild:
                customQueue.enqueue(rootNode.rightChild)
        return "The node is not present in the tree"
                    
newNode = getDeepestNode(newBT)
deleteDeepestNode(newBT, newNode)
levelOrderTraversal(newBT)
