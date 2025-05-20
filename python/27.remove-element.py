#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for item in nums:
            if item == val:
                count += 1

        for i in range(count):
            nums.remove(val)

        return len(nums)


# @lc code=end
