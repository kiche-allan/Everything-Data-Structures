# 24. Swap Nodes in Pairs
# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values inwhww the list's nodes (i.e., only nodes themselves may be changed.)

class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next
        
class Solution:
    def swapPairs(self, head:Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0) #create a dummy node as the new head
        dummy.next = head #set the next of the dummy to the original head
        prev = dummy #set prev as the dummy node
        
        while head and head.next:
            #nodes need to be swapped
            node1 = head
            node2 = head.next
            
            #update the links
            prev.next = node2
            node1.next = node2.next
            node2.next = node1
            
            #move the head and prev for the next iteration
            prev = node1
            head = node1.next
            
        return dummy.next #return the new head
    
# Create a dummy node: We create a dummy node with a value of 0, which serves as the new head of the swapped linked list. We also set the next of the dummy node to the original head, so that we can easily manipulate the linked list.

# Initialize pointers: We initialize two pointers, prev and head, initially pointing to the dummy node. The prev pointer will be used to keep track of the previous node, and the head pointer will be used to iterate through the linked list.

# Swap pairs of nodes: We enter a loop that continues until there are at least two nodes to swap. Inside the loop, we first identify the nodes that need to be swapped - node1 and node2, where node1 is the current head and node2 is the next node after head.

# Update the links: We update the links to swap the nodes. Specifically, we set prev.next to node2 to connect the previous node (prev) to the second node (node2). We also set node1.next to node2.next to connect the first node (node1) to the node after node2. Finally, we set node2.next to node1 to connect the second node (node2) to the first node (node1), effectively swapping their positions.

# Move pointers: We move the prev and head pointers to prepare for the next iteration. We set prev to node1, which is now the last node in the swapped pair, and we set head to node1.next, which is the next node after the swapped pair.

# Repeat: We repeat steps 3-5 until there are no more pairs of nodes to swap.

# Return the new head: Once the loop completes, we return dummy.next, which is the new head of the swapped linked list.