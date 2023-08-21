class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        
        
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0
        
class Stack:
    def __init__(self) -> None:
        self.LinkedList = LinkedList()
        
        #make the function iterable
    def __iter__(self):
        curNode = self.head
        while curNode:
            curNode = curNode.next
        
    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False
        
    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node
        
    #pop method
    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue

    #peek method
    def peep(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue
        
        
customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)
print("-------")
print(customStack.pop())
print(customStack)

