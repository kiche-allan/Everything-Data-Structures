class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        color_count = {0:0, 1:0, 2:0 }
         #count the frequencies for each element
        for color in nums:
             color_count[color] += 1

        # Overwrite the original array with the sorted colors.
        index = 0

        for color in range(3):
            for _ in range(color_count[color]):
                nums[index] = color
                index += 1
