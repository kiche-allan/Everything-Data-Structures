class Solution:
    def TwoSum(self, nums:int, target: int) -> int:
        PrevIndices = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in PrevIndices:
                PrevIndices = [[diff[num]], i]

        return []