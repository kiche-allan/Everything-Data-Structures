class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
     

#assign item values
   
linked_list = LinkedList()
linked_list.head = Node(1)
second = Node(2)
third = Node(3)
forth = Node(4)

#connect nodes

linked_list.head.next = second
second.next = third
third.next = forth

#print the linked list item
while linked_list.head != None:
    print(linked_list.head.data, end= " ")
    linked_list.head = linked_list.head.next
# In this example, the Node class represents a single node in the linked list, with a data attribute that stores the node's value and a next attribute that stores a reference to the next node in the list. The LinkedList class represents the linked list itself, with a head attribute that stores a reference to the first node in the list