# In implementing a stack with quesues, we can only implement 0(n) when pushing but 0(1) when popping time complexities. This is because we have to pop all the elements from the queue and push them back to the queue except the last element. This is done by using a temporary queue to store the elements. We can also implement 0(1) when popping but 0(n) when pushing time complexities. This is because we have to pop all the elements from the queue and push them back to the queue except the last element. This is done by using a temporary queue to store the elements.

class MyStack:
    def __init__(self):
        self.q = deque()
        
    def push(self, x: int) -> None:
        self.q.append(x)
        
    def pop(self) -> int:
        for i in range(len(self.q) -1):
            self.push(self.q.popleft())
            
        return self.q.popleft()
        
        
    def top(self) -> int:
        return self.q[-1]
        
    
    def empty(self) -> bool:
        return len(self.q) == 0
   
            
# The above code implements a stack using a deque data structure in Python. The deque data structure is a double-ended queue that supports adding and removing elements from either end of the queue. The deque data structure is a double-ended queue that supports adding and removing elements from either end of the queue.

# The MyStack class has the init method that initializes a deque q as an empty container. The class also has a push method that adds an integer 'x' to the end of the deque using the append method.
# The pop method, which removes and returns the last element in the stack, works by moving all elements except the last one to the beginning of the deque using a loop that iterates over len(self.q) - 1 times.

# The popleft method is used to remove the first element of the deque and add it back to the end of the deque using the push method. Finally, the last element of the deque, which is the original last element of the stack, is removed and returned using popleft.

# One important note is that this implementation has a time complexity of O(n) for the pop method, where n is the number of elements in the stack. This is because, in the worst case, we need to move all elements in the deque to the front to access the last element.


# Intuition
# If I were to solve this problem myself, my initial thought would be to use a list to implement the stack instead of a deque.
# In Python, a list is a dynamic array that supports both constant time append and pop operations. This makes it an excellent choice for implementing a stack, as we can simply append elements to the end of the list to push them onto the stack, and pop elements from the end of the list to pop them off the stack.

# Approach
# The key to using a deque as a stack is to always insert new elements at the beginning of the deque and remove elements from the beginning of the deque. This way, the most recent element that was added to the stack is always at the front of the deque, and is the first element to be removed when we pop from the stack.

# Complexity
# Time complexity:
# The time complexity of the push method in the code provided is O(1), since appending an element to the end of a deque using the append method takes constant time.

# However, the time complexity of the pop method in the code provided is O(n), where n is the number of elements in the stack. This is because the code iterates over the first n-1 elements in the deque using a for loop, and for each iteration, it removes the first element of the deque using popleft() and adds it to the end of the deque using append(). This has the effect of rotating the elements in the deque, so that the last element becomes the first element (i.e., the element that will be popped).

# The worst-case scenario is when the element that needs to be popped is at the bottom of the stack, in which case the pop method will need to rotate all n elements in the deque, taking O(n) time. However, if the element that needs to be popped is near the top of the stack, the pop method may be able to complete in less than O(n) time, as it will only need to rotate a smaller number of elements.

# Overall, the time complexity of this implementation is not ideal, as it can result in slow pop times when the stack contains a large number of elements. If constant-time pop performance is important for your use case, it may be better to use a list or a deque with a different implementation.

# Space complexity:
# 0(1)