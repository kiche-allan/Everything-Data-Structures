# Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

# You must write an algorithm that runs in linear time and uses linear extra space.
 
#  No, most sorting algorithms do not run in linear time. The best time complexity achievable by comparison-based sorting algorithms, such as quicksort, mergesort, and heapsort, is O(n log n), where n is the number of elements in the array.

# Linear time sorting algorithms, such as counting sort, radix sort, and bucket sort, are not based on comparisons and have specific constraints on the input data. They are efficient when the range of input values is small or when the input has a particular structure. However, these linear time sorting algorithms do not work for arbitrary inputs and may require additional conditions or modifications.

# Therefore, if the requirement is to find the maximum difference between two successive elements in the sorted form of an array and the algorithm must run in linear time, using a sorting algorithm alone would not satisfy this requirement. The bucket sort approach described earlier allows finding the maximum difference in linear time but does not actually sort the entire array.

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        
        # Check if the list is empty or contains only one element
        if len(nums) < 2:
            return 0
        
        # Get the minimum and maximum values in the list
        min_val = min(nums)
        max_val = max(nums)
        
        # Calculate the bucket size and number of buckets
        bucket_size = max(1, (max_val - min_val) // (len(nums) - 1))
        num_buckets = (max_val - min_val) // bucket_size + 1
        
        # Initialize the buckets
        buckets = [None] * num_buckets
        
        # Put each element in its corresponding bucket
        for num in nums:
            bucket_index = (num - min_val) // bucket_size
            if not buckets[bucket_index]:
                buckets[bucket_index] = {'min': num, 'max': num}
            else:
                buckets[bucket_index]['min'] = min(buckets[bucket_index]['min'], num)
                buckets[bucket_index]['max'] = max(buckets[bucket_index]['max'], num)
        
        # Calculate the maximum gap between adjacent buckets
        max_gap = 0
        prev_max = min_val
        for bucket in buckets:
            if bucket:
                max_gap = max(max_gap, bucket['min'] - prev_max)
                prev_max = bucket['max']
        
        return max_gap
# We define a Solution class with a maximumGap method that takes a list of integers nums as input and returns an integer, the maximum gap between two successive elements in the sorted form of nums.

# We check if the length of nums is less than 2, and return 0 if so, because we cannot find a gap between two elements if there is only one or none.

# We get the minimum and maximum values in nums using the built-in min and max functions.

# We calculate the bucket size as the maximum of 1 and the integer division of the range of nums (i.e., max_val - min_val) by the number of elements in nums minus 1 (i.e., len(nums) - 1). This ensures that we have at least one element in each bucket. We also calculate the number of buckets as the integer division of the range of nums by the bucket size plus 1, to ensure that we have a bucket for the maximum value.

# We initialize an empty list buckets of length num_buckets to hold the buckets.

# We loop through each element num in nums and calculate the index of the bucket it belongs to as the integer division of its distance from min_val by the bucket size. We then check if the corresponding bucket is empty or not, and if it is, we initialize it with the min and max values of num. Otherwise, we update the min and max values of the bucket with the minimum and maximum of num and the current min and max values, respectively.

# We initialize a variable max_gap to hold the maximum gap between adjacent buckets, and a variable prev_max to hold the maximum value in the previous bucket, initially set to min_val.

# We loop through each bucket in buckets, and if it is not empty, we update max_gap with the difference between its `min

# Complexity
# Time complexity:
# Space complexity:
    