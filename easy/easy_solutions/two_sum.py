from typing import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 1
        while i < len(nums):
            if nums[i] + nums[j] == target:
                return [i, j]
            j += 1
            if j == len(nums):
                i += 1
                j = i + 1



a = Solution()
print(a.twoSum([0, 5, 3, 2, 2], 4))
