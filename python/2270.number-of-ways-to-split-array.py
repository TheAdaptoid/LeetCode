#
# @lc app=leetcode id=2270 lang=python3
#
# [2270] Number of Ways to Split Array
#

# @lc code=start
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        left_total: int = 0
        right_total: int = sum(nums)
        valid_count: int = 0

        for curr_index in range(0, len(nums) - 1):
            split_val: int = nums[curr_index]

            left_total += split_val
            right_total -= split_val

            if left_total >= right_total:
                valid_count += 1

        return valid_count


# @lc code=end
