#the fibonacci numbers are a sequence of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1. The sequence goes like: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

#the fibonnacci numbers can be defined using recusrsion as follows:
# - the first fibonnacci number is 0
# - the second fibonnacci number is 1
# - each subsequent fibonacci number is the sum of the previous two fibonacci numbers

def fibonacci(n):
    #base case: the first two fibonacci numbers are 0 and 1
    if n==0 :
        return n
    elif n ==1:
        return 1
    #recuraive case: the nth fibonacci number is the sum of the (n-1)th and (n-2)th fibonacci numbers
    
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
    #test the function
    
for i in range(10):
    print(fibonacci(i), end = " ")
    
    #explanation of every line of code
    
    #the above line defines a function called fibonacci that takes a single argument n and returns the nth fibonacci number. 
    def fibonacci(n):
        
    # The function has two base cases: when n is 0 or 1, it either returns 0 or 1. the recursive case is when n is greater than 1, in which case the function calls itself twice, once with n -1 and once with n-2, and adds the results together. The function keeps calling itself until the base case is reached, and then returns the result of the addition.
            # Base case: the first two Fibonacci numbers are 0 and 1
        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        # These lines serve as the base case for recursion, where the recursion stops. The first base case returns 0 when the input value n is 0, as the first Fibonacci number is 0. The second base case returns 1 when the input value n is 1, as the second Fibonacci number is 1.
        
            # Recursive case: the nth Fibonacci number is the sum of the (n-1)th and (n-2)th Fibonacci numbers
        else:
            return fibonacci(n-1) + fibonacci(n-2)
        #the above line defines a recursive case. when n is greater than 1, the function calls itself twice, once with n-1 and once with n-2, 

        

    
