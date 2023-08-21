# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0 #variable to store the count of negative numbers
        
        #iterate through each row in the matrix
        for row in grid:
            left = 0
            right = len(row) - 1
            
            #perform binary search within the current row
            while left <= right:
                mid = (left + right) // 2
                
                #if the current element is negative
                if row[mid] < 0:
                    count += right - mid + 1
                    right = mid - 1
                    
                else:
                    left = mid + 1
                    
        return count
    
# Certainly! Here's a step-by-step explanation of how the code works:

# The countNegatives function takes a 2D matrix grid as input.

# It initializes a variable count to keep track of the count of negative numbers in the matrix.

# The function iterates through each row in the matrix using a for loop.

# For each row, it performs a binary search to find the first negative number (if any) using the variables left and right.

# Inside the binary search loop, the function calculates the mid index as the average of left and right.

# If the value at the mid index in the current row is negative (row[mid] < 0), it means there are negative numbers to the right of the mid index.

# In that case, the count is incremented by right - mid + 1, which represents the number of negative numbers in the remaining portion of the row (from mid to right).

# After updating the count, the right index is updated to mid - 1 to continue searching for negative numbers in the left portion of the row.

# If the value at the mid index is not negative, it means the negative numbers lie to the right of the mid index. In this case, the left index is updated to mid + 1 to search in the right portion of the row.

# The binary search loop continues until left becomes greater than right, indicating that the entire row has been searched.

# The process repeats for each row in the matrix, accumulating the count of negative numbers.

# Finally, the function returns the total count of negative numbers found in the matrix.

# By performing binary search on each row, the algorithm efficiently counts the number of negative numbers in the matrix. Since the matrix is sorted in non-increasing order, binary search helps in quickly narrowing down the search space to find the negative numbers in logarithmic time complexity.