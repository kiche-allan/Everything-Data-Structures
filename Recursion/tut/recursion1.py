#Recursion is a programming technique where a function calls itself in order to solve a problem. 
#It is often used toperform operations on data structures such as lists or trees where the problem can be broken down into smaller subproblems that are similar in nature to the original problem but smaller in size. A recursive function must have a base case and a recursive case. The base case is the condition that stops the recursion. The recursive case is the condition that calls the function again.

#base case
#recursive case

#the function must always make a progress towards the base case in each recursive call.

#recusrion that calculates the factorial of a number

#the factorial of a number is the product of all the numbers from 1 to that number
#the function "factorial" takes a single argument n and returns the factorial of "n" . The fucntion has a base case where it returns 1 if n is 0. If n is not 0, the function makes a recursive call to factorial(n-1) and multiplies it by n

#this way, the function keeps calling itself with the value of n-1 until the base case is reached, that is n=0. Each time the function calls itelf, it performs a smaller version of the same problem, to calculate factrial of n-1 abd keeps track if the intermediate result, which will be multiplied by n to get the final result.
def factorial(n):
    #base case : the factorial of 0 is 1
    if n == 0:
        return 1
    
    #recursive case: th factorial of n is the n* the factorial of (n-1)
    else:
        return n * factorial(n-1)
    
#test the fuction 
print(factorial(5))
#it prints 120


