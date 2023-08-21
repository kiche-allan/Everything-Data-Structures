# 11. Container With Most Water

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

#brute force method
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        for l in range(len(height)):
            for r in range(l + 1, len(height)):
                area = (r -l) *min(height[l], height[r])
                res = max(res, area)
                
#linear time technique
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1 
        
        while l < r:
            area = (r -l) * min(height[l], height[r])
            res = max(res, area)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res
    
# Describe your first thoughts on how to solve this problem.
# my initial thought on how to solve this problem would be to use a brute force approach. We can calculate the area of all possible containers formed by every pair of lines and keep track of the maximum area found. This would involve using nested loops to compare every pair of lines, and then computing the area of the container formed by those lines. The maximum area found so far can be updated if the area of the current container is greater than the previous maximum.

# While this approach will work, it has a time complexity of O(n^2), where n is the length of the input array. This is because we are comparing every pair of lines, so the number of comparisons we make is proportional to n^2. Therefore, for large input sizes, this approach would be too slow.
 
# Describe your approach to solving the problem.
# A more efficient approach to solve this problem is to use the two-pointer approach, which can solve the problem in O(n) time. In this approach, we use two pointers, one starting from the left end of the array, and the other starting from the right end. We then move the pointer corresponding to the shorter line towards the center of the array, and compute the area of the container formed by those lines. We keep track of the maximum area found so far, and repeat this process until the two pointers meet in the center. This approach is more efficient because we only need to compare every pair of lines once, resulting in a time complexity of O(n).


# compute and explain the complexity of the two pointer approach
# In the two-pointer approach, we initialize two pointers left and right at the start and end of the input array respectively. Then, we calculate the area of the container formed by the two lines at left and right. If this area is greater than the previous maximum, we update the maximum. Then, we move the pointer that corresponds to the shorter line one step towards the center of the array, and repeat the process until the pointers meet in the center.

 #The time complexity of this approach is O(n), where n is the length of the input array. This is because we traverse the array once, and for each step, we either move the left pointer one step towards the center of the array or move the right pointer one step towards the center of the array. Therefore, each pointer can move at most n-1 steps, resulting in a total of O(n) steps.

# Since the time complexity of the two-pointer approach is O(n), it is more efficient than the brute force approach, which has a time complexity of O(n^2).