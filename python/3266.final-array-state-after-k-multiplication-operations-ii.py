#
# @lc app=leetcode id=3266 lang=python3
#
# [3266] Final Array State After K Multiplication Operations II
#

# @lc code=start
from heapq import heapify


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for oper in range(k):
            index: int = min(enumerate(nums), key=lambda x: x[1])[0]
            nums[index] *= multiplier

        nums = [expr for operation in range(k)]

        mod: int = (10**9) + 7
        nums_mod: list[int] = [val % mod for val in nums]
        return nums_mod


# @lc code=end
