#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for leftIndex in range(len(nums)):
            for rightIndex in range(leftIndex + 1, len(nums)):
                if nums[leftIndex] + nums[rightIndex] == target:
                    return [leftIndex, rightIndex]


# @lc code=end
