# You are given the head of a linked list.

# Remove every node which has a node with a strictly greater value anywhere to the right side of it.

# Return the head of the modified linked list.

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr is not None:
            next_node = curr.next
            greater_node = False

            # Check if there is any node with a strictly greater value to the right side of current node
            temp = next_node
            while temp is not None:
                if temp.val > curr.val:
                    greater_node = True
                    break
                temp = temp.next

            if greater_node:
                if prev is not None:
                    prev.next = next_node
                else:
                    head = next_node
            else:
                prev = curr

            curr = next_node

        return head