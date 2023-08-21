#a common usecase  for recusriion is traversing and manipulating tree-like data structures. Here is an example of a recursive function that traverses a tree and prints the value of each node in the tree.

class Node:
    def __init__(self, value, left = None, right= None):
        #the above line defines a class 'node' and a method '__init__' that takes three arguments of vaue, left and right. the left and right arguments are optional and default to None. 'value' is the value of the node, 'left' is a reference of the left child node and 'right' is a reference to the right child node. 
        
        #self is not an explicit argument in the above code because it is automatically passed by Python to a method when it is called on an instance of a class. 
        
        #in the above code, 'self' is passed to the '__init__' and 'print_tree' method as the first argument when it is called on an instance of the class 'Node'.
        #'self'is used to refer to the current isntance of the class This allows the method to set the value of the instance variables, 'self.value', 'self.left' and 'self.right' to the values passed to the '__init__' method.
        
        #  Similarly, in the print_tree method, self is used to refer to the current instance of the class and access its attributes such as value, left, and right.
        
        #In python, self is used as a way to refer to the instance of a class, this is why it's not necessary to pass it as an explicit argument. It is automatically passed by Python when a method is called on an instance of a class.
        
        self.value = value
        self.left = left
        self.right = right
        #the above lines set the value of the instance variable of the object. 
        
def print_tree(node):
    if node is None:
                return
            #this line defines a function 'print_tree' which takes a single argument node which is the current node that is being traversed.
            
            
            #this line checks if the current node is None. If it is, the function returns without printing anything. iT SERVES AS THE BASE CASE FOR RECURSION where the recursion stops. 
    print(node.value)
    print_tree(node.left)
    print_tree(node.right)
            
            # these lines make the recursive call to the function, first with the left child node and then with the right child node. This way the function keeps traversing the tree, visiting each node exactly once
            
            
            #create a simple tree
root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
            
            #This line creates an instance of the Node class to create a sample tree. The tree has a root node with value 1, which has left child node with value 2 and right child node with value 3. The left child node has left child node with value 4 and right child node with value 5. Similarly, the right child node has left child node with value 6 and right child node with value 7.
            
            #print the tree 
print_tree(root)
            #THE LINE PRINTS THE 'PRINT-_TREE' FUNCTION WITH THE ROOT OF THE TREE AS THE ARGUMENT. THIS STARTS THE RECURSION AND TRAVERSAL OF THE TREE.
        
        