# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

# Implement the MyQueue class:

# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.
class MyQueue:
    
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def push(self, x: int) -> None:
        """
        Pushes element x to the back of the queue.
        """
        #move all elements from stack1 to stack2
        while self.stack1:
            self.stack2.append(self.stack1.pop())
            
        #push the new element to stack 1
        self.stack1.append(x)
        
        #move all elements from stack2 to stack1
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        
    def pop(self) -> int:
        """
        Removes the element from the front of the queue and returns it.
        """
        if not self.stack1:
            return None
        return self.stack1.pop()
    
    def peek(self) -> int:
        """
        Returns the element at the front of the queue.
        """
        if not self.stack1:
            return None
        return self.stack1[-1]
        
    def empty(self) -> bool:
        """
        Returns true if the queue is empty, false otherwise.
        """
        return not self.stack1
    
    
# Intuition
# To push an element to the back of the queue, I would simply push it onto the input stack. To pop an element from the front of the queue, I would check if the output stack is empty. If it is, I would transfer all the elements from the input stack to the output stack in reverse order, so that the element at the front of the queue becomes the top element of the output stack, and then pop it from the output stack. If the output stack is not empty, I would simply pop the top element from it. To peek at the element at the front of the queue, I would follow the same approach as popping, but without actually popping the element from the output stack. To check if the queue is empty, I would simply check if both the input and output stacks are empty. This approach ensures that the first element that is pushed to the input stack becomes the first element that is popped from the output stack, implementing the FIFO behavior of a queue.

# Approach
# Initialize two stacks, let's call them inputStack and outputStack, to store the elements of the queue.

# Implement the push(x) function:

# Simply push the element x onto the inputStack, as it represents pushing an element to the back of the queue.
# Implement the pop() function:

# Check if the outputStack is empty.
# If it is, transfer all the elements from inputStack to outputStack in reverse order (by popping from inputStack and pushing onto outputStack).
# Pop the top element from outputStack, which represents removing the element from the front of the queue, and return it.
# Implement the peek() function:

# Check if the outputStack is empty.
# If it is, transfer all the elements from inputStack to outputStack in reverse order.
# Peek at the top element of outputStack, which represents the element at the front of the queue, and return it without popping.
# Implement the empty() function:

# Check if both inputStack and outputStack are empty.
# If they are, return True to indicate that the queue is empty, otherwise return False.
# This approach ensures that the elements are maintained in the correct order to implement the FIFO behavior of a queue, and it only uses the standard operations of a stack, such as push, pop, peek, size, and is empty, as mentioned in the problem statement.

# Complexity
# Time complexity:
# Initialize two stacks, let's call them inputStack and outputStack, to store the elements of the queue.

# Implement the push(x) function:

# Simply push the element x onto the inputStack, as it represents pushing an element to the back of the queue.
# Implement the pop() function:

# Check if the outputStack is empty.
# If it is, transfer all the elements from inputStack to outputStack in reverse order (by popping from inputStack and pushing onto outputStack).
# Pop the top element from outputStack, which represents removing the element from the front of the queue, and return it.
# Implement the peek() function:

# Check if the outputStack is empty.
# If it is, transfer all the elements from inputStack to outputStack in reverse order.
# Peek at the top element of outputStack, which represents the element at the front of the queue, and return it without popping.
# Implement the empty() function:

# Check if both inputStack and outputStack are empty.
# If they are, return True to indicate that the queue is empty, otherwise return False.
# This approach ensures that the elements are maintained in the correct order to implement the FIFO behavior of a queue, and it only uses the standard operations of a stack, such as push, pop, peek, size, and is empty, as mentioned in the problem statement.

# Space complexity:
# The space complexity is O(n), where n is the number of elements in the queue. This is because we are using two stacks to store the elements, and in the worst case, all elements may need to be stored in either inputStack or outputStack. However, the actual space used may be less than O(n) on average, as elements are transferred between the two stacks and the maximum space used at any point in time would be the size of the larger stack.