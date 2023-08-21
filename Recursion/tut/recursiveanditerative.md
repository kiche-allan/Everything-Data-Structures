A recursive function is a function that calls itself. A recursive function must have a base case and a recursive case. The base case is the condition that stops the recursion. The recursive case is the condition that calls the function again.
On the other hand, iterative functions is a function that uses a loop to solve a problem. It repeatedly performs a set of instructions until a certain condition is met. Iterative functions are often used to perform operations on data structures such as lists or trees where the problem can be broken down into smaller subproblems that are similar in nature to the original problem but smaller in size.

Memory - Recursive function uses the call stack to keep track of the state of recursive calls. Each time a recursive call is made, the current state of the function is pushed to the call. As the function completes each recursive call and returns, the state is popped off the call stack. This process can cause a significant amount of memory to be used if the recursion s deep, which can lead to stack overflow errors. Iterative functions, on the other hand, do not use the call stack, so they do not have the same risk of stack overflow errors.

Readability: Recursive functions are often more elegant and easier to understand, especially for problems that have a recursive solution, such as traversing a tree. However, some people may find iterative functions easier to understand, especially for problems that have a iterative solution.

Performance: Recursive functions can be slower than iterative functions, as they make multiple function calls, each of which takes up some overhead. Additionally, the use of the call stack can also add overhead. Iterative functions are generally faster and more efficient as they only perform a set of instructions repeatedly.

when to use recursion

-When we can easily break down a problem into subproblems
-When we are fine with extra overhead(both time and space that comes with it)
-When we need a quick working solution instead of an efficient one
-When we traverse a tree. 