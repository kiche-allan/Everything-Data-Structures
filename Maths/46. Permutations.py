# 46. Permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        #base case
        if (len(nums) == 1):
            return [nums.copy()]

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)
        return result