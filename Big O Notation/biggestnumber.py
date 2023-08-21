def findBiggestNumber(sampleArray):
    biggestNumber = sampleArray[0]
    for index in range(1, len(sampleArray)):
        if sampleArray[index] > biggestNumber:
            biggestNumber = sampleArray[index]
        print(biggestNumber)
        
#     This is a Python function that takes an array called "sampleArray" as an input and finds the largest number in that array.

# It starts by initializing a variable "biggestNumber" to the first element of the array (sampleArray[0]).

# Then, it uses a for loop to iterate through the array starting from the second element (index 1) to the last element. In each iteration, it compares the current element (sampleArray[index]) with the current "biggestNumber". If the current element is greater than the current "biggestNumber", it assigns the current element to "biggestNumber".

# Finally, after the loop is finished, it returns the value of the "biggestNumber" which will be the biggest number in the input array.

# It also has a print(biggestNumber) statement inside the for loop, this will print the biggest number found till the current iteration, this could be useful for debugging or understanding the function's behavior.