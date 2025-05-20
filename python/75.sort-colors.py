#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, 0

        for num in nums:
            if num == 0:
                red += 1
            elif num == 1:
                white += 1
            else:
                blue += 1

        for index in range(len(nums)):
            if index < red:
                nums[index] = 0
            elif index < red + white:
                nums[index] = 1
            else:
                nums[index] = 2


# @lc code=end
