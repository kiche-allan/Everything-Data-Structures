# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.
class ListNode:
    def __init__(self, val =0, next= None):
        self.val = val
        self.next = next
def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    #create a dummy node to serve as the head of the new list
    dummy = ListNode()
    #create  a pointer to the tail of the new list
    tail = dummy
    
    #traverse both lists simultaneously
    while l1 and l2:
        #compare the values of the current nodes of both lists
        if l1.val < l2.val:
            #add the current node of the first list to the new list
            tail.next = l1
            #move the pointer to the tail of the new list to the next node
            tail = l1
            #move the pointer of the first of the first list to the next nosde
            l1 = l1.next
        else:
            #add the current node of the second list to the new list
           tail.next = l2
           #move the pointer to the tail of the new list to the next node 
           tail = l2
           #move the pointer of the secondlst to the next node
           l2 = l2.next
    #append the remaining nodes of the first or second list to the end of the node
    if li:
        tail.next = l1
    else:
        tail.next = l2
    #return the head of the next list(i.e,,. the node after the dummy node)
    
    return dummy.next

# Intuition
# My first thoughts on how to solve this problem would be to use two pointers to traverse both linked lists simultaneously, compare the values of the current nodes of both lists, and add the smaller value to a new linked list. The pointers would then move to the next nodes of the list that contributed the smallest value. This process would continue until all nodes of both lists have been added to the new list. If one of the lists has more nodes than the other, the remaining nodes should be appended to the end of the new list. Finally, we would return the head of the new list.

# Approach
# My approach to solving this problem would be to use two pointers to traverse both linked lists simultaneously, comparing the values of the current nodes of both lists, and adding the smaller value to a new linked list. The pointers would then move to the next nodes of the list that contributed the smallest value. This process would continue until all nodes of both lists have been added to the new list. If one of the lists has more nodes than the other, the remaining nodes should be appended to the end of the new list. Finally, we would return the head of the new list.

# To simplify the implementation, I would create a dummy node that serves as the head of the new list. I would then create a pointer to the tail of the new list, which would initially point to the dummy node. While traversing both lists simultaneously, I would add the smaller node to the tail of the new list and move the tail pointer to the newly added node. After adding all the nodes of one list to the new list, I would append the remaining nodes of the other list to the end of the new list using the tail pointer. Finally, I would return the head of the new list (i.e., the node after the dummy node).

# Complexity
# Time complexity:
# The time complexity of the above solution is O(m+n), where m and n are the lengths of the input linked lists, because we need to traverse both lists only once to create the new merged list. During each iteration of the while loop, we perform constant time operations such as comparing node values, updating the tail pointer, and moving the pointers of the input lists.

# Space complexity:
# The space complexity of the solution is also O(m+n), where m and n are the lengths of the input linked lists. This is because we create a new linked list of size m+n to store the merged list. We also create a dummy node and a tail pointer, which together take up constant space. Therefore, the overall space complexity is proportional to the size of the output, which is O(m+n).