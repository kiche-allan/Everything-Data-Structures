
# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         slow, fast = head, head

#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#             if slow == fast:
#                 return True

#         return False

#  This is an implementation of the "tortoise and hare" algorithm, which is an efficient way to detect cycles in a linked list.

# The function hasCycle takes a linked list head as input and returns True if the linked list contains a cycle, and False otherwise.

# The algorithm uses two pointers slow and fast, which start at the head of the linked list. The fast pointer moves two steps at a time, while the slow pointer moves one step at a time. If there is a cycle in the linked list, the fast pointer will eventually catch up to the slow pointer, indicating the presence of a cycle.

# The while loop checks if the fast pointer is not None and if fast.next is not None. If either of these conditions is not met, it means that the fast pointer has reached the end of the linked list, and the function returns False. Within the while loop, the slow pointer moves one step forward by setting it equal to slow.next, and the fast pointer moves two steps forward by setting it equal to fast.next.next.

# After each step, the algorithm checks if slow is equal to fast. If they are equal, it means that the fast pointer has caught up to the slow pointer, and there is a cycle in the linked list. The function returns True in this case.

# If the while loop completes without finding a cycle, it means that there is no cycle in the linked list, and the function returns False.

# Overall, this is a concise and efficient implementation of the "tortoise and hare" algorithm to detect cycles in a linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def hasCycle(head: ListNode) -> bool:
    if not head or not head.next: # Handle empty or single-node linked list
        return False
    
    tortoise = head
    hare = head.next
    
    while hare and hare.next:
        if hare == tortoise: # Cycle detected
            return True
        
        tortoise = tortoise.next
        hare = hare.next.next
        
    return False

# This code defines a ListNode class to represent each node in the linked list, with a val attribute for the node's value and a next attribute for the next node in the list. The hasCycle function takes a head argument, which is a pointer to the head of the linked list, and returns a boolean indicating whether the linked list contains a cycle.

# In the function, we first handle the special cases of an empty linked list or a linked list with only one node. If either of these cases applies, we return False immediately.

# Next, we initialize the tortoise and hare pointers to the head of the linked list and the next node, respectively. We then enter a while loop that continues until either the hare reaches the end of the list or the hare catches up to the tortoise. Within the loop, we move the pointers as described above, and we use an if statement to check if the hare has caught up to the tortoise. If it has, we return True to indicate the presence of a cycle. If the loop completes without finding a cycle, we return False.

# Overall, this code uses the "tortoise and hare" algorithm to detect cycles in a linked list, and it handles all special cases appropriately.



# Both implementations use the "tortoise and hare" algorithm to detect cycles in a linked list, and they have the same time and space complexity.

# The main difference between the two implementations is that the code I wrote is a standalone function, while the code you provided is a method of a class called Solution. This means that in order to use the hasCycle method, you would first need to create an instance of the Solution class.

# In addition, the input and output types of the two functions are slightly different. The hasCycle function I wrote takes a ListNode as input and returns a boolean, while the hasCycle method you provided takes an Optional[ListNode] as input and returns a boolean. The Optional type indicates that the input can be None, which is not necessary in the function I wrote since it assumes that the input is a valid ListNode.

# Overall, both implementations are correct and use the same algorithm to detect cycles in a linked list, but they have slightly different syntax and input/output types.

# Intuition
# My first thoughts on how to solve this problem involve using the "tortoise and hare" algorithm, also known as Floyd's cycle-finding algorithm. This is a well-known algorithm for detecting cycles in a linked list, and it involves using two pointers, one that moves one step at a time (the "tortoise") and another that moves two steps at a time (the "hare"). If there is a cycle in the linked list, the hare will eventually catch up to the tortoise, indicating the presence of a cycle.

# To implement this algorithm, I would initialize both pointers to the head of the linked list and then move them through the list in tandem, with the hare moving twice as fast as the tortoise. If the hare ever reaches the end of the list (i.e., its next node is null), then there is no cycle in the list. However, if the hare catches up to the tortoise at some point, then we know that there is a cycle in the list.

# I would implement this algorithm in code using a while loop that continues until either the hare reaches the end of the list or the hare catches up to the tortoise. Within the loop, I would move the pointers as described above, and I would use a conditional statement to check if the hare has caught up to the tortoise. If it has, then I would return True, indicating the presence of a cycle. If the loop completes without finding a cycle, then I would return False.

# Approach
# To solve the problem of detecting cycles in a linked list, my approach would involve using the "tortoise and hare" algorithm, also known as Floyd's cycle-finding algorithm. This algorithm uses two pointers, one that moves one step at a time (the "tortoise") and another that moves two steps at a time (the "hare"), to traverse the linked list. If there is a cycle in the list, the hare will eventually catch up to the tortoise, indicating the presence of a cycle.

# To implement this algorithm in code, I would start by initializing the two pointers to the head of the linked list. Then, I would create a while loop that continues until either the hare pointer reaches the end of the list (i.e., its next node is null) or the hare catches up to the tortoise. Within the loop, I would move the pointers as follows:

# The tortoise moves one step forward by setting it equal to its next node.
# The hare moves two steps forward by setting it equal to its next node's next node.
# After each step, I would check if the hare has caught up to the tortoise by comparing their memory addresses. If they are equal, then there is a cycle in the linked list, and I would return True. If the loop completes without finding a cycle, I would return False.

# One special case to consider is when the linked list is empty or has only one node. In this case, there can be no cycle, so I would return False without entering the loop.

# Overall, my approach involves using a well-known algorithm to solve the problem of detecting cycles in a linked list in an efficient and elegant way.

# Complexity
# Time complexity:
# 0(n)
# The time complexity of the given solution is O(n), where n is the number of nodes in the linked list. This is because the algorithm iterates through the linked list once, and in each iteration, it performs a constant amount of work (i.e., moving the two pointers by one or two nodes and checking if they meet). Therefore, the time complexity is linear in the size of the input.

# Space complexity:
# 0(1)
# The space complexity of the solution is O(1), which is constant. This is because the algorithm only uses two pointers (slow and fast) to traverse the linked list, and it does not use any extra data structures that depend on the size of the input. Therefore, the space used by the algorithm is independent of the size of the input, and it is constant regardless of the size of the linked list.