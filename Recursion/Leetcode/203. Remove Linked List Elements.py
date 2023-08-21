# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr is not None:
            if curr.val == val:
                if prev is not None:
                    prev.next = curr.next
                else:
                    head = curr.next
            else:
                prev = curr
                
            curr = curr.next
            
        return head
    
    
#     We start with the removeElements method of the Solution class, which takes two parameters as input: head, the head of the linked list, and val, the value of the nodes to be removed from the linked list.

# We then initialize two pointers - prev and curr - to None and head, respectively. These pointers will be used to keep track of the previous node and the current node as we traverse through the linked list.

# We then enter a while loop that continues until curr is not None, which means we have not reached the end of the linked list.

# Inside the loop, we first check if the value of curr (i.e., curr.val) is equal to the given val. If it is, we remove the current node from the linked list by updating the next pointer of the previous node (prev.next) to skip the current node (curr.next). This effectively removes the node with the value val from the linked list.

# If the value of curr is not equal to the given val, we update prev to be curr, effectively moving prev one step forward in the linked list.

# Finally, we update curr to be curr.next, moving curr one step forward in the linked list for the next iteration.

# After the loop, we return the head of the modified linked list as the final result. If the first node(s) of the original linked list had the value val and were removed, the new head would be updated to skip those node(s). If no nodes were removed, the head remains unchanged.