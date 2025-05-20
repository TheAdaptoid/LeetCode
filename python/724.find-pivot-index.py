#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start


class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left_sum: int = 0
        middle_val: int = 0
        right_sum: int = sum(nums)  # O(n)

        for idx, val in enumerate(nums):  # O(n)
            # Move middle to left
            left_sum += middle_val

            # Replace the middle with the
            # next from the right
            middle_val = val

            # Remove next from right
            # from the right sum
            right_sum -= val

            # Success case
            if left_sum == right_sum:
                return idx

        # Fail case
        return -1


# @lc code=end
