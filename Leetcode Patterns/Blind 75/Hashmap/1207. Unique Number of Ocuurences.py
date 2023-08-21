class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        #create a dictionary to store the count of occurences
        count_dict = {}

        #count the occurencweee of each value in the array
        for num in arr:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1

        #create a set to store the unique occurence counts
        unique_counts = set()

        #check if the count of the occurence for each value is unique
        for count in count_dict.values():
            if count in unique_counts:
                return False
            unique_counts.add(count)

        return True