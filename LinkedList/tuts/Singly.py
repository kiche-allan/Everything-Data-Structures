class Node:
    def __init__(self) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0
        
singly_linked_list = LinkedList()
node1 = Node(1)
node2 = Node(2)

#connect the nodes
singly_linked_list.head = node1
singly_linked_list.head.next = node2
singly_linked_list.tail = node2

#delete a node from singly linked list
def deleteNode(self, location):
    if self.head is None:
        print('The SSL does not exist')
        
    else:
        if location == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                
        elif location == 1:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                node = self.head 
                while node is not None:
                    if node.next == self.tail:
                        break
                    node = node.next
                node.next = None
                self.tail = node
                
        else:
            tempNode = self.head
            index = 0
            while index < location - 1:
                tempNode = tempNode.next
                index += 1
            nextNode = tempNode.next
            tempNode.next = nextNode.next
                
singleLinkedList = LinkedList()
singleLinkedList.insertNode(1, 1)
singleLinkedList.insertNode(2, 1)
singleLinkedList.insertNode(3, 1)
singleLinkedList.insertNode(4, 2)
singleLinkedList.insertNode(0, 0)
singleLinkedList.insertNode(0, 4)

print([node.value for node in singleLinkedList])
singleLinkedList.deleteNode(3)
print([node.value for node in singleLinkedList])
                 
                
            
                