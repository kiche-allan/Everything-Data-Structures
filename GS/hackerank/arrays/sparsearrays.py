# There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings. Return an array of the results.

# Example



# There are  instances of '',  of '' and  of ''. For each query, add an element to the return array, .

# Function Description

# Complete the function matchingStrings in the editor below. The function must return an array of integers representing the frequency of occurrence of each query string in stringList.

# matchingStrings has the following parameters:

# string stringList[n] - an array of strings to search
# string queries[q] - an array of query strings
# Returns

# int[q]: an array of results for each query
# Input Format

# The first line contains and integer , the size of .
# Each of the next  lines contains a string .
# The next line contains , the size of .
# Each of the next  lines contains a string .

def matchingStrings(stringList, queries):
    # Write your code here
    string_freq = {}
    
    #count the frequency of each string in stringList
    for string in stringList:
        if string in string_freq:
            string_freq[string] += 1
        else:
            string_freq[string] = 1
            
            #initialize result to store frequency of query strings
    results = []
    
    #for each query string, check if it exists in string_freq and get its frequency
    for query in queries:
        if query in string_freq:
            results.append(string_freq[query])
        else:
            results.append(0)
    return results