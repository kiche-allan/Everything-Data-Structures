# 4. Median of Two Sorted Arrays

# One approach to solving this problem is to use a binary search algorithm to find the median. The basic idea is to divide both arrays into two parts such that the left part have the same number of elements and the right parts have the same number of elements. Then if the maximum element of the left part of the first array is less than or equal to the minimum element of the right part of the secod array, and the maximum element of the left part of the second array is less than or equal to the minimum element of the right part of the first array, we have found the median.

# Otherwise, we can use the binary search algorithm to continue dividing the arrays and searching for the median.

# To achieve a time complexity of O(log(m+n)), we can use a modified version of binary search called "binary search with variable length", which allows us to search in arrays of different sizes in logarithmic time.

# Overall the algorithm is called as Median of Two Sorted Array, which can be solved using the variant of binary search called Binary Search with variable length.


#the code defines a class solution that contains a method findMedianSortedArrays which takes in two parameters, 'num1' and 'num2' which are the two sorted arrays for which we are trying to find median
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #The method first creates two variables A and B and assigns them the values of nums1 and nums2 respectively.
        A, B = nums1, nums2
        
        #The variable total is defined as the sum of the lengths of the two input arrays, nums1 and nums2
        total = len(nums1) + len(nums2)
        
        #The variable half is defined as the floor division of total by 2
        half = total // 2
        
        
        #The code then checks if the length of array B is less than that of array A. If it is, the values of A and B are swapped.
        if len(B) < len(A):
            #swap the values 
            A, B = B, A
        #run the binary values 
        #Two variables l and r are defined and are assigned the values of 0 and (length of A - 1) respectively.
        l, r = 0, len(A)  - 1
        
        #The code then enters into an infinite loop, which will only be broken out of when the median of the two arrays is found.
        while True:
            #Within the loop, there are two variables i and j defined. i is assigned the floor division of the sum of l and r by 2. j is assigned the value of half - i - 2.
            i = (l + r) // 2    #A
            j = half - i - 2   #B
            
            
            #The code then defines four variables: Aleft, Aright, Bleft, and Bright. Aleft is assigned the value of the element at index i in array A, if i is greater than or equal to 0. Otherwise, it is assigned the value of negative infinity. Aright is assigned the value of the element at index (i + 1) in array A, if (i + 1) is less than the length of A. Otherwise, it is assigned the value of positive infinity. Bleft is assigned the value of the element at index j in array B, if j is greater than or equal to 0. Otherwise, it is assigned the value of negative infinity. Bright is assigned the value of the element at index (j + 1) in array B, if (j + 1) is less than the length of B. Otherwise, it is assigned the value of positive infinity.

#The code then checks if Aleft is less than or equal to Bright and Bleft is less than or equal to Aright. If both conditions are true, the median has been found. If total is odd, the median is returned as the minimum of Aright and Bright. If total is even, the median is returned as the average of the maximum of Aleft and Bleft and the minimum of Aright and Bright.

#If the above conditions are not true, the code checks if Aleft is greater than Bright. If it is, the value of r is updated to be i - 1. If not, the value of l is updated to be i + 1.

#The loop continues until the median is found and returned.





            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i +1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) <len(B) else float("infinity")
            
            if Aleft <= Bright and Bleft <= Aright:
                #odd
                if total % 2:
                    return min(Aright, Bright)
                
                #even 
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i -1
            else:
                l = i +1 
                     
    # Describe your first thoughts on how to solve this problem
#my first thoughts will be to combine the two sorted arrays into one sorted array and then find the median of the array. To combine the arrays, I would iterate through the arrays comparing the current element from each array and adding the smaller element to the combined array. I would repeat this process until all the elements from both arrays are added to the combined array. Once both have been processed, the median of the combined array can be calculated by finding the middle elements of the new array. If the combined array has an odd number of elements , the median is the middle element. If it has an even number, the media is the everage of the two middle elements.



#Describe your approach to solving the problem.
#My approach to solving this problem would be to use binary search as this allows us to find the median more efficiently than combining the arrays. I would divide the arrays into halves in each iteration of binary search and compare the valuesto dtermine which half of the arrays to continue searching in. I would keep track of the indices of the halves of the arrays and use them to calculate the median. I would continue this process until the median is found. The time complexity of this algorithm is O(log(m+n)). The space complexity is O(1) as we are not using any extra space to store the arrays.

#Once I find the two elements such that one element from the first array is less than or equal to the next element in the second array and vice versa, I would calculate the median based on whether the total number of elements in both arrays is odd or even. If the total number of elements is odd, I would return the minimum of the two elements found in the current iteration.

#explain the time complexity of the above question

# The time complexity of the above solution is O(log(m+n)). The space complexity is O(1) as we are not using any extra space to store the arrays.
# The time complexity of the above solution is O(log(min(len(nums1), len(nums2)))). This is because the solution uses a binary search,the search space is divided in half. As a result, the number of iterations required is proportional to log(min(len(nums1), len(nums2))). In each iteration, a constant amount of work is done such as index calculation and element of comparison, so the overal time complexity is O(log(min(len(nums1), len(nums2)))).

# The reason the time complexity is logarithmic with respect to the minimum length of the two arrays, and not their sum, is that the solution only needs to search one of the arrays in each iteration, and the array with the smaller length is chosen to be searched. This ensures that the number of elements to search through in each iteration is always kept to a minimum.
        
#The space complexity is O(1) as we are not using any extra space to store the arrays.
#This is because the solution only uses a constant amount of space to store the variables used in the algorithm. The space complexity is O(1) as we are not using any extra space to store the arrays.    







