#
# @lc app=leetcode id=2562 lang=python3
#
# [2562] Find the Array Concatenation Value
#

# @lc code=start
class Solution:
    def findTheArrayConcVal(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]  # Jump early

        head: int = 0
        tail: int = len(nums) - 1
        cat_sum: int = 0

        while head <= tail:
            # Odd length base case
            if head == tail:
                cat_sum += nums[head]
                break  # Jump early

            cat_sum += (nums[head] * (10 ** len(str(nums[tail])))) + nums[tail]

            # move pointers
            head += 1
            tail -= 1

        return cat_sum


# @lc code=end
