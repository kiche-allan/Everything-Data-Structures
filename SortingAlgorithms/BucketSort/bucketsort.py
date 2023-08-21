# create buckets and distribute elements of array into buckets
# sort buckets individually
# merge buckets after sorting

# Bucket sort is a sorting algorithm that works by distributing the elements of an array into a number of buckets. Each bucket is then sorted using another algorithm, such as insertion sort, and the sorted buckets are concatenated to form the final sorted array. Here is the basic algorithm:

# Create an array of empty buckets.
# Iterate through the input array and insert each element into the appropriate bucket based on some hashing function.
# Sort each bucket using another sorting algorithm, such as insertion sort.
# Concatenate the sorted buckets in order to produce the sorted array.

def bucket_sort(arr, bucket_size= 5):
    if len(arr) ==0:
        return arr
    
    #find range of input data
    min_val, max_val = min(arr), max(arr)
    
    #compute bucket size
    bucket_count = (max_val - min_val)
    buckets = [[] for _ in range(bucket_count)]
    
    #distribute input data into buckets
    for i in range(len(arr)):
        index = (arr[i] - min_val)
        buckets[index].append(arr[i])
        
        
    #sort each bucket using insertion sort
    for i in range (len(buckets)):
        buckets[i].sort()
        
    #concatenate the sorted buckets
    return [buckets[i][j] for i in range(len(buckets)) for j in range(len(buckets[i])) ]

# In this implementation, arr is the input array to be sorted, and bucket_size is the size of each bucket. The algorithm first finds the range of input data and computes the number of buckets needed based on the bucket size. It then distributes the input data into the appropriate buckets based on a hashing function. Each bucket is sorted using insertion sort, and the sortebuck2d buckets are concatenated to form the final sorted array.