#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        occur = {}
        for i in nums:
            if i in occur:
                occur[i] += 1
            else:
                occur[i] = 1

        return [key for key, value in occur.items() if value == 1][0]


# @lc code=end
